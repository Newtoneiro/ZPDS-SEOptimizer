import streamlit as st
from streamlit_tags import st_tags
from src.utils import generate_article


def render_page():
    st.title("Pomóż mi napisać artykuł")

    keywords = st_tags(
        label="Dodaj słowa kluczowe",
        text="Wciśnij enter, żeby dodać",
    )

    topic = st.text_input(
        label="Podaj temat artykułu",
    )

    tone = st.selectbox(
        label="Wybierz ton artykułu",
        options=("formalny", "nieformalny", "humorystyczny", "informacyjny", "emocjonalny"),
    )

    length = st.slider(
        label="Wybierz długość artykułu (liczbę słów)",
        min_value=50,
        max_value=500,
        value=250,
    )

    button = st.button("Generuj", use_container_width=True)

    if button:
        if not keywords:
            st.error("Proszę dodać słowa kluczowe.")
        elif not topic:
            st.error("Proszę podać temat artykułu.")
        elif not tone:
            st.error("Proszę wybrać ton artykułu.")
        elif not length:
            st.error("Proszę wybrać długość artykułu.")
        else:
            with st.spinner("Trwają obliczenia..."):
                article_text = generate_article(
                    title=topic,
                    keywords=keywords,
                    tone=tone,
                    length=length
                )
            show_article(article_text, keywords)


def show_article(article_text: str, keywords: list):
    article_text = article_text.replace("<s>", "")

    for keyword in keywords:
        article_text = article_text.replace(keyword, f"**{keyword}**")

    with st.container(border=True):
        st.markdown(article_text, unsafe_allow_html=True)
