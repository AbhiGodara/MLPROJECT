import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation,DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig,ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r"notebook\data\student.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_array,test_array,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # x_train = train_array[:, :-1]
    # y_train = train_array[:, -1]
    # x_test = test_array[:, :-1]
    # y_test = test_array[:, -1]
    # print("x_train shape:", x_train.shape)
    # print("x_test shape:", x_test.shape)
    # print("y_train shape:", y_train.shape)
    # print("y_test shape:", y_test.shape)
    # print("First few y_train:", y_train[:5])
    # print("First few y_test:", y_test[:5])
    # print("Unique y_train values:", np.unique(y_train))
    # print("Unique y_test values:", np.unique(y_test))

    modeltrainer=ModelTrainer()
    R2_score=modeltrainer.initiate_model_trainer(train_array,test_array)
    print(f"R2 Score of the best model: {R2_score}")