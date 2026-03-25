import streamlit as st
from style import apply_theme, hero, explain, chips

apply_theme()

hero(
    "🌍 Carbon Emission Intelligence",
    "Explore global emission trends, compare countries and sectors, and understand future scenarios."
)

chips([
    "Global emissions",
    "Country comparison",
    "Sector analysis",
    "Forecasting",
    "Scenario analysis",
    "World map storytelling"
])

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

explain("""
<b>Portfolio value</b><br><br>
• Data cleaning and preprocessing<br>
• Time-series aggregation and analysis<br>
• Interactive dashboard development<br>
• Forecasting and scenario modelling<br>
• Clear, executive-style data storytelling
""")