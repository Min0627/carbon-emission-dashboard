import streamlit as st
from style import apply_theme, hero, explain, chips

st.set_page_config(
    page_title="Carbon Emission Dashboard",
    page_icon="🌍",
    layout="wide"
)

apply_theme()

hero(
    "🌍 Carbon Emission Intelligence Dashboard",
    "Track historical emissions, compare countries and sectors, explore future forecasts, and understand what reduction actions could change."
)

chips([
    "Global emissions",
    "Country comparison",
    "Sector analysis",
    "Forecasting",
    "Scenario analysis",
    "World map storytelling"
])

left, right = st.columns([1.5, 1])

with left:
    st.markdown("### What are carbon emissions?")
    st.write(
        "Carbon emissions are greenhouse gases released into the atmosphere, mainly from burning fossil fuels, transportation, electricity generation, and industrial activities. "
        "Higher emissions are linked to climate change, rising temperatures, and environmental risk."
    )

    st.markdown("### Why this dashboard matters")
    st.write(
        "This dashboard turns raw carbon emission data into clear business-style insights. "
        "It helps identify which countries and sectors contribute the most, how emissions change over time, and what future outcomes may look like under different scenarios."
    )

    st.markdown("### What you can learn")
    st.write(
        "You can use the pages on the left to move from the big picture into detail: start with overview metrics, compare countries, drill into sectors, view forecasts, test reduction scenarios, and explore emissions geographically on the world map."
    )

with right:
    explain("""
    <b>Dashboard flow</b><br><br>
    <b>Overview</b> → headline metrics and trend<br>
    <b>Countries</b> → compare top emitters and selected countries<br>
    <b>Sectors</b> → see which activities drive emissions<br>
    <b>Forecast</b> → estimate what may happen next<br>
    <b>Scenarios</b> → test reduction assumptions<br>
    <b>World Map</b> → tell the geographic story
    """)

explain("""
<b>Portfolio value</b><br>
This project demonstrates data cleaning, time-series aggregation, interactive dashboard design, forecasting, scenario modelling, and executive-style data storytelling.
""")