from cnnClassifier import logger
logger.info("This is an info message")

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeleine
from cnnClassifier.pipeline.stage_02_model_building import PrepareBaseModelTrainingPipeleine

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"------ STAGE :{STAGE_NAME} STARTED----------")
    
    data_ingestion = DataIngestionTrainingPipeleine()
    data_ingestion.main()
    
    logger.info(f"------------ STAGE: {STAGE_NAME} COMPLETED-----------")
    
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"------ STAGE :{STAGE_NAME} STARTED----------")
    
    prepare_base_model  = PrepareBaseModelTrainingPipeleine()
    prepare_base_model.main()
    
    logger.info(f"------------ STAGE: {STAGE_NAME} COMPLETED-----------")
    
    
except Exception as e:
    logger.exception(e)
    raise e