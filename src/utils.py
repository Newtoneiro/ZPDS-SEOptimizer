import os
import streamlit as st


STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')


def get_svg_path(name):
    theme = st.get_option("theme.base")
    svg_path = os.path.join(STATIC_PATH, f"{name}_{theme}.svg")
    if os.path.exists(svg_path):
        return svg_path
    return None
