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
        prompt = [
            "Chcę, abyś odpowiedział w roli bardzo utalentowanego copywritera, który specjalizuje się w tworzeniu artykułów."
            "Chcę, abyś generował WYŁĄCZNIE treść artykułu - bez komentarzy, bez TAGÓW, bez tytułów sekcji, podsumowań, bez uwag - NICZEGO."
            "Masz zwrócić czysty tekst."
            "Wygeneruj wysokiej jakości artykuł SEO zgodnie z poniższymi wytycznymi:\n\n"
            f"Tytuł: {self.title}\n"
            f"Podstawowe słowa kluczowe: {', '.join(self.keywords)}\n"
            f"Docelowa liczba słów: {self.length}\n"
            f"Ton wypowiedzi: {self.tone}\n\n"
            "Upewnij się, że artykuł jest dobrze zorganizowany, angażujący i zawiera odpowiednie śródtytuły."
            "Używaj słów kluczowych w naturalny sposób i dostarczaj czytelnikom wartościowych informacji."
        ]
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
