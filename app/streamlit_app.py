# =========================================================
# ResumeIQ AI — FINAL FIXED ENTERPRISE DASHBOARD
# =========================================================

import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SAMPLE DATA
# =========================================================

df = pd.DataFrame({

    "Candidate": [
        "Rahul",
        "Ananya",
        "Kiran",
        "Priya",
        "Vikram",
        "Aisha",
        "Rohit",
        "Sneha"
    ],

    "ATS Score": [
        96,
        91,
        86,
        81,
        74,
        68,
        61,
        54
    ],

    "Matched Skills": [
        9,
        8,
        8,
        7,
        6,
        5,
        4,
        3
    ],

    "Status": [
        "Shortlisted",
        "Shortlisted",
        "Shortlisted",
        "Shortlisted",
        "Shortlisted",
        "Rejected",
        "Rejected",
        "Rejected"
    ]
})


# =========================================================
# ENTERPRISE CSS
# =========================================================

st.markdown("""

<style>

/* =====================================================
GLOBAL SETTINGS
===================================================== */

html, body, [class*="css"] {

    font-family:
    "Inter",
    sans-serif !important;

    font-size: 24px !important;
}

/* =====================================================
REMOVE STREAMLIT DEFAULTS
===================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =====================================================
APP BACKGROUND
===================================================== */

.stApp {

    zoom: 1.12;

    background:
    linear-gradient(
        135deg,
        #020617 0%,
        #0F172A 45%,
        #111827 100%
    );
}

/* =====================================================
PAGE WIDTH
===================================================== */

.main .block-container {

    max-width: 99% !important;

    padding-top: 1rem !important;

    padding-left: 1.5rem !important;

    padding-right: 1.5rem !important;

    padding-bottom: 1rem !important;
}

/* =====================================================
SIDEBAR
===================================================== */

[data-testid="stSidebar"] {

    min-width: 420px !important;

    max-width: 420px !important;

    background:
    linear-gradient(
        180deg,
        rgba(15,23,42,0.98),
        rgba(2,6,23,0.98)
    );

    border-right:
    1px solid rgba(255,255,255,0.08);

    padding-top: 1rem;
}

[data-testid="stSidebar"] * {

    color: white !important;

    font-size: 26px !important;
}

/* =====================================================
HERO SECTION
===================================================== */

.hero {

    padding: 4rem;

    border-radius: 36px;

    background:
    linear-gradient(
        135deg,
        rgba(59,130,246,0.20),
        rgba(139,92,246,0.20),
        rgba(236,72,153,0.15)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    margin-bottom: 1.5rem;

    box-shadow:
    0 25px 80px rgba(0,0,0,0.35);
}

.hero-title {

    font-size: 6rem;

    font-weight: 900;

    color: white;

    margin-bottom: 0.8rem;
}

.hero-sub {

    font-size: 2rem;

    color: #CBD5E1;

    line-height: 1.9;
}

/* =====================================================
SECTION TITLES
===================================================== */

.section-title {

    font-size: 3rem;

    font-weight: 900;

    color: white;

    margin-top: 0.3rem;

    margin-bottom: 1rem;
}

/* =====================================================
KPI CARDS
===================================================== */

.metric-card {

    padding: 2rem;

    border-radius: 32px;

    min-height: 260px;

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,0.96),
        rgba(30,41,59,0.90)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 20px 60px rgba(0,0,0,0.30);

    transition: 0.3s ease;
}

.metric-card:hover {

    transform:
    translateY(-6px);

    box-shadow:
    0 25px 70px rgba(59,130,246,0.28);
}

.metric-icon {

    font-size: 3rem;

    margin-bottom: 0.7rem;
}

.metric-label {

    color: #CBD5E1;

    font-size: 1.8rem;

    margin-bottom: 0.5rem;
}

.metric-value {

    font-size: 5rem;

    font-weight: 900;

    color: white;
}

/* =====================================================
CHART CARDS
===================================================== */

.chart-card {

    padding: 1rem;

    border-radius: 28px;

    background:
    rgba(15,23,42,0.85);

    border:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 20px 60px rgba(0,0,0,0.30);

    margin-bottom: 1rem;
}

/* =====================================================
TABLE
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 24px;

    overflow: hidden;

    border:
    1px solid rgba(255,255,255,0.08);
}

thead tr th {

    background:
    #111827 !important;

    color: white !important;

    font-size: 34px !important;

    font-weight: 900 !important;

    padding: 24px !important;
}

tbody tr td {

    background:
    rgba(15,23,42,0.96) !important;

    color: #E2E8F0 !important;

    font-size: 32px !important;

    padding: 22px !important;
}

/* =====================================================
INSIGHT CARDS
===================================================== */

.insight-card {

    padding: 2rem;

    border-radius: 28px;

    min-height: 260px;

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,0.96),
        rgba(30,41,59,0.90)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 20px 60px rgba(0,0,0,0.30);
}

.insight-title {

    font-size: 2rem;

    font-weight: 900;

    color: white;

    margin-bottom: 1rem;
}

.insight-text {

    color: #CBD5E1;

    font-size: 24px;

    line-height: 1.9;
}

</style>

""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""

<div class="hero">

<div class="hero-title">
📄 ResumeIQ AI
</div>

<div class="hero-sub">

Enterprise-grade AI recruitment intelligence platform for
ATS screening, candidate ranking,
AI hiring analytics,
and recruiter workflow automation.

</div>

</div>

""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Recruiter Control Panel")

minimum_score = st.sidebar.slider(
    "Minimum ATS Score",
    0,
    100,
    40
)

required_skill = st.sidebar.selectbox(
    "Required Skill",
    [
        "All",
        "Python",
        "Machine Learning",
        "SQL",
        "Streamlit",
        "NLP",
        "Docker"
    ]
)


# =========================================================
# KPI SECTION
# =========================================================

st.markdown(
    """
    <div class="section-title">
    📊 Recruitment Intelligence Overview
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# KPI CARD STYLE
# =========================================================

st.markdown("""

<style>

.kpi-box {

    background:
    linear-gradient(
        135deg,
        rgba(15,23,42,0.96),
        rgba(30,41,59,0.90)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 35px;

    min-height: 230px;

    box-shadow:
    0 20px 60px rgba(0,0,0,0.30);

    transition: 0.3s ease;
}

.kpi-box:hover {

    transform: translateY(-6px);

    box-shadow:
    0 25px 70px rgba(59,130,246,0.28);
}

.kpi-icon {

    font-size: 42px;

    margin-bottom: 10px;
}

.kpi-title {

    color: #CBD5E1;

    font-size: 30px;

    font-weight: 700;

    margin-bottom: 10px;
}

.kpi-value {

    color: white;

    font-size: 64px;

    font-weight: 900;
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# KPI ROW 1
# =========================================================

k1, k2, k3 = st.columns(3)

with k1:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">👨‍💼</div>
        <div class="kpi-title">Candidates</div>
        <div class="kpi-value">248</div>
    </div>
    """, unsafe_allow_html=True)

with k2:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">✅</div>
        <div class="kpi-title">Shortlisted</div>
        <div class="kpi-value">84</div>
    </div>
    """, unsafe_allow_html=True)

with k3:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">❌</div>
        <div class="kpi-title">Rejected</div>
        <div class="kpi-value">164</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# KPI ROW 2
# =========================================================

k4, k5, k6 = st.columns(3)

with k4:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">📈</div>
        <div class="kpi-title">Avg Score</div>
        <div class="kpi-value">78%</div>
    </div>
    """, unsafe_allow_html=True)

