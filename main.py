import streamlit as st
from prediction_helper import predict

# Set the page configuration and title
st.set_page_config(page_title="Credit Risk Modelling")
st.title("📊Credit Risk Modelling")

# Header information and instructions
st.write("Welcome to Credit Risk Modelling tool! Fill in the applicant's details below to assess credit risk probability, score, and rating.")

# Input fields with a cleaner layout (two columns per row)
# Row 1: Basic Applicant Info
st.subheader("Applicant Information")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with col2:
    income = st.number_input('Annual Income (₹)', min_value=0, value=1200000)

# Row 2: Loan Details
st.subheader("Loan Details")
col3, col4 = st.columns(2)
with col3:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)
with col4:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)

# Row 3: Loan to Income Ratio
st.subheader("Financial Ratios")
loan_to_income_ratio = loan_amount / income if income > 0 else 0
st.write("Loan to Income Ratio:")
st.write(f"{loan_to_income_ratio:.2f}")

# Row 4: Delinquency & Credit Utilization
col5, col6 = st.columns(2)
with col5:
    avg_dpd_per_delinquency = st.number_input('Avg DPD per Delinquency', min_value=0, value=20)
with col6:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)

# Row 5: Additional Financial Details
col7, col8 = st.columns(2)
with col7:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with col8:
    num_open_accounts = st.number_input('Number of Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

# Row 6: Loan and Applicant Profile
st.subheader("Profile Details")
col9, col10 = st.columns(2)
with col9:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with col10:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

# Row 7: Loan Type
loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

# Calculate Risk Button
if st.button('📈 Calculate Risk'):
    # Call the predict function from the helper module
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    # Display the results
    st.write(f"Deafult Probability: {probability:.2%}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")
