import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""

<style>

.stApp {

    background: linear-gradient(
        to bottom right,
        #0E1117,
        #111827
    );

    color: white;
}

.login-box {

    background-color: rgba(255,255,255,0.05);

    padding: 40px;

    border-radius: 20px;

    box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
}

</style>

""", unsafe_allow_html=True)

# ==========================================
# LOGIN UI
# ==========================================

st.title("🔐 Student Dashboard Login")

st.markdown("---")

username = st.text_input("👤 Username")

password = st.text_input(
    "🔑 Password",
    type="password"
)

# ==========================================
# LOGIN BUTTON
# ==========================================

if st.button("🚀 Login"):

    if username == "admin" and password == "admin123":

        st.success("✅ Login Successful!")

        st.info(
            "👉 Now open app.py "
            "to access dashboard."
        )

    else:

        st.error("❌ Invalid Username or Password")