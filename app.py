import streamlit as st
from streamlit_option_menu import option_menu
from src.pages import PAGES


st.set_page_config(page_title="SEOptimizer", layout="centered")


# Navbar menu
selected = option_menu(
    menu_title=None,
    options=[page for page in PAGES.keys()],
    icons=[page[0] for page in PAGES.values()],
    menu_icon="list",
    default_index=0,
    orientation="horizontal",
)

PAGES[selected][1]()
