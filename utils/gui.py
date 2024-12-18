import streamlit as st

BLUE_COLOR = "#1c83e1"

def icon(emoji: str):
    """Hiển thị emoji icon cho page."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def space(num_lines: int = 1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


def hbar():
    """Adds a horizontal bar"""
    st.write("---")


def subsubheader(*args):
    text = " · ".join(tuple(args))
    st.write(text)

if __name__ == "__main__":
    pass
