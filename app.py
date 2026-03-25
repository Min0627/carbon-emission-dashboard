import streamlit as st
from style import apply_theme

st.set_page_config(
    page_title="Carbon Emission Dashboard",
    page_icon="🌍",
    layout="wide"
)

apply_theme()

pg = st.navigation(
    [
        st.Page("intro.py", title="Introduction", icon="📘"),
        st.Page("pages/1_Overview.py", title="Overview", icon="📊"),
        st.Page("pages/2_Countries.py", title="Countries", icon="🌎"),
        st.Page("pages/3_Sectors.py", title="Sectors", icon="🏭"),
        st.Page("pages/4_Forecast.py", title="Forecast", icon="🔮"),
        st.Page("pages/5_Scenarios.py", title="Scenarios", icon="🌱"),
        st.Page("pages/6_World_Map.py", title="World Map", icon="🗺️"),
    ],
    position="sidebar",
    expanded=True
)

pg.run()