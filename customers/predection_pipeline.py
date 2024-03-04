# =================================== Importing Library ==========================================

from pathlib import Path

import pandas as pd


from .common import load_bin



# ====================================== Prediction Pipeline ============================================


class PredictionPipeline:

    def __init__(self):
        pass

    def predict(self, features):

        # load model
        model = load_bin(r'C:\Users\User\Desktop\New folder\bank\customers\model.joblib')
        print("MOdel Successfully Uploaded")
        # load preprocessor str
        preprocessor = load_bin(r'C:\Users\User\Desktop\New folder\bank\customers\proprocessor.joblib')
        print("Preprocessor Successfully Uploaded")
        # load target label encoder str
        #target_encoder = load_bin(Path(self.config.target_encoder_obj_file_pat))

        #logging.info("Loaded model,preprocessor,target encoder str")

        # apply preprocessing
        train_data = preprocessor.transform(features)
        #logging.info("applied preprocessing on upcoming data")

        # taking predection
        preds = model.predict(train_data)
        #logging.info("Took prediction on upcoming data")

        return preds


# To convert custom data to dataframe


class CustomData:
    def __init__(
        self,
        age: int,
        balance: int,
        campaign: int,
        contact: str,
        day: int,
        default: str,
        duration: int,
        education: str,
        housing: str,
        job: str,
        loan: str,
        marital: str,
        month: str,
        pdays: int,
        poutcome: str,
        previous: int,
    ):

        self.age = age
        self.balance = balance
        self.campaign = campaign
        self.contact = contact
        self.day = day
        self.default = default
        self.duration = duration
        self.education = education
        self.housing = housing
        self.job = job
        self.loan = loan
        self.marital = marital
        self.month = month
        self.pdays = pdays
        self.poutcome = poutcome
        self.previous = previous

    def get_data_as_data_frame(self):

        try:
            custom_data_input_dict = {
                "age": [self.age],
                "balance": [self.balance],
                "campaign": [self.campaign],
                "contact": [self.contact],
                "day": [self.day],
                "default": [self.default],
                "duration": [self.duration],
                "education": [self.education],
                "housing": [self.housing],
                "job": [self.job],
                "loan": [self.loan],
                "marital": [self.marital],
                "month": [self.month],
                "pdays": [self.pdays],
                "poutcome": [self.poutcome],
                "previous": [self.previous],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            print(e)
