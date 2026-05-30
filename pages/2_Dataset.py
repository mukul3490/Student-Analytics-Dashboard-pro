import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Dataset",
    page_icon="📁",
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
# SIDEBAR FILTERS
# ==========================================

st.sidebar.title("📌 Dataset Filters")

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

st.title("📁 Student Dataset Explorer")

st.markdown("---")

# ==========================================
# SORTING SYSTEM
# ==========================================

st.subheader("🔄 Sort Dataset")

col1, col2 = st.columns(2)

with col1:

    sort_column = st.selectbox(

        "Sort By",

        [
            "Math",
            "Science",
            "English",
            "Attendance",
            "Percentage",
            "Total"
        ]
    )

with col2:

    sort_order = st.radio(

        "Sort Order",

        [
            "Ascending",
            "Descending"
        ]
    )

sorted_data = filtered_data.sort_values(

    by=sort_column,

    ascending=(sort_order == "Ascending")
)

# ==========================================
# DATASET TABLE
# ==========================================

st.markdown("---")

st.subheader("📊 Dataset Table")

st.dataframe(
    sorted_data,
    use_container_width=True
)

# ==========================================
# DATASET SUMMARY
# ==========================================

st.markdown("---")

st.subheader("📈 Dataset Summary")

st.dataframe(
    sorted_data.describe(),
    use_container_width=True
)

# ==========================================
# QUICK INSIGHTS
# ==========================================

st.markdown("---")

st.subheader("⚡ Quick Insights")

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:

    st.info(
        f"📚 Highest Math Marks: "
        f"{sorted_data['Math'].max()}"
    )

with insight_col2:

    st.success(
        f"🎯 Average Percentage: "
        f"{round(sorted_data['Percentage'].mean(), 2)}%"
    )

with insight_col3:

    st.warning(
        f"📈 Highest Attendance: "
        f"{sorted_data['Attendance'].max()}%"
    )

# ==========================================
# DOWNLOAD SECTION
# ==========================================

st.markdown("---")

st.subheader("📥 Download Sorted Dataset")

csv = sorted_data.to_csv(index=False)

st.download_button(
    label="📄 Download Dataset",
    data=csv,
    file_name="sorted_student_dataset.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "🚀 Built with Streamlit and Pandas"
)