import plotly.express as px
import streamlit as st
from src.utils import get_website_views_over_time


def render_page():
    st.title("Jak zmienia się widoczność mojej strony?")

    site_url = st.text_input("URL strony", placeholder="https://example.com/")

    if site_url:
        df, message = get_website_views_over_time(site_url)

        if df.empty:
            st.info(f"No data to display. Reason: {message}")
        else:
            # Plot the data
            fig = px.line(
                df,
                x="date",
                y="views",
                labels={
                    "date": "Czas [dni]",
                    "views": "Liczba wyświetleń strony [kliknięcia]",
                },
                title="Liczba wyświetleń strony w ciągu ostatnich 30 dni",
            )
            st.plotly_chart(fig, use_container_width=True)
