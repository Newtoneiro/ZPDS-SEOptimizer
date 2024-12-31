import time

import streamlit as st
from st_circular_progress import CircularProgress
from streamlit_extras.stylable_container import stylable_container

from utils import CONTAINER_CSS_STYLE, DARK_PURPLE, LIGHT_PURPLE


def generate_insights_page():
    st.markdown("## Jak mogę zwiększyć widoczność mojej strony?")
    uploaded_files = st.file_uploader(
        "Dodaj zrzuty ekranu swojej strony",
        type=["jpeg", "jpg", "png"],
        accept_multiple_files=True,
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            image_data = uploaded_file.getvalue()
            st.image(image_data)
        if st.button("Analizuj", use_container_width=True):
            with st.spinner("Trwają obliczenia..."):
                time.sleep(3)  # as now we do not wait for model output
                site_score, well_done_insights, improve_suggestions = get_insights(
                    uploaded_files
                )
            show_insights(site_score, well_done_insights, improve_suggestions)


def get_insights(
    uploaded_images: list,
) -> tuple[int, list[str], list[str]]:  # typing for UploadedFile not available
    site_score = 76
    well_done_insights = ["item 1", "item 2"]
    improve_suggestions = ["item 1", "item 2"]
    return site_score, well_done_insights, improve_suggestions


def show_insights(
    site_score: int, well_done_insights: list[str], improve_suggestions: list[str]
):
    _show_site_score(site_score)

    col1, col2 = st.columns(2)
    with col1:
        _show_insights_column("Co jest dobrze?", well_done_insights)
    with col2:
        _show_insights_column("Co mogę poprawić?", improve_suggestions)


def _show_site_score(site_score: int):
    style = "<style>h4 {text-align: center;}</style>"
    st.markdown(style, unsafe_allow_html=True)
    st.markdown("#### Całościowa ocena strony")

    my_circular_progress = CircularProgress(
        label="",
        size="large",
        value=site_score,
        track_color=LIGHT_PURPLE,
        color=DARK_PURPLE,
        key="my_circular_progress",
    )

    my_circular_progress.st_circular_progress()


def _show_insights_column(column_title: str, insights: list[str]):
    st.markdown(f"#### {column_title}")
    stylable_container(
        key="container_with_border", css_styles=CONTAINER_CSS_STYLE
    ).markdown("- " + "\n- ".join(insights))
