from fastapi import FastAPI
import pandas as pd

# create an instance of FASTAPI
app = FastAPI()

# Create Endpoint for the Random Forest Pipeline
['Plasma_Glucose', 'Blood_Work_Result_1', 'Blood_Pressure',
       'Blood_Work_Result_2', 'Blood_Work_Result_3', 'Body_Mass_Index',
       'Blood_Work_Result_4', 'Age', 'Insurance']

def random_forest_predict_sepsis(data:pd.DataFrame):
    data = 