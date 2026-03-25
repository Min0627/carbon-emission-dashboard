import streamlit as st
import plotly.express as px
from preprocessing import load_data, prepare_monthly_data
from style import apply_theme, hero, explain, format_plotly_chart, chips

st.set_page_config(page_title="Countries", page_icon="🌎", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "🌎 Countries",
    "Compare countries over time and identify the biggest contributors to carbon emissions."
)

country_options = sorted(monthly["country"].unique())
selected_countries = st.multiselect(
    "Choose one or more countries",
    country_options,
    default=country_options[:3]
)

if not selected_countries:
    st.warning("Please choose at least one country.")
    st.stop()

filtered = monthly[monthly["country"].isin(selected_countries)].copy()
trend = filtered.groupby(["date", "country"], as_index=False)["emission"].sum()
totals = monthly.groupby("country", as_index=False)["emission"].sum().sort_values("emission", ascending=False)

chips([
    f"Selected countries: {len(selected_countries)}",
    f"Top emitter overall: {totals.iloc[0]['country']}",
    f"2nd highest: {totals.iloc[1]['country']}"
])

left, right = st.columns([1.2, 1])

with left:
    st.markdown("### Country trend over time")
    fig = px.line(trend, x="date", y="emission", color="country", markers=True)
    fig.update_layout(hovermode="x unified")
    fig = format_plotly_chart(fig, x_title="Month", y_title="Emission", show_legend=True, legend_title="Country")
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Total emission by country")
    fig2 = px.bar(totals, x="country", y="emission")
    fig2.update_traces(
        marker_color="#2563EB",
        hovertemplate="<b>Country:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )
    fig2 = format_plotly_chart(fig2, x_title="Country", y_title="Emission", show_legend=False)
    st.plotly_chart(fig2, use_container_width=True)

selected_totals = (
    filtered.groupby("country", as_index=False)["emission"]
    .sum()
    .sort_values("emission", ascending=False)
)

leader = selected_totals.iloc[0]["country"]
leader_val = selected_totals.iloc[0]["emission"]

explain(
    f"<b>Auto insight:</b> Among the selected countries, <b>{leader}</b> contributes the most with total emissions of <b>{leader_val:,.0f}</b>. "
    f"This page helps compare whether countries follow stable, rising, or volatile emission patterns over time."
)