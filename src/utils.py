import os
import streamlit as st
import ollama
import pandas as pd
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta


STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")
KEYS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "keys")


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
        title=title, keywords=keywords, tone=tone, length=length
    ).generate_prompt()

    response = ollama.chat(
        model="mwiewior/bielik",
        messages=[
            {"role": "system", "content": "Jesteś ekspertem w tworzeniu treści SEO."},
            {"role": "user", "content": prompt},
        ],
    )

    article_content = response.message.content
    return article_content


def get_website_views_over_time(site_url):
    # Calculate date range (30 days back)
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

    # Authenticate
    credentials_file = os.path.join(KEYS_PATH, "credentials.json")
    credentials = Credentials.from_service_account_file(
        credentials_file, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
    )
    service = build("searchconsole", "v1", credentials=credentials)

    # Query for search analytics
    try:
        # Prepare the API request
        request = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["date"],
            "rowLimit": 10000,
        }
        # Execute the API request
        response = (
            service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        )

    except HttpError as e:
        error_message = f"Google Search Console API error: {e}"
        return pd.DataFrame(), error_message

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        return pd.DataFrame(), error_message

    # Process the response
    if "rows" not in response:
        return pd.DataFrame(), "No data available for the given date range."

    data = []
    for row in response["rows"]:
        data.append({"date": row["keys"][0], "views": row["clicks"]})

    df = pd.DataFrame(data)
    return df, "Success"
