# Colors
BACKGROUND_COLOR = "#262730"
ICON_COLOR = "lightblue"
HOVER_COLOR = "#4c566a"
SELECTED_BACKGROUND_COLOR = "#4a90e2"
SELECTED_TEXT_COLOR = "white"

# Font sizes
ICON_FONT_SIZE = "18px"
NAV_LINK_FONT_SIZE = "16px"

# Navbar styles
NAVBAR_STYLES = {
    "container": {"background-color": BACKGROUND_COLOR},
    "icon": {
        "color": ICON_COLOR,
        "font-size": ICON_FONT_SIZE,
        "margin-right": "10px",
    },
    "nav-link": {
        "font-size": NAV_LINK_FONT_SIZE,
        "text-align": "left",
        "margin": "0",
        "--hover-color": HOVER_COLOR,
    },
    "nav-link-selected": {
        "background-color": SELECTED_BACKGROUND_COLOR,
        "color": SELECTED_TEXT_COLOR,
    },
}
