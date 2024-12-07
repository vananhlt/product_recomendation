import streamlit as st
from PIL import Image
from utils.gui import space, hbar

emoji = '🌀'
st.set_page_config(page_title='Hasaki Recomendation App', page_icon=emoji, layout='centered')

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


st.title('Welcome to the Hasaki Recomendation app!')
st.markdown(
    """
This app provides insights on a demo recomendation for account usage.

### Get started!

👈 Select a page in the sidebar!
    """
)
hbar()
space(1)  
st.markdown(
"""
### Đây là Đồ Án Tốt Nghiệp Data Science \n
"""
)
sig_markdown = f"<h3 style='text-align: left; color: blue;'>Trung Tâm Tin Học - Trường Đại Học Khoa Học Tự Nhiên</h3>"
st.markdown(sig_markdown, unsafe_allow_html=True)

st.markdown(
"""
Khóa: DL07_299T27_ON \n

"""
)
st.image(add_logo(logo_path='img/tree_edu.png', width=175, height=240))

# userID selector
with st.sidebar:
    st.sidebar.image(add_logo(logo_path='img/hasaki_logo.png', width=1400, height=569)) 
    st.sidebar.info('Choose a page! 👆')
    hbar()
    st.sidebar.write("""##### 🏅 Thực hiện bởi:
                    Lê Thị Vân Anh & Nguyễn Vũ Khương""")
    st.sidebar.write("""##### 👩‍🏫 Giảng viên: Cô Khuất Thùy Phương""")
    st.sidebar.write("""##### 📅 Ngày báo cáo: 15/12/2024""")    

    
if __name__ == '__main__':
    import sys
    from streamlit import runtime
    from streamlit.web import cli as stcli
    if runtime.exists():
        pass
    
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())