import streamlit as st
import requests

st.set_page_config(
    page_title="Sepsis Prediction Page",
    page_icon="🤖",
    layout="wide"
)

# set title of the application
st.title("Sepssis Classifier Application 🤖")

# # load the api endpoints
# gradient_boost_endpoint = "http://127.0.0.1:8000/predict_sepsis/gradient_boost"
# log_regression_endpoint = "http://127.0.0.1:8000/predict_sepsis/log_regression"

# endpoints from Docker
gradient_boost_endpoint = "http://api:8000/predict_sepsis/gradient_boost"
log_regression_endpoint = "http://api:8000/predict_sepsis/log_regression"


# select between the two endpoints of the ml_model
col1,col2 = st.columns(2)
with col2:
    st.selectbox("Model Selection",options=["Logistic Regression","Gradient Boost"],key="model_select")

# initializa select model session state
if "model_select" not in st.session_state:
    st.session_state["model_select"] = "Logistic Regression"

# Initialize session state for input features
input_keys = ["Plasma_Glucose", "Blood_Work_Result_1", "Blood_Pressure", "Blood_Work_Result_2",
              "Blood_Work_Result_3", "Body_Mass_Index", "Blood_Work_Result_4", "Age", "Insurance"]


for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = 0

# define function to accept inputs and display forms
def display_forms():
    with st.form("input-features"):
        col1,col2 = st.columns(2)
        with col1:
            st.number_input("Plasma Glucose",min_value=0,step=1,key = "Plasma_Glucose")
            st.number_input("Blood Work Result 1",min_value=0,step=1,key = "Blood_Work_Result_1")
            st.number_input("Blood Pressure",min_value=0,step=1,key = "Blood_Pressure")
            st.number_input("Blood Work Result 2",min_value=0,step=1,key = "Blood_Work_Result_2")
           
        with col2:
            st.number_input("Blood Work Result 3",min_value=0,step=1,key = "Blood_Work_Result_3")
            st.number_input("Body Mass Index",min_value=0.0,step=0.1,key = "Body_Mass_Index")
            st.number_input("Blood Work Result 4",min_value=0.0,step=0.1,key = "Blood_Work_Result_4")
            st.number_input("Age", min_value=0, step=1, key = "Age")
            st.number_input("Insurance",min_value=0, max_value =1,step=1,key = "Insurance")
        submit_button = st.form_submit_button("Predict")
    return submit_button


# define function to make predictions
def make_prediction():
    input_features = {key: st.session_state[key] for key in input_keys}
    if st.session_state["model_select"] == "Logistic Regression":
        # send api resopnse to the gradient boost api
        log_regression_response =requests.post(log_regression_endpoint,json=input_features)
        if log_regression_response.status_code == 200:
            print(log_regression_response.status_code)
            prediction = log_regression_response.json()["prediction"]
            probability = log_regression_response.json()["prediction_probability"]
            st.divider()
            st.success(f"The Sepssis prediction is: {prediction}, with the following prediction probabilities {probability}")
        else:
            st.error(f"Error: {  log_regression_response.json()["error"]}")
    else:
        gradient_boost_response =requests.post(gradient_boost_endpoint,json=input_features)
        print(gradient_boost_response.status_code)
        if gradient_boost_response.status_code == 200:
            print(gradient_boost_response.status_code)
            prediction = gradient_boost_response.json()["prediction"]
            probability = gradient_boost_response.json()["prediction_probability"]
            st.divider()
            st.success(f"The Sepssis prediction is: {prediction}, with the following prediction probabilities {probability}")
        else:
            st.error(f"Error: {gradient_boost_response.json()["error"]}")




if __name__ == "__main__":
    submit_button = display_forms()
    if submit_button:
        make_prediction()