with k5:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">🏆</div>
        <div class="kpi-title">Top Score</div>
        <div class="kpi-value">97%</div>
    </div>
    """, unsafe_allow_html=True)

with k6:

    st.markdown("""
    <div class="kpi-box">
        <div class="kpi-icon">🧠</div>
        <div class="kpi-title">Skill Match</div>
        <div class="kpi-value">89%</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# CHART TITLE
# =========================================================

st.markdown(
    '<div class="section-title">📈 Candidate Intelligence Analytics</div>',
    unsafe_allow_html=True
)


# =========================================================
# CHARTS
# =========================================================

chart1, chart2 = st.columns([1.4, 1])


# =========================================================
# BAR CHART
# =========================================================

with chart1:

    fig = px.bar(
        df,
        x="Candidate",
        y="ATS Score",
        color="Status",
        text="ATS Score",
        color_discrete_map={
            "Shortlisted": "#3B82F6",
            "Rejected": "#EF4444"
        }
    )

    fig.update_traces(
        textfont_size=30,
        marker_line_width=2
    )

    fig.update_layout(

        template="plotly_dark",

        height=780,

        font=dict(size=30),

        title="ATS Candidate Ranking",

        title_font_size=36,

        xaxis=dict(
            tickfont=dict(size=28),
            title_font=dict(size=28)
        ),

        yaxis=dict(
            tickfont=dict(size=28),
            title_font=dict(size=28)
        ),

        legend=dict(
            font=dict(size=28)
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# PIE CHART
# =========================================================

with chart2:

    pie = px.pie(
        df,
        names="Status",
        hole=0.50,
        color="Status",
        color_discrete_map={
            "Shortlisted": "#3B82F6",
            "Rejected": "#EF4444"
        }
    )

    pie.update_traces(
        textfont_size=32
    )

    pie.update_layout(

        template="plotly_dark",

        height=780,

        font=dict(size=30),

        title="Hiring Decision Distribution",

        title_font_size=36,

        legend=dict(
            font=dict(size=28)
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )


# =========================================================
# TABLE TITLE
# =========================================================

st.markdown(
    '<div class="section-title">📋 Candidate Intelligence Panel</div>',
    unsafe_allow_html=True
)


# =========================================================
# TABLE
# =========================================================

st.dataframe(
    df,
    use_container_width=True,
    height=760
)
# =========================================================
# AI RECRUITMENT INSIGHTS
# =========================================================

st.markdown("""
<h1 style="
color:white;
font-size:52px;
font-weight:900;
margin-top:40px;
margin-bottom:30px;
">
🧠 AI Recruitment Insights
</h1>
""", unsafe_allow_html=True)

# =========================================================
# INSIGHT COLUMN LAYOUT
# =========================================================

c1, c2, c3 = st.columns(3)

# =========================================================
# CARD 1
# =========================================================

with c1:

    st.info("""
🎯 TOP CANDIDATE INSIGHT

Candidates with Python, NLP, and SQL skills demonstrated significantly stronger ATS scores and higher recruiter shortlist probability.
""")

# =========================================================
# CARD 2
# =========================================================

with c2:

    st.info("""
📈 RECRUITMENT TREND

Machine Learning, Streamlit, Data Analytics, and AI Engineering are dominating enterprise hiring workflows and recruiter demand.
""")

# =========================================================
# CARD 3
# =========================================================

with c3:

    st.info("""
⚡ ATS OPTIMIZATION

Resume keyword optimization and technical skill alignment strongly improved AI-based candidate ranking performance.
""")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""

<br><br><br>

<center>

<h2 style="
    color:#E2E8F0;
    font-size:38px;
    font-weight:900;
">
ResumeIQ AI — Enterprise Recruitment Intelligence
</h2>

<p style="
    color:#94A3B8;
    font-size:24px;
">
Built using Python, NLP, Streamlit & Machine Learning
</p>

</center>

""", unsafe_allow_html=True)