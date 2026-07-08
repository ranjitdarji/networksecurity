import streamlit as st
import requests
import pandas as pd
import plotly.express as px

if "prediction_df" not in st.session_state:
    st.session_state.prediction_df = None

st.set_page_config(
    page_title="Network Security Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Network Security Dashboard")
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Dashboard", "Prediction", "About"]
)

# ==========================================
# DASHBOARD PAGE
# ==========================================
if page == "Dashboard":
    st.header("📊 Dashboard")

    if st.session_state.prediction_df is not None:
        df = st.session_state.prediction_df
        total = len(df)
        safe = len(df[df["predicted_column"] == 0])
        phishing = len(df[df["predicted_column"] == 1])
    else:
        total, safe, phishing = 0, 0, 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄 Total URLs", total)
    with col2:
        st.metric("✅ Safe URLs", safe)
    with col3:
        st.metric("⚠️ Phishing URLs", phishing)

    st.markdown("---")

    if st.session_state.prediction_df is None:
        st.info("📂 Upload a CSV file from the Prediction page to start analysis.")
    else:
        st.success("✅ Prediction completed successfully.")
        st.subheader("Prediction Preview")
        st.dataframe(st.session_state.prediction_df.head(), use_container_width=True)

        st.markdown("---")
        st.subheader("📊 Prediction Analytics")

        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            pie_fig = px.pie(
                values=[safe, phishing],
                names=["Safe", "Phishing"],
                title="Website Distribution",
                hole=0.4
            )
            st.plotly_chart(pie_fig, use_container_width=True)

        with chart_col2:
            bar_fig = px.bar(
                x=["Safe", "Phishing"],
                y=[safe, phishing],
                title="Prediction Count",
                text=[safe, phishing]
            )
            bar_fig.update_traces(textposition="outside")
            st.plotly_chart(bar_fig, use_container_width=True)
            
        st.markdown("---")
        st.subheader("📌 Project Overview")
        left, right = st.columns(2)
        with left:
            st.info("""
                ### 🎯 Objective
                This project predicts whether a website is:
                - ✅ Safe Website
                - ⚠️ Phishing Website
                
                using a Machine Learning model.
                """)
        with right:
            st.success("""
                ### 🛠 Technology Stack
                - Python / Streamlit / FastAPI
                - Scikit-Learn / MLflow
                - MongoDB Atlas
                """)        

