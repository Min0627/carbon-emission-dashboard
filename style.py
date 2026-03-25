import streamlit as st

COLORS = {
    "bg": "#F5F7FB",
    "surface": "#FFFFFF",
    "surface_soft": "#F8FAFC",
    "border": "#D9E2EC",
    "text": "#0F172A",
    "muted": "#475569",
    "navy": "#0B1F3A",
    "blue": "#2563EB",
    "blue_2": "#1D4ED8",
    "teal": "#0EA5A4",
    "amber": "#F59E0B",
    "green": "#16A34A",
    "red": "#EF4444"
}

def apply_theme():
    st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: "Inter", "Segoe UI", Arial, sans-serif;
    }}

    body {{
        color: {COLORS["text"]};
    }}

    [data-testid="stAppViewContainer"] {{
        background: {COLORS["bg"]};
    }}

    .block-container {{
        max-width: 1380px;
        padding-top: 1.0rem;
        padding-bottom: 2rem;
    }}

    [data-testid="stHeader"] {{
        background: rgba(255,255,255,0);
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #07162D 0%, #0B1F3A 100%);
        border-right: 1px solid #102A43;
    }}

    [data-testid="stSidebar"] * {{
        color: #F8FAFC !important;
    }}

    /* Typography */
    h1, h2, h3, h4 {{
        color: {COLORS["text"]} !important;
        letter-spacing: -0.02em;
        font-weight: 750 !important;
    }}

    p, label, li {{
        color: {COLORS["muted"]} !important;
    }}

    span, div {{
        color: inherit;
    }}

    /* Hero */
    .hero {{
        background: linear-gradient(135deg, #1D4ED8 0%, #0EA5A4 100%);
        border-radius: 24px;
        padding: 36px 32px 30px 32px;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
        margin-bottom: 18px;
    }}

    .hero h1 {{
        color: white !important;
        margin: 0;
        font-size: 2.9rem;
        line-height: 1.05;
    }}

    .hero p {{
        color: rgba(255,255,255,0.96) !important;
        margin: 10px 0 0 0;
        font-size: 1.04rem;
    }}

    /* Cards */
    .kpi-card {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 18px;
        padding: 18px 18px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
        min-height: 116px;
    }}

    .kpi-label {{
        font-size: 0.92rem;
        font-weight: 650;
        color: {COLORS["muted"]} !important;
        margin-bottom: 10px;
    }}

    .kpi-value {{
        font-size: 2rem;
        font-weight: 800;
        color: {COLORS["text"]} !important;
        line-height: 1.1;
    }}

    .kpi-bar {{
        height: 5px;
        border-radius: 999px;
        margin-top: 14px;
        background: linear-gradient(90deg, #2563EB, #0EA5A4);
    }}

    .panel {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 18px;
        padding: 16px 18px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
    }}

    .insight-box {{
        background: #F8FAFC;
        border: 1px solid {COLORS["border"]};
        border-left: 6px solid {COLORS["blue"]};
        border-radius: 16px;
        padding: 15px 16px;
        margin-top: 12px;
        color: {COLORS["text"]} !important;
    }}

    .metric-list {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 18px;
        padding: 12px 14px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
    }}

    .metric-item {{
        padding: 10px 4px;
        border-bottom: 1px solid #EAF0F6;
    }}

    .metric-item:last-child {{
        border-bottom: none;
    }}

    .metric-title {{
        color: {COLORS["text"]} !important;
        font-weight: 700;
        font-size: 0.98rem;
    }}

    .metric-sub {{
        color: {COLORS["muted"]} !important;
        font-size: 0.9rem;
        margin-top: 2px;
    }}

    .info-chip {{
        display: inline-block;
        padding: 6px 10px;
        border-radius: 999px;
        background: #E0F2FE;
        color: #075985 !important;
        font-size: 0.84rem;
        font-weight: 700;
        margin-right: 8px;
        margin-bottom: 8px;
    }}

    /* Labels */
    .stSelectbox label, .stMultiSelect label, .stSlider label {{
        color: {COLORS["text"]} !important;
        font-weight: 650;
    }}

    /* Select visible box */
    [data-baseweb="select"] > div {{
        background: white !important;
        color: {COLORS["text"]} !important;
        border: 1px solid {COLORS["border"]} !important;
        border-radius: 12px !important;
        box-shadow: none !important;
    }}

    [data-baseweb="select"] input,
    [data-baseweb="select"] span,
    [data-baseweb="select"] div {{
        color: {COLORS["text"]} !important;
    }}

    /* Dropdown menu */
    [data-baseweb="menu"] {{
        background: white !important;
        border: 1px solid {COLORS["border"]} !important;
        border-radius: 12px !important;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.14) !important;
    }}

    [data-baseweb="menu"] ul {{
        background: white !important;
    }}

    [data-baseweb="menu"] li {{
        background: white !important;
        color: {COLORS["text"]} !important;
        font-weight: 500 !important;
    }}

    [data-baseweb="menu"] li:hover {{
        background: #EFF6FF !important;
        color: {COLORS["text"]} !important;
    }}

    /* Multiselect chips */
    .stMultiSelect [data-baseweb="tag"] {{
        background: #DBEAFE !important;
        color: #1E3A8A !important;
        border-radius: 999px !important;
        border: 1px solid #BFDBFE !important;
    }}

    .stMultiSelect [data-baseweb="tag"] span {{
        color: #1E3A8A !important;
        font-weight: 650 !important;
    }}

    /* Buttons */
    .stDownloadButton button, .stButton button {{
        background: {COLORS["blue"]} !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }}

    .stDownloadButton button:hover, .stButton button:hover {{
        background: {COLORS["blue_2"]} !important;
        color: white !important;
    }}

    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {{
        color: {COLORS["text"]} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

def hero(title: str, subtitle: str):
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def kpi(col, label: str, value: str):
    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-bar"></div>
    </div>
    """, unsafe_allow_html=True)

def explain(text: str):
    st.markdown(f"""
    <div class="insight-box">
        {text}
    </div>
    """, unsafe_allow_html=True)

def chips(items):
    html = "".join([f'<span class="info-chip">{item}</span>' for item in items])
    st.markdown(html, unsafe_allow_html=True)

def top_list(items):
    html = '<div class="metric-list">'
    for title, subtitle in items:
        html += f'''
        <div class="metric-item">
            <div class="metric-title">{title}</div>
            <div class="metric-sub">{subtitle}</div>
        </div>
        '''
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def format_plotly_chart(fig, x_title="", y_title="", show_legend=False, legend_title=""):
    fig.update_layout(
        template="plotly_white",
        height=430,
        margin=dict(l=20, r=20, t=24, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter, Segoe UI, Arial, sans-serif", color=COLORS["text"], size=13),
        xaxis=dict(
            title=x_title,
            title_font=dict(size=14, color=COLORS["text"]),
            tickfont=dict(size=12, color=COLORS["muted"]),
            showgrid=False,
            linecolor=COLORS["border"],
            tickcolor=COLORS["border"]
        ),
        yaxis=dict(
            title=y_title,
            title_font=dict(size=14, color=COLORS["text"]),
            tickfont=dict(size=12, color=COLORS["muted"]),
            gridcolor="#E8EEF5",
            linecolor=COLORS["border"],
            tickcolor=COLORS["border"],
            zeroline=False
        ),
        showlegend=show_legend,
        legend=dict(
            title=dict(text=legend_title, font=dict(color=COLORS["text"])),
            font=dict(color=COLORS["text"]),
            bgcolor="rgba(255,255,255,0.96)",
            bordercolor=COLORS["border"],
            borderwidth=1
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_color=COLORS["text"],
            bordercolor=COLORS["border"]
        )
    )
    return fig

def format_map(fig):
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(family="Inter, Segoe UI, Arial, sans-serif", color=COLORS["text"], size=13),
        margin=dict(l=10, r=10, t=20, b=10),
        coloraxis_colorbar=dict(
            title="Emission",
            title_font=dict(color=COLORS["text"]),
            tickfont=dict(color=COLORS["muted"])
        ),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#94A3B8",
            projection_type="equirectangular",
            bgcolor="white",
            showland=True,
            landcolor="#F8FAFC",
            showcountries=True,
            countrycolor="#CBD5E1"
        )
    )
    return fig