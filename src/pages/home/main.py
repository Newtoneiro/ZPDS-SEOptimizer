import streamlit as st
import os
from src import utils

HOME_GRAPHIC = os.path.join(utils.STATIC_PATH, "home_graphic.svg")


def render_page():
    st.divider()
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Zwiększ widoczność swojej strony w wyszukiwaniach Google.")

    with col2:
        st.image(HOME_GRAPHIC, use_container_width=True)

    st.divider()
