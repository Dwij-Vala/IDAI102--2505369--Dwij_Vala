import streamlit as st
import pandas as pd
import os
from components.purchase_logger import purchase_logger
from components.co2_estimator import co2_estimator
from components.eco_suggestions import eco_suggestions
from components.dashboard import dashboard
from components.badge_display import badge_display
from components.mindful_reflection import mindful_reflection

st.set_page_config(

    page_title="ShopImpact 🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Accessibility settings panel
with st.sidebar.expander("Accessibility Settings 🦾", expanded=True):
    theme = st.radio("Theme Mode", ["Dark", "High Contrast", "Light"], index=0, help="Switch between dark, high-contrast, and light modes for best visibility.")
    font_size = st.slider("Font Size", min_value=16, max_value=32, value=22, step=2, help="Adjust text size for readability.")
    dyslexia_font = st.checkbox("Enable Dyslexia-Friendly Font", value=False, help="Use a font designed for easier reading.")



# Theme palettes
THEMES = {
    "Dark": {
        "BG": "#2d2a26", "ACCENT": "#7c6f57", "TEXT": "#e6d7b2", "CARD": "#4b4637", "HIGHLIGHT": "#b7c68b", "GRAD1": "#a3b18a", "GRAD2": "#f4a261"
    },
    "High Contrast": {
        "BG": "#000000", "ACCENT": "#FFD700", "TEXT": "#FFFFFF", "CARD": "#222222", "HIGHLIGHT": "#FFD700", "GRAD1": "#FFD700", "GRAD2": "#000000"
    },
    "Light": {
        "BG": "#f4ecd8", "ACCENT": "#a3b18a", "TEXT": "#3a5a40", "CARD": "#e9c46a", "HIGHLIGHT": "#a3b18a", "GRAD1": "#e9c46a", "GRAD2": "#a3b18a"
    }
}
PALETTE = THEMES.get(theme, THEMES["Dark"])
FONT_FAMILY = "OpenDyslexic, Arial, sans-serif" if dyslexia_font else "Trebuchet MS, Verdana, sans-serif"

st.markdown(f"""
    <style>
    .reportview-container {{ background: {PALETTE['BG']}; border-radius: 32px; }}
    .sidebar .sidebar-content {{ background: {PALETTE['ACCENT']}; border-radius: 32px; }}
    h1, h2, h3, h4, h5, h6 {{ color: {PALETTE['TEXT']}; font-family: '{FONT_FAMILY}'; font-size: {font_size+8}px; letter-spacing: 2px; text-shadow: 2px 2px 8px {PALETTE['HIGHLIGHT']}; border-radius: 32px; }}
    .stButton>button {{ font-size: {font_size+4}px; background: {PALETTE['HIGHLIGHT']}; color: {PALETTE['BG']}; border-radius: 32px; box-shadow: 0 0 12px {PALETTE['ACCENT']}; font-weight: bold; }}
    .stTextInput>div>div>input {{ font-size: {font_size}px; background: {PALETTE['CARD']}; color: {PALETTE['TEXT']}; border: 2px solid {PALETTE['HIGHLIGHT']}; border-radius: 32px; }}
    .stDataFrame, .stTable {{ background: {PALETTE['CARD']}; color: {PALETTE['TEXT']}; font-size: {font_size}px; border-radius: 32px; }}
    .stRadio>div>label {{ color: {PALETTE['HIGHLIGHT']}; font-size: {font_size}px; font-weight: bold; border-radius: 32px; }}
    .stMetric {{ color: {PALETTE['HIGHLIGHT']}; font-size: {font_size+6}px; font-weight: bold; border-radius: 32px; }}
    .stMarkdown {{ color: {PALETTE['TEXT']}; font-size: {font_size}px; border-radius: 32px; }}
    body {{ background: linear-gradient(135deg, {PALETTE['GRAD1']} 60%, {PALETTE['GRAD2']} 100%); border-radius: 32px; }}
    </style>
""", unsafe_allow_html=True)


# Motivational quotes
import random
quotes = [
    "The greatest threat to our planet is the belief that someone else will save it. – Robert Swan",
    "Small acts, when multiplied by millions of people, can transform the world. – Howard Zinn",
    "Sustainability is not a goal, but a way of living.",
    "Buy less, choose well, make it last. – Vivienne Westwood",
    "The Earth does not belong to us: we belong to the Earth. – Marlee Matlin",
    "Every time you spend money, you're casting a vote for the kind of world you want. – Anna Lappé"
]
quote = random.choice(quotes)
st.markdown(f"""
<div style='background: #1a1f1a; border-radius: 18px; padding: 30px; margin-bottom: 20px; box-shadow: 0 0 20px #3a5a40;'>
    <h1 style='color: #e9c46a; font-size: 3em; text-align: center; font-family: 'Trebuchet MS', Verdana;'>ShopImpact 🌱</h1>
    <p style='color: #f4a261; font-size: 1.5em; text-align: center;'>Welcome! Log your purchases, track your CO₂ impact, earn eco-badges 🏅, and reflect mindfully.</p>
    <blockquote style='color: #e9c46a; font-size: 1.2em; text-align: center; margin-top: 18px;'>{quote}</blockquote>
</div>
""", unsafe_allow_html=True)

## ...existing code...

# Load or initialize purchase data
data_path = os.path.join("data", "purchases.csv")
if os.path.exists(data_path):
    purchases = pd.read_csv(data_path)
else:
    purchases = pd.DataFrame(columns=["Item", "Category", "Price", "CO2_kg", "Timestamp"])

# Sidebar navigation
page = st.sidebar.radio(
    "Navigate",
    ["Log Purchase", "CO₂ Estimator", "Eco Suggestions", "Dashboard", "Badges", "Mindful Reflection"]
)

if page == "Log Purchase":
    purchase_logger(purchases, data_path)
elif page == "CO₂ Estimator":
    co2_estimator(purchases)
elif page == "Eco Suggestions":
    eco_suggestions(purchases)
elif page == "Dashboard":
    dashboard(purchases)
elif page == "Badges":
    badge_display(purchases)
elif page == "Mindful Reflection":
    mindful_reflection()
