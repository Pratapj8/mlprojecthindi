from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer

import sys
import pandas as pd

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Load data from CSV files
        train_data = pd.read_csv(train_data_path)
        test_data = pd.read_csv(test_data_path)

        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        model_trainer = ModelTrainer()
        r2_score_value = model_trainer.initiate_model_trainer(train_arr, test_arr)  # Use transformed data
        print(f"R² Score of the best model: {r2_score_value:.16f}")  # ✅ Print R² Score

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