# ==========================================
# PREDICTION PAGE
# ==========================================
elif page == "Prediction":
    st.header("🔍 Website Prediction")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Dataset")
        st.dataframe(df.head(), use_container_width=True)
        st.markdown("---")

        st.subheader("📊 Dataset Information")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📄 Total Rows", df.shape[0])
            st.metric("📑 Total Columns", df.shape[1])
        with col2:
            st.metric("❌ Missing Values", int(df.isnull().sum().sum()))
            st.metric("📋 Duplicate Rows", int(df.duplicated().sum()))

        # Trigger Prediction API
        if st.button("🚀 Predict"):
            with st.spinner("Predicting..."):
                uploaded_file.seek(0)
                files = {"file": (uploaded_file.name, uploaded_file, "text/csv")}

                try:
                    response = requests.post("http://127.0.0.1:8000/predict", files=files)
                    if response.status_code == 200:
                        prediction = response.json()["prediction"]
                        st.session_state.prediction_df = pd.DataFrame(prediction)
                        st.success("Prediction Completed Successfully")
                    else:
                        st.error(f"API Error: {response.text}")
                        st.stop()
                except Exception:
                    st.error("Unable to connect with FastAPI.\n\nRun:\nuvicorn app:app --reload")
                    st.stop()

        # RENDER RESULTS (Outside the button block, driven by session state)
        if st.session_state.prediction_df is not None:
            prediction_df = st.session_state.prediction_df
            st.markdown("---")
            
            total = len(prediction_df)
            safe = len(prediction_df[prediction_df["predicted_column"] == 0])
            phishing = len(prediction_df[prediction_df["predicted_column"] == 1])

            safe_percent = round((safe / total) * 100, 2) if total > 0 else 0
            phishing_percent = round((phishing / total) * 100, 2) if total > 0 else 0

            st.subheader("📈 Prediction Summary")
            c1, c2 = st.columns(2)
            with c1:
                st.success(f"✅ Safe Websites : {safe}")
                st.progress(safe_percent / 100)
                st.write(f"**{safe_percent}%**")
            with c2:
                st.error(f"⚠️ Phishing Websites : {phishing}")
                st.progress(phishing_percent / 100)
                st.write(f"**{phishing_percent}%**")

            st.subheader("Prediction Result")
            search = st.text_input("🔍 Search in Prediction Result")

            if search:
                filtered_df = prediction_df[
                    prediction_df.astype(str).apply(
                        lambda row: row.str.contains(search, case=False).any(), axis=1
                    )
                ]
            else:
                filtered_df = prediction_df

            st.dataframe(filtered_df, use_container_width=True)
            st.markdown("---")

            st.subheader("📊 Prediction Analytics")
            chart1, chart2 = st.columns(2)
            with chart1:
                pie = px.pie(values=[safe, phishing], names=["Safe", "Phishing"], title="Prediction Distribution", hole=0.45)
                st.plotly_chart(pie, use_container_width=True)
            with chart2:
                bar = px.bar(x=["Safe", "Phishing"], y=[safe, phishing], title="Prediction Count", text=[safe, phishing])
                bar.update_traces(textposition="outside")
                st.plotly_chart(bar, use_container_width=True)

            csv = prediction_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇ Download Prediction CSV",
                csv,
                "prediction.csv",
                "text/csv"
            )

# ==========================================
# ABOUT PAGE
# ==========================================
elif page == "About":

    st.header("ℹ️ About Project")

    st.markdown("""
    ## 🛡️ Network Security - Phishing Website Detection System

    This project is developed to detect whether a website is **Safe** or **Phishing**
    using a Machine Learning model.

    The application provides an interactive dashboard where users can upload a CSV
    dataset and instantly predict phishing websites.
    """)

    st.markdown("---")

    st.subheader("🎯 Objective")

    st.info("""
    The main objective of this project is:

    • Detect phishing websites accurately.

    • Reduce cyber fraud.

    • Help users identify malicious websites.

    • Provide an easy-to-use prediction dashboard.
    """)

    st.markdown("---")

    st.subheader("⚙️ Project Workflow")

    st.code("""
User Upload CSV
        │
        ▼
 FastAPI Backend
        │
        ▼
 Data Preprocessing
        │
        ▼
 Random Forest Model
        │
        ▼
 Prediction
        │
        ▼
 Streamlit Dashboard
""")

    st.markdown("---")

    st.subheader("🛠️ Technology Stack")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
### Backend

✅ FastAPI

✅ Python

✅ Scikit-Learn

✅ Pandas
""")

    with col2:

        st.success("""
### Tools

✅ MongoDB Atlas

✅ MLflow

✅ Streamlit

✅ Git
""")

    st.markdown("---")

    st.subheader("⭐ Features")

    st.write("""
- Upload CSV Dataset
- Detect Safe & Phishing Websites
- Interactive Dashboard
- Prediction Summary
- Pie & Bar Charts
- Search Prediction Results
- Download Prediction Report
- FastAPI Integration
- Machine Learning Model
""")

    st.markdown("---")

    st.subheader("🚀 Future Improvements")

    st.write("""
- User Login System
- URL Prediction using Text Box
- Live Website Prediction
- Cloud Deployment
- Email Alert for Phishing URLs
- Better Dashboard Analytics
""")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.info("""
**Name:** Ranjit Darji

**Project:** Network Security - Phishing Website Detection

**Frontend:** Streamlit

**Backend:** FastAPI

**Machine Learning:** Scikit-Learn
""")

    st.markdown("---")

    st.caption(
        "© 2026 Network Security Dashboard | Developed by Ranjit Darji"
    )