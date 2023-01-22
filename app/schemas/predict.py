from pydantic import BaseModel
from typing import Optional, Any, List
from insurance_claim_model.processing.validation import InsuranceDataInputScheme

class PredictResults(BaseModel):
    errors:    Optional[Any]
    version:    str
    predictions:    Optional[List[float]]

class MultipleInsuranceInputs(BaseModel):
    inputs: List[InsuranceDataInputScheme]

    class Config:
        schema_extra = {
            "example":
            {
                "inputs":[
                    {
                    'index': 1023,
                    'PatientID': 1024,
                    'age': 51.0,
                    'gender': 'female',
                    'bmi': 41.3,
                    'bloodpressure': 98,
                    'diabetic': 'No',
                    'children': 0,
                    'smoker': 'No',
                    'region': 'northeast'
                    }
                ]
            }
        }

