import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Student Analytics Dashboard Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS STYLING
# ==========================================

st.markdown("""

<style>
      header[data-testid="stHeader"] {
    background: none;
}

div.block-container {
    padding-top: 1rem;
}
[data-testid="collapsedControl"] {
    color: white !important;
    background-color: rgba(255,255,255,0.1) !important;
    border-radius: 6px;
}

[data-testid="collapsedControl"] svg {
    fill: white !important;
    color: white !important;
}
            [data-testid="collapsedControl"] {
    color: white !important;
}

[data-testid="collapsedControl"] svg {
    fill: white !important;
}



/* =========================================
MAIN BACKGROUND
========================================= */

.stApp {

    background: linear-gradient(
        to bottom right,
        #0E1117,
        #111827
    );

    color: white;
}

/* =========================================
HEADINGS
========================================= */

h1 {

    color: white;

    font-size: 48px;

    font-weight: 800;

    letter-spacing: -1px;

    margin-bottom: 10px;
}

h2 {

    color: #F3F4F6;

    font-size: 36px;

    font-weight: 700;

    margin-bottom: 8px;
}

h3 {

    color: #E5E7EB;

    font-size: 28px;

    font-weight: 600;

    margin-bottom: 6px;
}

h4 {

    color: #D1D5DB;

    font-size: 22px;

    font-weight: 600;
}

/* =========================================
SIDEBAR
========================================= */

section[data-testid="stSidebar"] {

    background-color: #111827;

    border-right: 1px solid #333;
}

            /* =========================================
SIDEBAR TEXT
========================================= */

section[data-testid="stSidebar"] * {

    color: white !important;

    font-family: 'Segoe UI', sans-serif;
}

/* =========================================
SIDEBAR TITLE
========================================= */

section[data-testid="stSidebar"] h1 {

    font-size: 28px;

    font-weight: bold;

    color: #FF4B4B;
}

/* =========================================
SIDEBAR BUTTONS & INPUTS
========================================= */

section[data-testid="stSidebar"] .stButton>button {

    background: linear-gradient(
        to right,
        #FF4B4B,
        #FF6B6B
    );

    border-radius: 10px;
}

/* =========================================
SIDEBAR SLIDER
========================================= */

section[data-testid="stSidebar"] .stSlider {

    padding-top: 10px;
}
            
/* =========================================
FILE UPLOADER
========================================= */

[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.03) !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    border-radius: 15px;

    padding: 15px;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;

    border: none !important;
}

[data-testid="stFileUploader"] button {
    background: linear-gradient(
        135deg,
        #FF4B4B,
        #FF6B6B
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding: 10px 20px !important;

    font-size: 16px !important;

    font-weight: 600 !important;

    width: 100% !important;
}
            [data-testid="stFileUploader"] button div {
    display: none !important;
}
            [data-testid="stFileUploader"] button::after {
    content: "Upload CSV";
    color: white;
    font-size: 16px;
    font-weight: 600;
}

/* =========================================
SELECTBOX
========================================= */

.stSelectbox div[data-baseweb="select"] {

    background-color: #1E1E1E !important;

    color: white !important;

    border-radius: 10px;

    border: 1px solid #444 !important;
}

.stSelectbox svg {

    fill: white !important;
}

div[data-baseweb="popover"] {

    background-color: #1E1E1E !important;

    color: white !important;
}

div[role="listbox"] {

    background-color: #1E1E1E !important;

    color: white !important;

    border: 1px solid #444 !important;
}

div[role="option"] {

    background-color: #1E1E1E !important;

    color: white !important;
}

div[role="option"]:hover {

    background-color: #FF4B4B !important;

    color: white !important;
}
            .stSelectbox div[data-baseweb="select"] > div {
    background-color: #1E1E1E !important;
    color: white !important;
}

.stSelectbox input {
    color: white !important;
}

.stSelectbox [data-baseweb="select"] {
    background-color: #1E1E1E !important;
}
                 
/* =========================================
METRIC CARDS
========================================= */

[data-testid="stMetric"] {

    background: linear-gradient(
        145deg,
        #2C3E50,
        #4CA1AF
    );

    border: 1px solid rgba(255,255,255,0.08);

    padding: 22px;

    border-radius: 20px;

    text-align: center;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.6);

    transition: all 0.3s ease-in-out;

    backdrop-filter: blur(6px);
}

/* =========================================
METRIC HOVER EFFECT
========================================= */

[data-testid="stMetric"]:hover {

    transform: translateY(-6px);

    border: 1px solid #FF4B4B;

    box-shadow:
        0px 0px 15px rgba(255,75,75,0.25),
        0px 0px 30px rgba(255,75,75,0.10);
}

/* =========================================
GLASS CONTAINERS
========================================= */

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;

}

/* =========================================
BUTTONS
========================================= */

.stButton>button {

    background: linear-gradient(
        to right,
        #FF4B4B,
        #FF6B6B
    );

    color: white;

    border: none;

    border-radius: 12px;

    height: 50px;

    width: 100%;

    font-size: 16px;

    font-weight: bold;

    transition: 0.3s;
}

.stButton>button:hover {

    transform: scale(1.02);

    box-shadow: 0px 0px 15px rgba(255,75,75,0.5);
}

/* =========================================
DATAFRAMES
========================================= */

[data-testid="stDataFrame"] {

    border-radius: 15px;

    overflow: hidden;

    border: 1px solid #333;
}

/* =========================================
EXPANDERS
========================================= */

.streamlit-expanderHeader {

    background-color: #1E1E1E;

    border-radius: 10px;

    color: white;
}

/* =========================================
INPUT BOXES
========================================= */

.stTextInput>div>div>input {

    background-color: #1E1E1E;

    color: white;

    border-radius: 10px;
}

/* =========================================
SELECTBOX
========================================= */

.stSelectbox div[data-baseweb="select"] {

    background-color: #1E1E1E;

    border-radius: 10px;
}

/* =========================================
RADIO BUTTONS
========================================= */

.stRadio {

    color: white;
}

/* =========================================
SLIDER
========================================= */

.stSlider {

    color: white;
}
            
            /* =========================================
RESPONSIVE DESIGN
========================================= */

@media (max-width: 768px) {

    h1 {

        font-size: 28px !important;
    }

    h2 {

        font-size: 24px !important;
    }

    h3 {

        font-size: 20px !important;
    }

    .block-container {

        padding-left: 1rem;

        padding-right: 1rem;
    }

    [data-testid="stMetric"] {

        padding: 10px;

        border-radius: 12px;
    }

    .stButton>button {

        height: 45px;

        font-size: 14px;
    }
}

/* =========================================
FOOTER
========================================= */

footer {

    visibility: hidden;
}

</style>

""", unsafe_allow_html=True)

