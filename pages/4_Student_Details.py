import streamlit as st
import pandas as pd
from fpdf import FPDF

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Student Details",
    page_icon="🎓",
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
# PDF GENERATOR
# ==========================================

def generate_pdf(student):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(
        200,
        10,
        txt="Student Performance Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    for column in student.columns:

        value = student[column].values[0]

        pdf.cell(
            200,
            10,
            txt=f"{column}: {value}",
            ln=True
        )

    pdf.output("student_report.pdf")

# ==========================================
# CREATE GRADE COLUMN
# ==========================================

data["Grade"] = data["Percentage"].apply(assign_grade)

# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.title("📌 Student Filters")

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

st.title("🎓 Student Details Dashboard")

st.markdown("---")

# ==========================================
# STUDENT SEARCH
# ==========================================

st.markdown("## 🔍 Student Search")

student_name = st.text_input(
    "Enter Student Name",
    placeholder="Type a student name..."
)

student_data = filtered_data[
    filtered_data["Name"]
    .str.lower()
    .str.contains(student_name.lower())
]

# ==========================================
# DISPLAY STUDENT DATA
# ==========================================

if not student_data.empty:

    st.subheader("📋 Student Record")

    student_data["Grade"] = student_data["Grade"].replace({
        "A": "🟢 A",
        "B": "🔵 B",
        "C": "🟡 C",
        "D": "🔴 D"
    })

    st.dataframe(
        student_data,
        use_container_width=True
    )
    # ==========================================
    # PROGRESS BARS
    # ==========================================

    math_marks = int(student_data["Math"].fillna(0).values[0])

    science_marks = int(student_data["Science"].fillna(0).values[0])

    english_marks = int(student_data["English"].fillna(0).values[0])

    attendance = int(student_data["Attendance"].fillna(0).values[0])

    percentage = int(student_data["Percentage"].fillna(0).values[0])

    st.markdown("---")

    st.subheader("📚 Subject Performance")

    st.write("Math")

    st.progress(math_marks)

    st.write("Science")

    st.progress(science_marks)

    st.write("English")

    st.progress(english_marks)

    st.write("Attendance")

    st.progress(attendance)

    st.write("Overall Percentage")

    st.progress(percentage)

    # ==========================================
    # EXPANDABLE REPORT
    # ==========================================

    st.markdown("---")

    with st.expander("📄 View Full Student Report"):

        st.write(student_data)

        st.write("📊 Detailed Performance Analysis")

        st.write(
            f"Average Marks: "
            f"{round(student_data['Percentage'].values[0], 2)}%"
        )

        st.write(
            f"Grade: "
            f"{student_data['Grade'].values[0]}"
        )

        st.write(
            f"Attendance: "
            f"{student_data['Attendance'].values[0]}%"
        )

    # ==========================================
    # PDF GENERATOR
    # ==========================================

    def generate_pdf(student):

     pdf = FPDF()

     pdf.add_page()

     pdf.set_font("Arial", size=14)

     pdf.cell(
        200,
        10,
        txt="Student Performance Report",
        ln=True,
        align="C"
    )

     pdf.ln(10)

     for column in student.columns:

        value = student[column].values[0]

        pdf.cell(
            200,
            10,
            txt=f"{column}: {value}",
            ln=True
        )

     pdf.output("student_report.pdf")    

else:

    st.warning("⚠️ No student found.")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "🚀 Built with Streamlit and Pandas"
)




