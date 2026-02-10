# Creating a dataclass and specifying all the static varibales I defined in config.yaml in this entity 

from pathlib import Path
from dataclasses import dataclass


#setting the frozen parameter to true means that no more varibles can be included 

# ===================== DATA INGESTION ===============================
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir :Path
    source_URL : str
    local_data_file : Path 
    unzip_dir : Path
     

# ========================== MODEL BUILDING ==============================
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

#============================= TRAINING ======================================
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list