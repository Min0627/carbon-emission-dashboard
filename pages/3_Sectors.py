import streamlit as st
import plotly.express as px
from preprocessing import load_data, prepare_monthly_data
from style import apply_theme, hero, explain, format_plotly_chart, chips

st.set_page_config(page_title="Sectors", page_icon="🏭", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "🏭 Sectors",
    "Understand which sectors contribute the most and how a selected sector changes over time."
)

sector_options = sorted(monthly["sector"].unique())
selected_sector = st.selectbox(
    "Choose one sector",
    sector_options,
    help="Select a sector to explore its contribution and time trend."
)

sector_summary = monthly.groupby("sector", as_index=False)["emission"].sum().sort_values("emission", ascending=False)
sector_data = monthly[monthly["sector"] == selected_sector]
sector_trend = sector_data.groupby("date", as_index=False)["emission"].sum()

chips([
    f"Top sector: {sector_summary.iloc[0]['sector']}",
    f"Selected sector: {selected_sector}"
])

left, right = st.columns([1, 1])

with left:
    st.markdown("### Share by sector")
    fig = px.pie(
        sector_summary,
        names="sector",
        values="emission",
        hole=0.52,
        color_discrete_sequence=["#2563EB", "#0EA5A4", "#F59E0B", "#8B5CF6", "#14B8A6", "#F97316"]
    )
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>Sector:</b> %{label}<br><b>Emission:</b> %{value:,.0f}<extra></extra>"
    )
    fig.update_layout(
        template="plotly_white",
        height=430,
        paper_bgcolor="white",
        font=dict(color="#0F172A"),
        legend=dict(
            bgcolor="rgba(255,255,255,0.95)",
            bordercolor="#D9E2EC",
            borderwidth=1
        )
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Trend for selected sector")
    fig2 = px.line(sector_trend, x="date", y="emission", markers=True)
    fig2.update_traces(
        line=dict(color="#0EA5A4", width=3),
        marker=dict(size=6, color="#0F172A"),
        hovertemplate="<b>Month:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )
    fig2 = format_plotly_chart(fig2, x_title="Month", y_title="Emission", show_legend=False)
    st.plotly_chart(fig2, use_container_width=True)

top_sector = sector_summary.iloc[0]["sector"]
top_val = sector_summary.iloc[0]["emission"]

explain(
    f"<b>Auto insight:</b> The largest source of emissions is <b>{top_sector}</b> with total emissions of <b>{top_val:,.0f}</b>. "
    f"The selected sector, <b>{selected_sector}</b>, can be tracked over time to see whether it is stabilising or becoming more volatile."
)