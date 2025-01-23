import plotly.express as px
import streamlit as st


def render_page():
    st.title("Jak zmienia się widoczność mojej strony?")
    x, y = get_progress_data()
    fig = px.line(
        x=x, y=y, labels={"x": "czas [tyg.]", "y": "liczba wyświetleń strony [tys.]"}
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        theme=None,
    )


def get_progress_data() -> tuple[list]:
    x = list(range(100))
    return x, [i * 2 for i in x]
