from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.pipline.training_pipeline import TrainPipeline
import sys


logging.info("Welcome to the arena!!")

# try:
#     a = 2/0
# except Exception as e:
#     raise USvisaException(e,sys)

from us_visa import logger # After setting up a local package
from us_visa.configuration.mongo_db_connection import MongoDBClient

# import dagshub
# dagshub.init(repo_owner='utkarsh-iitbhu', repo_name='mlflow-dvc-classification-tf', mlflow=True)

# STAGE_NAME = "Data Ingestion Stage"

# logging.info("Welcome to our pipeline")

# try:
#     logging.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<")
#     obj = MongoDBClient()
#     logging.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx=================x")
# except Exception as e:
#     raise USvisaException(e,sys)

obj = TrainPipeline()
obj.run_pipeline()