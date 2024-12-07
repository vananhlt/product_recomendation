import streamlit as st
import pandas as pd
from PIL import Image
import pickle
from utils.gui import icon, space, hbar

# Lấy danh sách userID để đưa vào Account sidebar
customer = pd.read_csv('data/Khach_hang.csv')
USERID_OPTIONS = customer['ma_khach_hang'].values[0:20]

# Lấy danh sách sản phẩm content-based để recomended
products = pd.read_csv('data/San_pham.csv')
ITEMS_OPTIONS = products['ten_san_pham'].values[0:20]

# Đọc danh sách đề xuất sản phẩm
with open('data/products_gensim_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)


# Lấy danh sách recomended theo userID
RECOMENDED_USERID = pd.read_csv('data/alsResult_rec.csv')

emoji = '🤔'
st.set_page_config(
    page_title='Prediction - About app', page_icon=emoji, layout='centered'
)

icon("🤔")
st.title('About this app')

st.write(
    """
### How does this app work?
- With Content-based filtering (model gensim) Using select product.
- With Collaborative Filtering (model ALS) selection UserID in the sibebar.

"""
)
###💬 Questions? Comments?
# content = st.text_area(label='Input your Questions/Comments:')
# if content!="":
    # st.download_button(label='Send Comments', data=content, file_name='my_notes.txt')

# st.write(f'You wrote {len(content)} characters.')
hbar()

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def get_recommendations(sp_id, cosine_sim=cosine_sim, df=products, nums=5):
        
    # Get the index of the product that matches the ma_san_pham
    matching_indices = df.index[df['ma_san_pham'] == sp_id].tolist()
    if not matching_indices:
        print(f'No product found with ID: {sp_id}')
        return pd.DataFrame()  # Return an empty DataFrame if no match

    idx = matching_indices[0]
    sim_scores = pd.DataFrame(cosine_sim)
    sim_scores = sim_scores[idx]
    sim_scores = sim_scores.sort_values(key=lambda x: x, ascending=False)
    sim_scores = sim_scores[1:nums+1]  # Lấy n sản phẩm tương tự nhất
    product_indices = [i for i in sim_scores.index]
    result = df.iloc[product_indices]
    result = result.sort_values(by=['diem_trung_binh'], ascending=False)
    
    # Chỉ đề xuất nếu điểm trung bình lớn hơn 3
    result = result[result['diem_trung_binh']>3]
    result = result[['ma_san_pham', 'ten_san_pham',	'gia_ban', 'gia_goc', 'diem_trung_binh', 'mo_ta']]

    return result

# def display_recommended_products_with_expander(recommended_products, cols=5):
#     # Hiển thị đề xuất ra bảng
#     for i in range(0, len(recommended_products), cols):
#         cols = st.columns(cols)
#         for j, col in enumerate(cols):
#             if i + j < len(recommended_products):
#                 product = recommended_products.iloc[i + j]
#                 with col:   
#                     st.write(product['ten_san_pham'])                    
#                     expander = st.expander(f"Mô tả")
#                     product_description = product['mo_ta']
#                     truncated_description = ' '.join(product_description.split()[:50]) + '...'
#                     expander.write(truncated_description)
#                     expander.markdown("Nhấn vào mũi tên để đóng hộp text này.")  

def display_recommended_products(recommended_products, img_path):
    # Hiển thị đề xuất ra từng dòng
    icon = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
    for i in range(0, len(recommended_products)):
        product = recommended_products.iloc[i]
        ten_sp = '{} - {}'.format(icon[i], product['ten_san_pham'])
        st.write(ten_sp)
        st.image(img_path)
        with st.expander('Xem thêm Mô tả'):
            product_description = product['mo_ta']
            truncated_description = ' '.join(product_description.split()[:100]) + '...'
            st.write('\n{}'.format(truncated_description))
    space(5)
    footer_markdown = f"<h6 style='text-align: center; color: blue;'>**©️ DEMO RECOMENDATION **</h6>"
    st.markdown(footer_markdown, unsafe_allow_html=True)    

def recomended_for_userid(userid, df=RECOMENDED_USERID):

    recommended_user = df[df['ma_khach_hang']==userid]
    recommended_user = recommended_user.merge(products, how='left', on=['ma_san_pham', 'ten_san_pham', 'diem_trung_binh'])
    recommended_user.drop(columns='phan_loai', inplace=True)
    return recommended_user

def main():
  with st.sidebar:
    st.sidebar.image(add_logo(logo_path='img/hasaki_logo.png', width=1400, height=569)) 
    st.sidebar.info('Choose a page!')
    
    # Make sure session state is preserved
    userID = st.sidebar.selectbox(
                            'Chọn tài khoản login 👇',
                            options=USERID_OPTIONS
                            )
    if userID:
        st.sidebar.text(f'🆔: {userID}')  
    hbar()
    st.sidebar.write("""##### 🏅 Thực hiện bởi:
                    Lê Thị Vân Anh & Nguyễn Vũ Khương""")
    st.sidebar.write("""##### 👩‍🏫 Giảng viên: Cô Khuất Thùy Phương""")
    st.sidebar.write("""##### 📅 Ngày báo cáo: 15/12/2024""")  
      
  st.write('### LỰA CHỌN MÔ HÌNH ĐỀ XUẤT')
  # Tạo hai tab tương ứng với hai loại recomended
  tab1, tab2 = st.tabs(['🏷️ BY PRODUCT', '👨‍👨‍👧‍👧 BY USER'])
  with tab1:  
    st.subheader('Content-based filtering')
    for selected_item in st.session_state:
        st.session_state[selected_item] = st.session_state[selected_item]      
        
    selected_product = st.selectbox(
        'Lựa chọn sản phẩm 👇',
        options=ITEMS_OPTIONS,
        key='selected_item',)
    
    if selected_product:
        selected_product = products[products['ten_san_pham'] == selected_product]
        ITEM_CODE = selected_product['ma_san_pham'].values[0]
        
        if not selected_product.empty:
            st.write('#### Bạn vừa chọn:')
            st.write('### ', selected_product['ten_san_pham'].values[0])

            product_description = selected_product['mo_ta'].values[0]
            truncated_description = ' '.join(product_description.split()[:100])
            st.write('##### Thông tin:')
            st.write(truncated_description, '...')

            st.write('### Các sản phẩm liên quan:')
            recommended_products = get_recommendations(ITEM_CODE)
            display_recommended_products(recommended_products, img_path='img/product_of_you.png')
        
        else:    
            st.write(f'Không tìm thấy sản phẩm với ID: {ITEM_CODE}')
  
  with tab2:
    st.subheader('Collaborative Filtering')
    st.write(f'#### Đề xuất cho ID: {userID}')
    st.write(f'#### Các sản phẩm liên quan:')    
    recommended_users = recomended_for_userid(userID)
    display_recommended_products(recommended_users, img_path='img/product_of_you_2.png')

if __name__ == "__main__":
    main()