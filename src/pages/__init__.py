# flake8:noqa

from src.pages.home.main import render_page as home
from src.pages.generate_article.main import render_page as generate_article
from src.pages.analytics.main import render_page as analytics

# Icons come from https://icons.getbootstrap.com/?q=wri
PAGES = {
    "Home": ("house-fill", home),
    "Generate Article": ("pen-fill", generate_article),
    "Page Analytics": ("graph-up", analytics),
}