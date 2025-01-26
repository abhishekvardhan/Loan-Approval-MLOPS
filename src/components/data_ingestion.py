import pandas as pd
import numpy as np

import os
import sys

from logger import setup_logger

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

logger=setup_logger()
def load_split_data():
    logger.info("Logger is set up")
    output_dir = Path(__file__).parent / '..'/ '..' / 'artifacts' 
    output_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    file_path = output_dir / 'loan_data.csv'
    data = pd.read_csv(file_path)
    data=data.drop(columns=['person_age'])
    logger.info("Data is loaded")
    logger.info(f"Data shape: {data.shape}")
    train_data,test_data=train_test_split(data,test_size=0.25)
    logger.info("Data is split into train and test")

    train_data.to_csv(output_dir / 'train_data.csv', index=False)
    test_data.to_csv(output_dir / 'test_data.csv', index=False)
    logger.info("Data is saved to disk")
