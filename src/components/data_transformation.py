import pandas as pd
import numpy as np
from logger import setup_logger
import os
import sys
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from pathlib import Path
logger=setup_logger()

def get_data_transformation():
   person_education= ['High School','Bachelor', 'Associate', 'Master','Doctorate'],  # Categories for 'size'
   person_home_ownership= ['OTHER', 'RENT', 'MORTGAGE','OWN'],     # Categories for 'quality'
   previous_loan_defaults_on_file= ['Yes','No']
   ordinal_cols = ['person_education', 'person_home_ownership', 'previous_loan_defaults_on_file']
   onehot_cols=['loan_intent']
   numerical_cols=['person_age',  'person_income', 'loan_amnt',  'loan_percent_income', 'cb_person_cred_hist_length','credit_score']
   ordinal_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinalencoder', OrdinalEncoder(categories=[person_education,person_home_ownership,previous_loan_defaults_on_file])),
    ('scaler', StandardScaler())
    ])
    # Pipeline for one-hot encoding
   onehot_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine both pipelines using ColumnTransformer
   preprocess_pipeline = ColumnTransformer(transformers=[
    ('ordinal', ordinal_pipeline, ordinal_cols),
    ('onehot', onehot_pipeline, onehot_cols),
    ('num_pipeline',num_pipeline,numerical_cols),
    ])
   num_pipeline=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())])
   return preprocess_pipeline


def transform_data():
    logger.info("Transforming data")
    output_dir = Path(__file__).parent / '..'/ '..' / 'artifacts' 
    output_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    train_data=pd.read_csv(output_dir+"/train.csv")
    test_data=pd.read_csv(output_dir+"/test.csv")
    logger.info("Data is loaded")
    logger.info(f"train_data columns: {train_data.columns}")
    X_train=train_data.drop(columns=['loan_status'])
    X_test=test_data.drop(columns=['loan_status'])
    y_train=train_data['loan_status']
    y_test=test_data['loan_status']
    logger.info("data before transformation is"+str(X_train.head()))
    X_train = get_data_transformation.fit_transform(X_train)
    X_test = get_data_transformation.transform(X_test)
    logger.info("data after transformation is"+str(X_train.head()))
    
    return transformed_data