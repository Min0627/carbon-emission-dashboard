import streamlit as st
import plotly.graph_objects as go
from preprocessing import load_data, prepare_monthly_data
from forecasting import forecast_emission
from style import apply_theme, hero, explain, format_plotly_chart, chips

st.set_page_config(page_title="Forecast", page_icon="🔮", layout="wide")
apply_theme()

df = load_data()
monthly = prepare_monthly_data(df)

hero(
    "🔮 Forecast",
    "Estimate future emissions based on historical patterns."
)

country_list = ["All"] + sorted(monthly["country"].unique())
sector_list = ["All"] + sorted(monthly["sector"].unique())

c1, c2, c3 = st.columns(3)
selected_country = c1.selectbox("Choose country", country_list)
selected_sector = c2.selectbox("Choose sector", sector_list)
periods = c3.slider("Future months", 3, 24, 12)

filtered = monthly.copy()
if selected_country != "All":
    filtered = filtered[filtered["country"] == selected_country]
if selected_sector != "All":
    filtered = filtered[filtered["sector"] == selected_sector]

forecast_input = filtered.groupby("date", as_index=False)["emission"].sum()

if len(forecast_input) < 6:
    st.error("Not enough data to forecast. Choose a broader selection.")
    st.stop()

forecast, _ = forecast_emission(forecast_input, periods=periods)

chips([
    f"Forecast horizon: {periods} months",
    f"Country filter: {selected_country}",
    f"Sector filter: {selected_sector}"
])

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=forecast_input["date"],
    y=forecast_input["emission"],
    mode="lines+markers",
    name="Past",
    line=dict(color="#2563EB", width=3),
    marker=dict(size=6),
    hovertemplate="<b>Month:</b> %{x}<br><b>Past emission:</b> %{y:,.0f}<extra></extra>"
))
fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat"],
    mode="lines+markers",
    name="Forecast",
    line=dict(color="#0EA5A4", width=3, dash="dash"),
    marker=dict(size=6),
    hovertemplate="<b>Month:</b> %{x}<br><b>Forecast emission:</b> %{y:,.0f}<extra></extra>"
))
fig = format_plotly_chart(fig, x_title="Month", y_title="Emission", show_legend=True, legend_title="Series")
fig.update_layout(hovermode="x unified", height=480)
st.plotly_chart(fig, use_container_width=True)

first_forecast = forecast["yhat"].iloc[0]
last_forecast = forecast["yhat"].iloc[-1]
trend_word = "increase" if last_forecast > first_forecast else "decrease"
delta_pct = ((last_forecast - first_forecast) / first_forecast * 100) if first_forecast != 0 else 0

explain(
    f"<b>Auto insight:</b> The model suggests emissions may <b>{trend_word}</b> over the next <b>{periods} months</b>. "
    f"Estimated change across the forecast horizon is about <b>{delta_pct:+.1f}%</b>."
)