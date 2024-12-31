import streamlit as st

DARK_PURPLE = "#8b3ad6"
LIGHT_PURPLE = "#f2e8fa"
BEIGE = "#D9D9D9"

CONTAINER_CSS_STYLE = """
    {
        border: 1px solid rgba(49, 51, 63, 0.2);
        border-radius: 0.5rem;
        padding: calc(1em - 1px);
        background-color: #f2e8fa;
    }
"""


# use to go from wide layout to standard one
def st_normal():
    _, col, _ = st.columns([1, 2, 1])
    return col
