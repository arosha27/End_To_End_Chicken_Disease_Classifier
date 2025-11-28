from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_building import PrepareBaseModel

from cnnClassifier import logger 

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeleine:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
        
