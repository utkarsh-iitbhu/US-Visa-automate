from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationArtifact: # Output
    validation_status:bool # Valid data boolean
    message: str 
    drift_report_file_path: str # Wether data is drifted or not

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str # Pickle file path
    transformed_train_file_path:str # Train file path
    transformed_test_file_path:str # Test file path
    
@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact