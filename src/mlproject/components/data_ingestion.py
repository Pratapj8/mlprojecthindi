import os
import sys
from src.mlproject.exception import CustomeException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_csv_data  # Updated import

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Reading data from CSV instead of MySQL
            df = read_csv_data()  
            logging.info("Reading completed from CSV file")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Saving raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Splitting data
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving split data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomeException(e, sys)
