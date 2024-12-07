import streamlit as st
import pandas as pd
from PIL import Image
from utils.gui import icon, space, hbar

# Lấy danh sách userID để đưa vào Account sidebar
products = pd.read_csv('data/San_pham.csv')
customer = pd.read_csv('data/Khach_hang.csv')
USERID_OPTIONS = customer['ma_khach_hang'].values[0:20]

emoji = '⚙️'
st.set_page_config(
    page_title='Dataset Insights', page_icon=emoji, layout='centered'
)

def product_dataframe(df=products):
    # Hiển thị danh sách sản phẩm
    df = df[['ma_san_pham', 'ten_san_pham', 'gia_ban', 'gia_goc', 'diem_trung_binh', 'mo_ta']]
    
    column_label = {'ma_san_pham': 'Mã Sản Phẩm',
                    'ten_san_pham': 'Tên sản phẩm',
                    'gia_ban': 'Giá bán',
                    'gia_goc': 'Giá gốc',
                    'mo_ta': 'Mô tả',
                    'diem_trung_binh': 'Điểm TB'
    }
    
    df.rename(columns=column_label, inplace=True)
        
    return df.head(5).sort_values(by='Điểm TB', ascending=False)

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def main():
    
    with st.sidebar:
        st.sidebar.image(add_logo(logo_path='img/hasaki_logo.png', width=1400, height=569)) 
        st.sidebar.info('Choose a page! 👆')
        hbar()
        st.sidebar.write("""##### 🏅 Thực hiện bởi:
                        Lê Thị Vân Anh & Nguyễn Vũ Khương""")
        st.sidebar.write("""##### 👩‍🏫 Giảng viên: Cô Khuất Thùy Phương""")
        st.sidebar.write("""##### 📅 Ngày báo cáo: 15/12/2024""")    
    
    # Header
    icon(emoji)
    st.subheader('Business Objective')
    st.write("""
        ###### ✨ HASAKI.VN là hệ thống cửa hàng mỹ phẩm chính hãng và dịch vụ chăm sóc sắc đẹp chuyên sâu với hệ thống cửa hàng trải dài trên toàn quốc. Khách hàng có thể lên đây để lựa chọn sản phẩm, xem các đánh giá/ nhận xét cũng như đặt mua sản phẩm.
        """)
    space(1)
    st.write("""###### 🔑 Problem/ Requirement: Giả sử HASAKI.VN chưa triển khai hệ thống Recommender System giúp đề xuất sản phẩm phù hợp tới người dùng và bạn được yêu cầu triển khai hệ thống này, bạn sẽ làm gì?""")    
    st.image('img/hasaki_1.jpg')  
    hbar()
    
    # Giới thiệu mô hình sử dụng trong project
    st.write(
    """
    ### Lựa chọn thuật toán sử dụng đề xuất?
    - Content-based filtering bằng Cosine Similarity (mô hình Gensim)
    so sánh mức độ giống nhau của hai văn bản bằng cách tính khoảng cách giữa hai vec-tơ qua phương pháp đo góc Cosine.

    - Collaborative Filtering với Similarity matrix (mô hình ALS)
    phương pháp gợi ý sản phẩm với ý tưởng chính dựa trên các hành vi của các users khác cùng trên một item để suy ra mức độ quan tâm
    của một user lên sản phẩm. Việc suy ra này được thực hiện dựa trên Similarity matrix đo độ giống nhau giữa các users.
    """
    )
    st.image(image='img/recomender.png')
    hbar()
    
    # Get data
    st.subheader('Tìm hiểu về bộ dữ liệu Hasaki')
    st.subheader('Reviews Product')
    df = product_dataframe()
    
    column_config={'Mã Sản Phẩm': st.column_config.NumberColumn(format='%d'), \
                    'Điểm TB': st.column_config.NumberColumn(format='%.1f ⭐')}
    
    st.dataframe(data=df, use_container_width=True, hide_index=True, column_config=column_config)    
    space(1)
    st.subheader('Distribution of Product',)

    left_col, right_col = st.columns(2)
    with left_col:
        st.image(image='img/mean_rating.png', caption='Rating phân bố chủ yếu ở 4-5 ⭐')
    with right_col:
        st.image(image='img/distribution.png', caption='Người dùng chủ yếu mua từ 1-2 sản phẩm')
    
    left_col, right_col = st.columns(2)
    with left_col:
        st.image(image='img/length.png', caption='Đa phần sử dụng 200-400 từ để mô tả sản phẩm')

    st.image(image='img/rating_price.png', caption='Tương quan nghịch giữa giá bán và điểm trung bình')
    st.image('img/wordcloud.png', caption='Wordcloud mô tả sản phẩm')
    hbar()

    st.subheader('Quá trình tiền xử lý trước khi đưa vào mô hình')
    st.image(image='img/pipline.png')
    space(1)
    hbar()
    
if __name__ == "__main__":
    main()
