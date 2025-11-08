from cnnClassifier import logger
logger.info("This is an info message")

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeleine

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"------ STAGE :{STAGE_NAME} STARTED----------")
    
    data_ingestion = DataIngestionTrainingPipeleine()
    data_ingestion.main()
    
    logger.info(f"------------ STAGE: {STAGE_NAME} COMPLETED-----------")
    
    
except Exception as e:
    logger.exception(e)
    raise e