# Creating a dataclass and specifying all the static varibales I defined in config.yaml in this entity 

from pathlib import Path
from dataclasses import dataclass


#setting the frozen parameter to true means that no more varibles can be included 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir :Path
    source_URL : str
    local_data_file : Path 
    unzip_dir : Path