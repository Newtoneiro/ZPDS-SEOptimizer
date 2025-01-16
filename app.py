import streamlit as st
from streamlit_navigation_bar import st_navbar

import pages as pg
from utils import BEIGE, st_normal

# set layout to wide to be able to have full screen size image on home page
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

# set navigation bar
page_names = ["Start", "Widoczność strony", "Generowanie artykułu", "Mój profil"]
styles = {
    "div": {"max-width": "700px"},
    "nav": {"background-color": BEIGE},
}
options = {"show_sidebar": False}
page = st_navbar(page_names, styles=styles, options=options)

if page == "Start":
    pg.home_page()
elif page == "Widoczność strony":
    with st_normal():
        pg.progress_tracker()
elif page == "Generowanie artykułu":
    with st_normal():
        pg.generate_article_page()
