import time

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_tags import st_tags

from utils import CONTAINER_CSS_STYLE


def generate_article_page():
    st.title("Pomóż mi napisać artykuł")

    keywords = st_tags(
        label="Dodaj słowa kluczowe",
        text="Wciśnij enter, żeby dodać kolejne słowo kluczowe",
    )

    topic = st.text_input(
        label="Podaj temat artykułu",
    )

    tone = st.selectbox(
        label="Wybierz ton artykułu",
        placeholder="Wybierz ton artykułu z listy",
        options=("formalny", "nieformalny", "humorystyczny", "informacyjny", "emocjonalny"),
        index=None,
    )

    length = st.slider(
        label="Wybierz długość artykułu (liczbę słów)",
        min_value=50,
        max_value=500,
        value=250,
    )

    if keywords and topic and tone and length and st.button("Generuj", use_container_width=True):
        with st.spinner("Trwają obliczenia..."):
            time.sleep(3)  # as now we do not wait for model output
            article_text = get_article(keywords, topic, tone, length)
        show_article(article_text)


def get_article(keywords: list[str], topic: str, tone: str, length: int) -> str:
    article_text = "article text will be here"
    return article_text


def show_article(article_text: str):
    with stylable_container(
        key="container_with_border",
        css_styles=CONTAINER_CSS_STYLE,
    ):
        st.markdown(article_text)
