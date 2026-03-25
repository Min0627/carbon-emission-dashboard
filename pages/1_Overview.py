import streamlit as st
import plotly.express as px
from preprocessing import load_data, prepare_monthly_data
from style import apply_theme, hero, kpi, explain, format_plotly_chart, chips

st.set_page_config(page_title="Overview", page_icon="📊", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "📊 Overview",
    "Start with the overall carbon emission picture before drilling into country, sector, and future trends."
)

trend = monthly.groupby("date", as_index=False)["emission"].sum()
sector_summary = monthly.groupby("sector", as_index=False)["emission"].sum().sort_values("emission", ascending=False)
country_summary = monthly.groupby("country", as_index=False)["emission"].sum().sort_values("emission", ascending=False)

total_emission = monthly["emission"].sum()
countries = monthly["country"].nunique()
sectors = monthly["sector"].nunique()
latest_month = monthly["date"].max()
latest_value = monthly.loc[monthly["date"] == latest_month, "emission"].sum()

prev_month = trend.iloc[-2]["emission"] if len(trend) > 1 else latest_value
change_pct = ((latest_value - prev_month) / prev_month * 100) if prev_month != 0 else 0

c1, c2, c3, c4 = st.columns(4)
kpi(c1, "Total Emission", f"{total_emission:,.0f}")
kpi(c2, "Countries", f"{countries}")
kpi(c3, "Sectors", f"{sectors}")
kpi(c4, "Latest Month", f"{latest_value:,.0f}")

chips([
    f"Latest change: {change_pct:+.1f}%",
    f"Top country: {country_summary.iloc[0]['country']}",
    f"Top sector: {sector_summary.iloc[0]['sector']}"
])

st.markdown("### Overall emission trend")
fig = px.line(trend, x="date", y="emission", markers=True)
fig.update_traces(
    line=dict(color="#2563EB", width=3),
    marker=dict(size=6, color="#0EA5A4"),
    hovertemplate="<b>Month:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
)
fig = format_plotly_chart(fig, x_title="Month", y_title="Emission", show_legend=False)
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:
    st.markdown("### Sector contribution")
    fig2 = px.bar(sector_summary, x="sector", y="emission", text_auto=".2s")
    fig2.update_traces(
        marker_color="#0EA5A4",
        hovertemplate="<b>Sector:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )
    fig2 = format_plotly_chart(fig2, x_title="Sector", y_title="Emission", show_legend=False)
    st.plotly_chart(fig2, use_container_width=True)

with right:
    st.markdown("### Top countries")
    fig3 = px.bar(country_summary.head(10), x="country", y="emission", text_auto=".2s")
    fig3.update_traces(
        marker_color="#F59E0B",
        hovertemplate="<b>Country:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )
    fig3 = format_plotly_chart(fig3, x_title="Country", y_title="Emission", show_legend=False)
    st.plotly_chart(fig3, use_container_width=True)

top_country = country_summary.iloc[0]["country"]
top_sector = sector_summary.iloc[0]["sector"]

direction = "increased" if change_pct > 0 else "decreased"

explain(
    f"<b>Auto insight:</b> Overall emissions {direction} by <b>{abs(change_pct):.1f}% compared with the previous month</b>. "
    f"The highest-emitting country is <b>{top_country}</b>, while the largest contributing sector is <b>{top_sector}</b>."
)