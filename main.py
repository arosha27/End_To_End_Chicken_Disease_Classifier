from cnnClassifier import logger
logger.info("This is an info message")

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeleine
from cnnClassifier.pipeline.stage_02_model_building import PrepareBaseModelTrainingPipeleine
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import ModelEvaluationPipeline


#-------------------DATA INGESTION STAGE-----------------------------
STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"------ STAGE :{STAGE_NAME} STARTED----------")
    
    data_ingestion = DataIngestionTrainingPipeleine()
    data_ingestion.main()
    
    logger.info(f"------------ STAGE: {STAGE_NAME} COMPLETED-----------")
    
except Exception as e:
    logger.exception(e)
    raise e



#-------------------PREPARE BASE MODEL STAGE-----------------------------
STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"------ STAGE :{STAGE_NAME} STARTED----------")
    
    prepare_base_model  = PrepareBaseModelTrainingPipeleine()
    prepare_base_model.main()
    
    logger.info(f"------------ STAGE: {STAGE_NAME} COMPLETED-----------")
    
    
except Exception as e:
    logger.exception(e)
    raise e



#-------------------MODEL TRAINING STAGE-----------------------------
STAGE_NAME = "Model Training"
try:
    logger.info(f"************************************")
    logger.info(f"-------------------------STAGE {STAGE_NAME} started----------------------------")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"----------------------STAGE {STAGE_NAME} completed---------------------------")
    
    
except Exception as e:
    logger.exception(e)
    raise e


#-------------------MODEL EVALUATION STAGE-----------------------------
STAGE_NAME = "Evaluation"
try:
    
    logger.info(f"---------------------------------")
    logger.info(f"-----------------------STAGE {STAGE_NAME} started--------------------")
    model_evaluator = ModelEvaluationPipeline()
    model_evaluator.main()
    logger.info(f"------------------------STAGE {STAGE_NAME} completed-----------------------")
    
except Exception as e:
    logger.exception(e)
    raise e