# ================================= Importing libraries ====================================
import os



import json
import joblib
import sys

from pathlib import Path
from typing import Any
import pandas as pd
from datetime import timedelta


# evaluation
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

import os, uuid


# ====================================== Utility Functions ==========================================








def load_bin(path: Path):
    """load binary data

    Args:
        path: path to binary file

    Returns: binary file object.

    """
    try:
        # read binary data
        data = joblib.load(path)

        #logging.info(f"binary file loaded from: {path}")

        return data

    except Exception as e:
        print(e)
        #logging.info(e)
        #raise CustomException(e, sys)



