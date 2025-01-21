import streamlit as st
import time
from streamlit_extras.stylable_container import stylable_container
from streamlit_tags import st_tags
from src.styles import ARTICLE_STYLES


def render_page():
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
                time.sleep(2)
                article_text = get_article(keywords, topic, tone, length)
            show_article(article_text)


def get_article(keywords: list[str], topic: str, tone: str, length: int) -> str:
    # random paragraph
    lorem_ipsum = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Integer nec odio. Praesent libero. Sed cursus
    ante dapibus diam.Sed nisi. Nulla quis sem at nibh
    elementum imperdiet. Duis sagittis ipsum.
    Praesent mauris. Fusce nec tellus sed augue
    semper porta. Mauris massa.
    Vestibulum lacinia arcu eget nulla.
    """

    # Insert keywords in the text as bold
    for keyword in keywords:
        lorem_ipsum = lorem_ipsum.replace("Lorem", f"**{keyword}**", 1)

    article = f"""
    # {topic}

    ### **Tytuł artykułu:** {topic}
    ### **Ton artykułu:** {tone}
    ### **Słowa kluczowe:** {', '.join(keywords)}
    ### **Długość artykułu:** {length} słów

    {lorem_ipsum * (length // 50)}
    """

    return article


def show_article(article_text: str):
    with stylable_container(
        key="container_with_border",
        css_styles=ARTICLE_STYLES,
    ):
        st.markdown(article_text)
