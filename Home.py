import streamlit as st
from PIL import Image
from utils.gui import hbar

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
st.image(image='img/recomender.png')

# userID selector
with st.sidebar:
    st.sidebar.image(add_logo(logo_path='img/hasaki_logo.png', width=1400, height=569)) 
    st.sidebar.info('Choose a page! 👆')
    hbar()
    st.sidebar.write("""#### Thực hiện bởi:
                    Lê Thị Vân Anh & Nguyễn Vũ Khương""")
    st.sidebar.write("""#### Giảng viên: Khuất Thùy Phương""")
    st.sidebar.write("""#### Ngày báo cáo: 16/12/2024""")    

    
if __name__ == '__main__':
    import sys
    from streamlit import runtime
    from streamlit.web import cli as stcli
    if runtime.exists():
        pass
    
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())