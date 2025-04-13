from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainder
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


# To Check Data Ingestion
# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
#         dataingestion = DataIngestion(dataingestionconfg)
        
#         logging.info("Initiate the Data Ingestion")
        
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
        
#         print(dataingestionartifact)
        
    
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)



## To Check Data validation
# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
#         dataingestion = DataIngestion(dataingestionconfg)
        
#         logging.info("Initiate the Data Ingestion")
        
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
#         logging.info("Data Ingestion Completed")
#         print(dataingestionartifact)
        
#         data_validation_config = DataValidationConfig(trainingpipelineconfig)
#         data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
#         logging.info("Initiate the Data Validation")
#         data_validation_artifact = data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed")
        # print(data_validation_artifact)
    
    # except Exception as e:
    #     raise NetworkSecurityException(e,sys)
    

## To Check data Transformation    
# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
#         dataingestion = DataIngestion(dataingestionconfg)
        
#         logging.info("Initiate the Data Ingestion")
        
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
#         logging.info("Data Ingestion Completed")
#         print("dataingestionartifact",dataingestionartifact)
        
#         data_validation_config = DataValidationConfig(trainingpipelineconfig)
#         data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
#         logging.info("Initiate the Data Validation")
#         data_validation_artifact = data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed")
#         print("data_validation_artifact:",data_validation_artifact)
        
        
#         data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
#         logging.info("Initiate the Data Transformation")
#         data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
#         data_transformation_artifact = data_transformation.initiate_data_transformation()
#         logging.info("Data Transformation Completed")
#         print("data_transformation_artifact:",data_transformation_artifact)
    
#     except Exception as e:
        
#         raise NetworkSecurityException(e,sys)    



### To Check Model Trainder
if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfg)
        
        logging.info("Initiate the Data Ingestion")
        
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        # print("dataingestionartifact",dataingestionartifact)
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
        logging.info("Initiate the Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        # logging.info("Data Validation Completed")
        # print("data_validation_artifact:",data_validation_artifact)
        
        
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiate the Data Transformation")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        # print("data_transformation_artifact:",data_transformation_artifact)
        
        logging.info("Model Training Started")
        model_trainder_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainder(model_trainder_config, data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiated_model_trainer()
        logging.info("Model Training Completed")
    
    except Exception as e:
        
        raise NetworkSecurityException(e,sys)    