import os
import sys
from src.mlproject.exception import CustomeException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
# import pymysql  # Commented out since we're not using MySQL now

load_dotenv()

# MySQL Configuration (commented out for future use)
# host = os.getenv("host")
# user = os.getenv("user")
# password = os.getenv("password")
# db = os.getenv("db")
# port = int(os.getenv("port"))  # Ensure port is an integer

# File path to the CSV
file_path = "/Users/apple/Downloads/Data_science_file/Krish_naik_Files_notes/PracticeProject/stud.csv"

def read_csv_data():
    """
    Function to read data from a CSV file.
    :return: DataFrame containing the CSV data.
    """
    logging.info("Reading data from CSV file started")
    try:
        df = pd.read_csv(file_path)
        logging.info("CSV file read successfully")
        print(df.head())
        return df
    except Exception as ex:
        raise CustomeException(ex, sys)

# Commented out the MySQL part for now
# def read_sql_data():
#     logging.info("Reading data from SQL database started")
#     try:
#         # Use environment variables for the connection
#         mydb = pymysql.connect(
#             host=host,
#             user=user,
#             password=password,
#             db=db,
#             port=port
#         )
#         logging.info("Connection Established", mydb)
#         df = pd.read_sql_query("SELECT * FROM students", mydb)
#         print(df.head())
#         return df
#     except Exception as ex:
#         raise CustomeException(ex, sys)
