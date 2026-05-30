import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Charts",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

# uploaded_file = st.sidebar.file_uploader(
#     "📂 Upload CSV File",
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
# HANDLE MISSING VALUES
# ==========================================

data = data.fillna(0)

# ==========================================
# TOTAL & PERCENTAGE
# ==========================================

data["Total"] = (

    data["Math"] +
    data["Science"] +
    data["English"]
)

data["Percentage"] = data["Total"] / 3
filtered_data = data.copy()

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📈 Charts & Visual Analytics")

st.markdown(
    "Explore student performance through advanced charts visual analytics"
)

st.markdown("---")

# ==========================================
# BAR CHART
# ==========================================

st.subheader("📊 Student Total Marks")

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(

    x="Name",

    y="Total",

    data=data,

    palette="viridis",

    ax=ax
)

plt.xticks(rotation=15)

st.pyplot(fig)

# ==========================================
# PIE CHART
# ==========================================

st.subheader("🥧 Gender Distribution")

gender_counts = data["Gender"].value_counts()

fig, ax = plt.subplots(figsize=(5, 5))

ax.pie(

    gender_counts,

    labels=gender_counts.index,

    autopct="%1.1f%%",

    startangle=90
)

ax.axis("equal")

st.pyplot(fig)

# ==========================================
# LINE CHART
# ==========================================

st.subheader("📉 Attendance Trend")

fig, ax = plt.subplots(figsize=(10, 5))

sns.lineplot(

    x="Name",

    y="Attendance",

    data=data,

    marker="o",

    linewidth=3,

    ax=ax
)

plt.xticks(rotation=15)

st.pyplot(fig)

# ==========================================
# HEATMAP
# ==========================================

st.subheader("🔥 Subject Correlation Heatmap")

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(

    data[
        [
            "Math",
            "Science",
            "English",
            "Attendance",
            "Percentage"
        ]
    ].corr(),

    annot=True,

    cmap="coolwarm",

    linewidths=1,

    ax=ax
)

st.pyplot(fig)

# ==========================================
# DISTRIBUTION PLOT
# ==========================================

st.subheader("📚 Percentage Distribution")

fig, ax = plt.subplots(figsize=(9, 5))

sns.histplot(

    data["Percentage"],

    kde=True,

    bins=10,

    ax=ax
)

st.pyplot(fig)

# ==========================================
# BOXPLOT
# ==========================================

st.subheader("📦 Subject Comparison Boxplot")

fig, ax = plt.subplots(figsize=(9, 5))

sns.boxplot(

    data=data[
        [
            "Math",
            "Science",
            "English"
        ]
    ],

    ax=ax
)

st.pyplot(fig)

# ==========================================
# CO-RELATION HEATMAP
# ==========================================

st.markdown("---")

st.subheader("🔥 Subject Correlation Heatmap")

correlation = filtered_data[
    ["Math", "Science", "English", "Attendance", "Percentage"]
].corr()

fig, ax = plt.subplots(figsize=(8, 5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=1,
    ax=ax
)

st.pyplot(fig)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "🚀 Built with Streamlit, Matplotlib & Seaborn"
)