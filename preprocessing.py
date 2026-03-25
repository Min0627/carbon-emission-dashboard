import pandas as pd

def load_data():
    df = pd.read_csv("data/dataset.csv")
    df.columns = df.columns.str.lower().str.strip()

    if "date" not in df.columns:
        raise ValueError("The dataset must contain a 'date' column.")

    # Convert date safely
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["date"])

    # Rename value column if needed
    if "value" in df.columns and "emission" not in df.columns:
        df = df.rename(columns={"value": "emission"})

    # Check required columns
    required = ["country", "sector", "date", "emission"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Keep only needed columns
    df = df[required].copy()

    # Clean text
    df["country"] = df["country"].astype(str).str.strip()
    df["sector"] = df["sector"].astype(str).str.strip()

    # Convert emission to numeric
    df["emission"] = pd.to_numeric(df["emission"], errors="coerce")

    # Drop bad rows
    df = df.dropna()

    # Standardize country names for map compatibility
    country_map = {
        "USA": "United States",
        "US": "United States",
        "UK": "United Kingdom",
        "UAE": "United Arab Emirates",
        "Russia": "Russian Federation",
        "South Korea": "Korea, Republic of",
        "Vietnam": "Viet Nam",
        "WORLD": "World",
        "ROW": "Rest of World"
    }

    df["country"] = df["country"].replace(country_map)

    return df


def prepare_monthly_data(df):
    monthly = (
        df.groupby(
            ["country", "sector", pd.Grouper(key="date", freq="MS")]
        )["emission"]
        .sum()
        .reset_index()
    )
    return monthly