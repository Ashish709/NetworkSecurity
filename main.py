from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.excpetion.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfg)
        
        logging.info("Initiate the Data Ingestion")
        
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        
        print(dataingestionartifact)
        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
