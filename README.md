## 🌍 Carbon Emission Dashboard

An interactive data analytics dashboard built with **Python + Streamlit** to explore global carbon emission trends, compare countries and sectors, and forecast future emissions.

---

## 📊 Project Overview

This project provides a complete end-to-end data analytics workflow:

* 📥 Data preprocessing and cleaning
* 📈 Interactive visualizations
* 🌍 Geographic emission mapping
* 🔮 Time-series forecasting
* 🧠 Insight generation for decision-making

The goal is to transform raw emission data into **clear, actionable insights** that help understand environmental impact.

---

## ✨ Key Features

### 1. Overview Dashboard

* High-level emission trends
* Key KPIs and summaries
* Easy-to-understand insights

### 2. Country Analysis

* Compare emissions across countries
* Identify top emitters
* Track trends over time

### 3. Sector Analysis

* Breakdown of emissions by sector
* Identify largest contributors (e.g. power, transport)
* Sector-level trend analysis

### 4. Forecasting

* Time-series prediction using Prophet
* Future emission trend visualization
* Helps simulate future scenarios

### 5. Scenario Simulation

* Adjust reduction assumptions
* See potential impact on emissions
* Supports decision-making

### 6. World Map Visualization

* Geographic distribution of emissions
* Identify emission hotspots
* Compare countries visually

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (dashboard & UI)
* **Pandas** (data processing)
* **Plotly** (interactive charts)
* **Prophet** (forecasting)

---

## 📁 Project Structure

```
carbon-emission-dashboard/
│
├── app.py
├── preprocessing.py
├── forecasting.py
├── style.py
│
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Countries.py
│   ├── 3_Sectors.py
│   ├── 4_Forecast.py
│   ├── 5_Scenarios.py
│   └── 6_World_Map.py
│
└── data/
    └── dataset.csv
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pandas plotly streamlit prophet
```

### 2. Run the app

```bash
python -m streamlit run app.py
```

---

## 📌 Key Insights (Example)

* Power sector is the largest contributor to emissions
* A small number of countries dominate global emissions
* Some countries show increasing emission trends over time
* Forecasting indicates continued growth without intervention

---

## 💡 Why This Project Matters

Carbon emissions are a major driver of climate change.
This project demonstrates how data analytics can:

* Simplify complex environmental data
* Support policy and decision-making
* Highlight high-impact areas for emission reduction

---

## 📸 Screenshots (Add later)

*Add your dashboard screenshots here to showcase UI*

---

## 👨‍💻 Author

Built as a data analytics portfolio project to demonstrate:

* Data cleaning & transformation
* Dashboard development
* Data storytelling
* Forecasting & modeling

---

## ⭐ Future Improvements

* Add real-time data integration
* Improve forecasting accuracy
* Deploy dashboard online (Streamlit Cloud)
* Add user authentication

---
