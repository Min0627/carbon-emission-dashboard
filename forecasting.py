import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def forecast_emission(df, periods=12):
    ts = df.sort_values("date").copy()

    model = ARIMA(ts["emission"], order=(1, 1, 1))
    fitted = model.fit()

    forecast = fitted.forecast(steps=periods)

    future_dates = pd.date_range(
        start=ts["date"].iloc[-1],
        periods=periods + 1,
        freq="MS"
    )[1:]

    out = pd.DataFrame({
        "ds": future_dates,
        "yhat": forecast
    })

    return out, fitted