import os
import streamlit as st
import ollama


STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')


def get_svg_path(name):
    theme = st.get_option("theme.base")
    svg_path = os.path.join(STATIC_PATH, f"{name}_{theme}.svg")
    if os.path.exists(svg_path):
        return svg_path
    return None


class ArticleSpecification:
    def __init__(self, title, keywords, length, tone):
        self.title = title
        self.keywords = keywords
        self.length = length
        self.tone = tone

    def generate_prompt(self):
        prompt = (
            "I want you to answer in the role of a very talender copywriter that specializes in article generation."
            "I want you to output ONLY the contents of the article, no comments, no disclaimers - pure text."
            "Generate a high-quality SEO article with the following specifications:\n\n"
            f"Title: {self.title}\n"
            f"Primary Keywords: {', '.join(self.keywords)}\n"
            f"Target Word Count: {self.length}\n"
            f"Tone of Voice: {self.tone}\n\n"
            "Please ensure the article is well-structured, engaging, and includes relevant subheadings."
            "Use keywords naturally and provide valuable insights to readers."
            "Please translate the output to polish."
        )
        return " ".join(prompt)


def generate_article(title, keywords, tone, length):
    prompt = ArticleSpecification(
        title=title,
        keywords=keywords,
        tone=tone,
        length=length
    ).generate_prompt()

    response = ollama.chat(
        model="mwiewior/bielik",
        messages=[
            {"role": "system", "content": "Jesteś ekspertem w tworzeniu treści SEO."},
            {"role": "user", "content": prompt}
        ]
    )

    article_content = response.message.content
    return article_content