# ==========================================
# LOAD DATA
# ==========================================

uploaded_file = st.sidebar.file_uploader(
    "📁 Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

else:

    data = pd.read_csv("students.csv")

data = data.fillna(0)

filtered_data = data.copy()

# ==========================================
# TOTAL & PERCENTAGE
# ==========================================

data["Total"] = (
    data["Math"] +
    data["Science"] +
    data["English"]
)

data["Percentage"] = data["Total"] / 3

# ==========================================
# GRADE FUNCTION
# ==========================================

def assign_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 50:
        return "C"

    else:
        return "D"

# ==========================================
# CREATE GRADE COLUMN
# ==========================================

data["Grade"] = data["Percentage"].apply(assign_grade)

# ==========================================
# STUDENT RANKING
# ==========================================

data["Rank"] = data["Total"].rank(

    ascending=False,

    method="dense"

).fillna(0).astype(int)

# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.title("📌 Dashboard Filters")

selected_subject = st.sidebar.selectbox(

    "📚 Choose Subject",

    [ "Math", "Science", "English"]

)
subject_average = round(data[selected_subject].mean(), 2)

subject_topper = data.loc[
    data[selected_subject].idxmax(),
    "Name"
]

selected_gender = st.sidebar.multiselect(

    "👨‍🎓 Select Gender",

    options=data["Gender"].unique(),

    default=data["Gender"].unique()

)

attendance_range = st.sidebar.slider(

    "📈 Attendance Range",

    int(data["Attendance"].min()),

    int(data["Attendance"].max()),

    (
        int(data["Attendance"].min()),

        int(data["Attendance"].max())
    )
)

# ==========================================
# FILTERED DATA
# ==========================================

filtered_data = data[

    (data["Gender"].isin(selected_gender)) &

    (data["Attendance"] >= attendance_range[0]) &

    (data["Attendance"] <= attendance_range[1])

]

# ==========================================
# HOME PAGE
# ==========================================

st.title("📊 Student Analytics Dashboard Pro")

st.markdown("""
### 📌 Smart Student Performance Tracking System

Analyze student marks, attendance, rankings, and insights
through interactive visual analytics.
""")
st.markdown("---")

# ==========================================
# HERO SECTION
# ==========================================

col1, col2 = st.columns([2, 1])

with col1:

    st.subheader("🚀 Dashboard Features")

    st.write("""
    ✅ Advanced Analytics
    
    ✅ Interactive Charts
    
    ✅ Student Performance Tracking
    
    ✅ Dynamic Filtering
    
    ✅ Downloadable Reports
    
    ✅ Modern UI/UX
    
    ✅ Responsive Dashboard
    
    ✅ Multipage Architecture
    """)

with col2:

    st.metric(
        "👨‍🎓 Total Students",
        len(filtered_data)
    )

    st.metric(
        "📚 Avg Percentage",
        round(filtered_data["Percentage"].mean(), 2)
    )

# ==========================================
# QUICK OVERVIEW
# ==========================================

st.markdown("---")

st.subheader("📈 Quick Overview")

overview_col1, overview_col2, overview_col3 = st.columns(3)

with overview_col1:

    st.info(
        f"🏆 {selected_subject} Topper: "
        f"{subject_topper}"
    )

with overview_col2:

    st.success(
        f"📊 Highest Attendance: "
        f"{filtered_data['Attendance'].max()}"
    )

with overview_col3:

    st.warning(
       f"🎯 Average {selected_subject} Marks: "
       f"{subject_average}"
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    "### 🚀 Developed by Mukul Sharma"
)

st.caption(
    "Student Analytics Dashboard Pro | Streamlit + Pandas + Seaborn"
)