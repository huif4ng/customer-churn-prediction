import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    layout="wide"
)

# load model
@st.cache_resource
def load_model():
    feature_names = joblib.load('models/feature_names.pkl')
    pipeline = joblib.load("models/churn_pipeline.pkl")
    return pipeline, feature_names

pipeline, feature_names = load_model()

# profile preset
LOW_RISK_PROFILE = {
    "tenure": 48,
    "contract": "Two year",
    "paperless_billing": "No",
    "payment_method": "Bank transfer (automatic)",
    "phone_service": "Yes",
    "multiple_lines": "Yes",
    "internet_service": "DSL",
    "online_security": "Yes",
    "online_backup": "Yes",
    "device_protection": "Yes",
    "tech_support": "Yes",
    "streaming_tv": "Yes",
    "streaming_movies": "Yes",
    "monthly_charges": 55.0,
    "total_charges": 2640.0,
    "gender": "Male",
    "senior_citizen": "No",
    "partner": "Yes",
    "dependents": "Yes",
}

HIGH_RISK_PROFILE = {
    "tenure": 2,
    "contract": "Month-to-month",
    "paperless_billing": "Yes",
    "payment_method": "Electronic check",
    "phone_service": "Yes",
    "multiple_lines": "No",
    "internet_service": "Fiber optic",
    "online_security": "No",
    "online_backup": "No",
    "device_protection": "No",
    "tech_support": "No",
    "streaming_tv": "No",
    "streaming_movies": "No",
    "monthly_charges": 95.0,
    "total_charges": 190.0,
    "gender": "Female",
    "senior_citizen": "Yes",
    "partner": "No",
    "dependents": "No",
}

def init_state(profile=None):
    defaults = profile or {}
    fields = [
        ("tenure", 12), ("contract", "Month-to-month"),
        ("paperless_billing", "Yes"), ("payment_method", "Electronic check"),
        ("phone_service", "Yes"), ("multiple_lines", "No"),
        ("internet_service", "DSL"), ("online_security", "No"),
        ("online_backup", "No"), ("device_protection", "No"),
        ("tech_support", "No"), ("streaming_tv", "No"),
        ("streaming_movies", "No"), ("monthly_charges", 65.0),
        ("total_charges", 780.0), ("gender", "Male"),
        ("senior_citizen", "No"), ("partner", "Yes"), ("dependents", "No"),
    ]
    for key, default in fields:
        st.session_state[key] = defaults.get(key, default)

if "tenure" not in st.session_state:
    init_state()

# UI
st.title("Churn Risk Predictor")
st.write("Select customer persona below to predict churn probability.")

# Profile preset buttons
st.markdown("**Quick Profiles:**")
btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 6])
with btn_col1:
    if st.button("✅ Low Risk Profile", type="secondary"):
        init_state(LOW_RISK_PROFILE)
        st.rerun()
with btn_col2:
    if st.button("⚠️ High Risk Profile", type="secondary"):
        init_state(HIGH_RISK_PROFILE)
        st.rerun()

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Account Info")
    tenure = st.slider("Tenure (months)", 0, 72, st.session_state["tenure"])
    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"],
        index=["Month-to-month", "One year", "Two year"].index(st.session_state["contract"])
    )
    paperless_billing = st.selectbox(
        "Paperless Billing", ["Yes", "No"],
        index=["Yes", "No"].index(st.session_state["paperless_billing"])
    )
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check",
         "Bank transfer (automatic)", "Credit card (automatic)"],
        index=["Electronic check", "Mailed check",
               "Bank transfer (automatic)", "Credit card (automatic)"].index(
                   st.session_state["payment_method"])
    )

with col2:
    st.subheader("Services")
    phone_service = st.selectbox(
        "Phone Service", ["Yes", "No"],
        index=["Yes", "No"].index(st.session_state["phone_service"])
    )
    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"],
        index=["No", "Yes", "No phone service"].index(st.session_state["multiple_lines"])
    )
    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"],
        index=["DSL", "Fiber optic", "No"].index(st.session_state["internet_service"])
    )

    security_options = ["Yes", "No", "No internet service"]
    online_security = st.selectbox(
        "Online Security", security_options,
        index=security_options.index(st.session_state["online_security"])
    )
    for i, value in enumerate(security_options):
        if value == online_security:
            default = i

    online_backup = st.selectbox(
        "Online Backup", security_options,
        index=security_options.index(st.session_state["online_backup"])
    )
    device_protection = st.selectbox(
        "Device Protection", security_options,
        index=security_options.index(st.session_state["device_protection"])
    )
    tech_support = st.selectbox(
        "Tech Support", security_options,
        index=security_options.index(st.session_state["tech_support"])
    )
    streaming_tv = st.selectbox(
        "TV Streaming", security_options,
        index=security_options.index(st.session_state["streaming_tv"])
    )
    streaming_movies = st.selectbox(
        "Movies Streaming", security_options,
        index=security_options.index(st.session_state["streaming_movies"])
    )

with col3:
    st.subheader("Billing")
    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0, max_value=200.0,
        value=float(st.session_state["monthly_charges"])
    )
    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0, max_value=10000.0,
        value=float(st.session_state["total_charges"])
    )
    gender = st.selectbox(
        "Gender", ["Male", "Female"],
        index=["Male", "Female"].index(st.session_state["gender"])
    )
    senior_citizen = st.selectbox(
        "Senior Citizen", ["No", "Yes"],
        index=["No", "Yes"].index(st.session_state["senior_citizen"])
    )
    partner = st.selectbox(
        "Has Partner", ["Yes", "No"],
        index=["Yes", "No"].index(st.session_state["partner"])
    )
    dependents = st.selectbox(
        "Has Dependents", ["Yes", "No"],
        index=["Yes", "No"].index(st.session_state["dependents"])
    )

st.divider()

if st.button("Predict Churn Risk", type="primary"):
    # training features
    input_data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
        'Partner': partner,
        'Dependents': dependents,
        'PhoneService': phone_service,
        'PaperlessBilling': paperless_billing,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security, 
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaymentMethod': payment_method
    }
    input_df = pd.DataFrame([input_data])
    input_df["has_streaming"] = (
        (input_df['StreamingTV'] == "Yes") | 
        (input_df['StreamingMovies'] == "Yes")
    ).astype(int)
    input_df = input_df[feature_names]

    # predict
    churn_prob = pipeline.predict_proba(input_df)[0][1]

    THRESHOLD = 0.5

    # display result
    col_result1, col_result2 = st.columns(2)

    with col_result1:
        if churn_prob >= THRESHOLD:
            st.error(f"⚠️ High Churn Risk")
        else:
            st.success(f"✅ Low Churn Risk")

        st.metric(
            "Churn Probability", 
            f"{churn_prob:.1%}",
            # delta=f"Threshold: {THRESHOLD:.0%}"
        )

    with col_result2:
        # probability gauge
        fig, ax = plt.subplots(figsize=(4, 1.5))
        ax.barh(
            [''], [churn_prob], 
            color='#e74c3c' if churn_prob >= THRESHOLD else '#2ecc71',
            height=0.5
        )
        ax.barh(
            [''], [1 - churn_prob], 
            left=[churn_prob],
            color='#ecf0f1', height=0.5
        )
        ax.set_xlim(0, 1)
        ax.axvline(x=THRESHOLD, color='gray', linestyle='--', linewidth=1)
        ax.set_xlabel('Churn Probability')
        ax.set_title('Risk Score')
        st.pyplot(fig)
        plt.close()
