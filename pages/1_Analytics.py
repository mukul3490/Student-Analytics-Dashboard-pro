import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

# uploaded_file = st.sidebar.file_uploader(
#     "📁 Upload CSV File",
#     type=["csv"]
# )

# if uploaded_file is not None:

#     data = pd.read_csv(uploaded_file)

# else:

#     data = pd.read_csv("students.csv")
if "data" in st.session_state:
    data = st.session_state["data"]
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

with st.spinner("🚀 Loading Dashboard..."):

    import time

    time.sleep(1)

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📊 Analytics Dashboard")

st.markdown("---")

# ==========================================
# METRICS SECTION
# ==========================================

st.subheader("📌 Dashboard Metrics")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "👨‍🎓 Total Students",
        len(filtered_data)
    )

with col2:

    st.metric(
        "📚 Average Math",
        round(filtered_data["Math"].mean(), 2)
    )

with col3:

    st.metric(
        "📈 Highest Attendance",
        filtered_data["Attendance"].max()
    )

# ==========================================
# PERFORMANCE INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("📈 Performance Insights")

average_percentage = round(
    filtered_data["Percentage"].mean(),
    2
)

if average_percentage >= 85:

    st.success(
        f"✅ Excellent Performance: "
        f"{average_percentage}%"
    )

elif average_percentage >= 65:

    st.warning(
        f"⚠️ Average Performance: "
        f"{average_percentage}%"
    )

else:

    st.error(
        f"❌ Needs Improvement: "
        f"{average_percentage}%"
    )

# ==========================================
# TOPPER SECTION
# ==========================================

st.markdown("---")

st.subheader("🏆 Topper Details")

topper = filtered_data.loc[
    filtered_data["Total"].idxmax()
]

st.success(
    f"{topper['Name']} is the topper with "
    f"{topper['Total']} marks."
)

# ==========================================
# RANKING SECTION
# ==========================================

st.markdown("---")

st.subheader("🏅 Top Ranked Students")

top_rankers = filtered_data.sort_values(

    by="Rank"

).head(5)

st.dataframe(

    top_rankers[

        [
            "Name",
            "Total",
            "Percentage",
            "Grade",
            "Rank"
        ]
    ]
)

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.markdown("---")

st.subheader("📥 Download Student Report")

csv = filtered_data.to_csv(index=False)

st.download_button(
    label="📄 Download CSV Report",
    data=csv,
    file_name="student_report.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "🚀 Built with Streamlit and Pandas"
)