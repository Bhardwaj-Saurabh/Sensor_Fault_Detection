import os

SAVED_MODEL_DIR = os.path.join('saved_models')

# define constant variable for training pipeline
TARGET_COLUMN = 'class'
PIPELINE_NAME = 'sensor'
ARTIFACT_DIR = 'artifact'
FILE_NAME = 'sensor.csv'

TRAIN_FILE_NAME = 'train.csv'
TEST_FILE_NAME = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
MODEL_FILE_NAME = 'model.pkl'
SCHEMA_FILE_NAME = os.path.join('config', 'schema.yaml')
SCHEMA_DROP_COLS = 'drop_Columns'