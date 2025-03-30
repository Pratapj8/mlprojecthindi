import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pickle
import numpy as np

load_dotenv()

file_path = "/Users/apple/Downloads/Data_science_file/Krish_naik_Files_notes/PracticeProject/stud.csv"

def read_csv_data(file_path):
    try:
        logging.info("Reading data from CSV file started")
        df = pd.read_csv(file_path)
        logging.info("CSV file read successfully")
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}
        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            para = param.get(model_name, {})  # Safely get params

            logging.info(f"Evaluating model: {model_name}")

            if para:  # Apply GridSearch only if params exist
                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)
                model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
