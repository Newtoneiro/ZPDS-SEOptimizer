import streamlit as st
from src import utils


HOME_GRAPHIC = "home_graphic"


def render_page():
    st.divider()
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Zwiększ widoczność swojej strony w wyszukiwaniach Google.")

    with col2:
        st.image(
            utils.get_svg_path(HOME_GRAPHIC),
            use_container_width=True
        )

    st.divider()
