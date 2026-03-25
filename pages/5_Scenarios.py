import streamlit as st
import plotly.express as px
from preprocessing import load_data, prepare_monthly_data
from style import apply_theme, hero, explain, format_plotly_chart, chips, kpi

st.set_page_config(page_title="Sectors", page_icon="🏭", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "🏭 Sector Analysis",
    "See which sectors contribute the most and how one selected sector changes over time."
)

sector_options = sorted(monthly["sector"].unique())
selected_sector = st.selectbox("Choose one sector", sector_options)

sector_summary = (
    monthly.groupby("sector", as_index=False)["emission"]
    .sum()
    .sort_values("emission", ascending=False)
)

sector_data = monthly[monthly["sector"] == selected_sector]
sector_trend = sector_data.groupby("date", as_index=False)["emission"].sum()

top_sector = sector_summary.iloc[0]["sector"]
top_val = sector_summary.iloc[0]["emission"]

selected_total = sector_summary.loc[
    sector_summary["sector"] == selected_sector, "emission"
].iloc[0]

total_all = sector_summary["emission"].sum()
selected_share = (selected_total / total_all * 100) if total_all != 0 else 0

k1, k2, k3 = st.columns(3)
kpi(k1, "Top Sector", top_sector)
kpi(k2, "Top Sector Emission", f"{top_val:,.0f}")
kpi(k3, "Selected Sector Share", f"{selected_share:.1f}%")

chips([
    f"Top sector: {top_sector}",
    f"Selected sector: {selected_sector}",
    f"Share: {selected_share:.1f}%"
])

left, right = st.columns([1, 1])

with left:
    st.markdown("### Sector contribution ranking")

    fig = px.bar(
        sector_summary.sort_values("emission", ascending=True),
        x="emission",
        y="sector",
        orientation="h",
        text="emission"
    )

    fig.update_traces(
        marker_color="#2563EB",
        texttemplate="%{text:,.0f}",
        textposition="outside",
        hovertemplate="<b>Sector:</b> %{y}<br><b>Emission:</b> %{x:,.0f}<extra></extra>"
    )

    fig = format_plotly_chart(
        fig,
        x_title="Emission",
        y_title="Sector",
        show_legend=False
    )

    fig.update_layout(height=470)
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### Trend for selected sector")

    fig2 = px.line(
        sector_trend,
        x="date",
        y="emission",
        markers=True
    )

    fig2.update_traces(
        line=dict(color="#0EA5A4", width=3),
        marker=dict(size=6, color="#0F172A"),
        hovertemplate="<b>Month:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )

    fig2 = format_plotly_chart(
        fig2,
        x_title="Month",
        y_title="Emission",
        show_legend=False
    )

    fig2.update_layout(height=470)
    st.plotly_chart(fig2, use_container_width=True)

explain(
    f"<b>Auto insight:</b> <b>{top_sector}</b> is the largest emitting sector with total emissions of <b>{top_val:,.0f}</b>. "
    f"The selected sector, <b>{selected_sector}</b>, represents about <b>{selected_share:.1f}% of all sector emissions</b>."
)