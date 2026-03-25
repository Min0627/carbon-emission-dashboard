import streamlit as st
import pandas as pd
import plotly.express as px
from preprocessing import load_data, prepare_monthly_data
from style import apply_theme, hero, explain, format_plotly_chart, format_map, kpi, chips, top_list

st.set_page_config(page_title="World Map", page_icon="🗺️", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "🗺️ World Map Storytelling",
    "Identify geographic concentration, leading emitters, and country-level patterns over time."
)

sector_options = ["All"] + sorted(monthly["sector"].unique().tolist())
month_df = pd.DataFrame({"date": sorted(monthly["date"].dropna().unique())})
month_df["label"] = month_df["date"].dt.strftime("%b %Y")
country_options = sorted(monthly["country"].unique().tolist())

f1, f2, f3 = st.columns(3)
selected_sector = f1.selectbox("Choose sector", sector_options)
selected_label = f2.selectbox("Choose month", month_df["label"], index=len(month_df) - 1)
selected_country = f3.selectbox("Choose one country for detail", country_options)

selected_month = month_df.loc[month_df["label"] == selected_label, "date"].iloc[0]

filtered = monthly.copy()
filtered = filtered[~filtered["country"].isin(["World", "Rest of World"])]

if selected_sector != "All":
    filtered = filtered[filtered["sector"] == selected_sector]

static_data = filtered[filtered["date"] == selected_month].copy()
map_data = static_data.groupby("country", as_index=False)["emission"].sum().sort_values("emission", ascending=False)

if map_data.empty:
    st.warning("No data available for this selection.")
    st.stop()

total_map_emission = map_data["emission"].sum()
country_count = map_data["country"].nunique()
top_country = map_data.iloc[0]["country"]
top_value = map_data.iloc[0]["emission"]
avg_emission = map_data["emission"].mean()
share_pct = (top_value / total_map_emission * 100) if total_map_emission else 0

k1, k2, k3, k4 = st.columns(4)
kpi(k1, "Total Emission in View", f"{total_map_emission:,.0f}")
kpi(k2, "Countries Shown", f"{country_count}")
kpi(k3, "Top Country", top_country)
kpi(k4, "Average per Country", f"{avg_emission:,.0f}")

chips([
    f"Month: {selected_label}",
    f"Sector: {selected_sector}",
    f"Top emitter share: {share_pct:.1f}%"
])

st.markdown("### Geographic distribution")

col_map, col_side = st.columns([2, 1])

with col_map:
    fig_map = px.choropleth(
        map_data,
        locations="country",
        locationmode="country names",
        color="emission",
        hover_name="country",
        hover_data={"emission": ":,.0f"},
        color_continuous_scale=["#DBEAFE", "#93C5FD", "#60A5FA", "#3B82F6", "#1D4ED8"],
        title=""
    )
    fig_map.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Emission: %{z:,.0f}<extra></extra>"
    )
    fig_map = format_map(fig_map)
    st.plotly_chart(fig_map, use_container_width=True)

with col_side:
    st.markdown("### Top emitters")
    top5 = map_data.head(5)
    top_items = [
        (row["country"], f"Emission: {row['emission']:,.0f}")
        for _, row in top5.iterrows()
    ]
    top_list(top_items)

st.markdown("### Comparison and detail")

left, right = st.columns([1, 1])

with left:
    st.markdown("### Top 10 countries in selected view")
    fig_bar = px.bar(
        map_data.head(10).sort_values("emission", ascending=True),
        x="emission",
        y="country",
        orientation="h",
        text="emission"
    )
    fig_bar.update_traces(
        marker_color="#2563EB",
        texttemplate="%{text:,.0f}",
        textposition="outside",
        hovertemplate="<b>Country:</b> %{y}<br><b>Emission:</b> %{x:,.0f}<extra></extra>"
    )
    fig_bar = format_plotly_chart(fig_bar, x_title="Emission", y_title="Country", show_legend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with right:
    st.markdown("### Selected country trend")
    country_data = filtered[filtered["country"] == selected_country].copy()
    country_trend = country_data.groupby("date", as_index=False)["emission"].sum()

    fig_country = px.line(country_trend, x="date", y="emission", markers=True)
    fig_country.update_traces(
        line=dict(color="#0EA5A4", width=3),
        marker=dict(size=6, color="#0F172A"),
        hovertemplate="<b>Month:</b> %{x}<br><b>Emission:</b> %{y:,.0f}<extra></extra>"
    )
    fig_country = format_plotly_chart(fig_country, x_title="Month", y_title="Emission", show_legend=False)
    st.plotly_chart(fig_country, use_container_width=True)

latest_country_value = country_trend.iloc[-1]["emission"] if not country_trend.empty else 0
trend_direction = "increasing" if len(country_trend) > 1 and country_trend.iloc[-1]["emission"] > country_trend.iloc[0]["emission"] else "stable or decreasing"

explain(
    f"""
    <b>Key insight:</b><br><br>
    • In <b>{selected_label}</b>, <b>{top_country}</b> is the leading emitter with <b>{top_value:,.0f}</b><br>
    • That accounts for about <b>{share_pct:.1f}% of all emissions shown on the map</b><br>
    • For <b>{selected_country}</b>, the latest visible emission is <b>{latest_country_value:,.0f}</b><br>
    • The selected country shows a <b>{trend_direction}</b> pattern over time<br><br>
    👉 This helps highlight where targeted emission reduction could have the greatest impact.
    """
)

csv = map_data.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download selected map data",
    data=csv,
    file_name="world_map_selected_view.csv",
    mime="text/csv"
)