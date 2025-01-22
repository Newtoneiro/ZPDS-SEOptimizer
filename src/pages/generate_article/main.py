import streamlit as st
import ollama
from streamlit_extras.stylable_container import stylable_container
from streamlit_tags import st_tags


class Article_Specification:
    def __init__(self, title, keywords, length, tone):
        self.title = title
        self.keywords = keywords
        self.length = length
        self.tone = tone

    def generate_prompt(self):
        prompt = (
            f"I want you to answer in the role of a very talender copywriter that specializes in article generation."
            f"I want you to output ONLY the contents of the article, no comments, no disclaimers - pure text."
            f"Generate a high-quality SEO article with the following specifications:\n\n"
            f"Title: {self.title}\n"
            f"Primary Keywords: {', '.join(self.keywords)}\n"
            f"Target Word Count: {self.length}\n"
            f"Tone of Voice: {self.tone}\n\n"
            f"Please ensure the article is well-structured, engaging, and includes relevant subheadings. Use keywords naturally and provide valuable insights to readers."
            f"Please translate the output to polish."
        )
        return " ".join(prompt)


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
                article_text = generate_article(
                    Article_Specification(title=topic, keywords=keywords, tone=tone, length=length)
                )
            show_article(article_text)


def generate_article(article_specifications: Article_Specification):
    content = article_specifications.generate_prompt()
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "assistant", "content": content}
        ]
    )
    return response.message.content


def show_article(article_text: str):
    with stylable_container(
        key="container_with_border",
    ):
        st.write(article_text)
