from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import joblib
from feature_transformer import FeatureEngineeringTransformer

# create an instance of FASTAPI
app = FastAPI()


# load model components
def load_ml_components():
    with open("../models/sepsis_model_components.joblib","rb") as file:
        mode_components = joblib.load(file)
    return mode_components

model_components = load_ml_components()



# # Create SeppssisFeatures class from pydantic BaseModel
class SepssisFeatures(BaseModel):
    Plasma_Glucose:int
    Blood_Work_Result_1: int
    Blood_Pressure: int
    Blood_Work_Result_2: int
    Blood_Work_Result_3: int
    Body_Mass_Index: float
    Blood_Work_Result_4: float
    Age: int
    Insurance: int


# # Create Endpoint for the XGB Classifier Pipeline
@app.post("/predict_sepsis/xgb_classifier")
async def predict_sepsis(data:SepssisFeatures):
    # create dataframe from sepssis data
    df = pd.DataFrame([data.model_dump()])
    # call the random_forest_pipeline and encoder from the ml model
    xgb_classifier_pipeline = model_components["xgb_classifier"]
    encoder = model_components["encoder"]
    # make prediction
    prediction = xgb_classifier_pipeline.predict(df)
    prediction = int(prediction[0])
    decoded_prediction = encoder.inverse_transform([prediction])[0]
    prediction_proba = xgb_classifier_pipeline.predict_proba(df)[0].tolist()
    return {"prediction": decoded_prediction,"prediction_probability":prediction_proba}

# # Create Endpoint for the Gradient Boost Model
@app.post("/predict_sepsis/gradient_boost")
async def predict_sepsis(data:SepssisFeatures):
    # create dataframe from sepssis data
    df = pd.DataFrame([data.model_dump()])
    # call the random_forest_pipeline and encoder from the ml model
    gradient_boost_pipeline = model_components["gradient_boost"]
    encoder = model_components["encoder"]
    # make prediction
    prediction = gradient_boost_pipeline.predict(df)
    prediction = int(prediction[0])
    decoded_prediction = encoder.inverse_transform([prediction])[0]
    prediction_proba = gradient_boost_pipeline.predict_proba(df)[0].tolist()
    return {"prediction": decoded_prediction,"prediction_probability":prediction_proba}