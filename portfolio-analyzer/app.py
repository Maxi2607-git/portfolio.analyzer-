# app.py (Launcher für modulare Streamlit-App)
import streamlit as st
from components.upload_csv import show_upload
from components.overview import show_overview
from components.performance import show_performance

# === Globale Session State Defaults ===
if "portfolio_file" not in st.session_state:
    st.session_state["portfolio_file"] = None

if "portfolio_df" not in st.session_state:
    st.session_state["portfolio_df"] = None

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# === Seiteneinstellungen ===
st.set_page_config(page_title="Portfolio Analyzer", layout="wide")

# === Sidebar Navigation ===
from components.sidebar import show_sidebar
menu_option = show_sidebar()

# === Theme-Umschaltung mit CSS ===
if st.session_state.theme == "Dark":
    st.markdown("""
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        [data-testid="stSidebar"] {
            background-color: #171A21;
            color: #FAFAFA;
        }
        * {
            color: #FAFAFA !important;
        }
        </style>
    """, unsafe_allow_html=True)

# === Routing ===
if menu_option == "📁 Upload CSV":
    show_upload()
elif menu_option == "📈 Portfolio Overview":
    show_overview()
elif menu_option == "📉 Performance & Risk Analytics":
    show_performance()
