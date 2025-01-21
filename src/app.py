import streamlit as st
from streamlit_option_menu import option_menu
from src.pages import PAGES
from src.styles import NAVBAR_STYLES


st.set_page_config(page_title="SEOptimizer", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navbar menu
selected = option_menu(
    menu_title=None,
    options=[page for page in PAGES.keys()],
    icons=[page[0] for page in PAGES.values()],
    menu_icon="list",
    default_index=0,
    orientation="horizontal",
    styles=NAVBAR_STYLES,
)

PAGES[selected][1]()
