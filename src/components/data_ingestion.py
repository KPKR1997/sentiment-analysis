import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass 
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_Ingestion(self):
         logging.info("Data ingestion started")
         try:
             df = pd.read_csv(r'notebooks\student.csv')
             logging.info("Data ingestion completed. Data frame created with the file")

             os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

             df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)
             
             train, test = train_test_split(df, test_size = 0.2, random_state = 42)
             logging.info("Train_test_split initiated")

             train_set = df.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
             train_set = df.to_csv(self.ingestion_config.test_data_path, index=False, header = True)
             logging.info("Ingestion completed, Required data files created in artifacts")

             return(
                 self.ingestion_config.train_data_path,
                 self.ingestion_config.test_data_path
             )

         except Exception as e:
             raise CustomException(e,sys)
         

if __name__ == "__main__":
    object = DataIngestion()
    object.initiate_data_Ingestion()
    