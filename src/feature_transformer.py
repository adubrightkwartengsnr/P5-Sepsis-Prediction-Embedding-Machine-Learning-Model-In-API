from sklearn.base import BaseEstimator,TransformerMixin


# Define the FeatureEngin
class FeatureEngineeringTransformer(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass

    def fit(self,X,y=None):
        return self
        
    
    def transform(self, X):
        X = X.copy()
        X["BMI_Category"] = pd.cut(X["Body_Mass_Index"],bins=[0,18.5,24.9,29.5,float("inf")],
                            labels=["Underweight","Normal","Overweight","Obese"]).astype("object")
        X["BP_Category"] = pd.cut(X["Blood_Pressure"],bins=[0,120,129,139,float("inf")],
                            labels=["Normal","Prehypertension","Hypertension Stage 1","Hypertension Stage 2",]).astype("object")
        
        X["Age_Group"] = pd.cut(X["Age"],bins=[0,18,30,65,float("inf")],
                            labels=["Younger Age","Adults","Older People","Senior Citizens"]).astype("object")
        return X