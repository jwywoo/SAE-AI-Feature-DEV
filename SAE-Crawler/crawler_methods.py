from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from dotenv import load_dotenv

import pandas as pd
import re
import os 
import json

load_dotenv()

## Common Methods
### Getting Data
def load_csv(csv_name, dir="data"):
    print("Getting CSV ")
    csv_path = os.path.join(dir,csv_name)
    try:
        if os.path.exists(csv_path):
            return pd.read_csv(csv_path)
        else:
            return None
    except:
        print("Failed to load, csv not available")
        return None

def save_csv(csv_name, modified_df, dir="data"):
    path_name = os.path.join(dir, csv_name)
    modified_df.to_csv(path_name, index=False)


### Switch Frame
def switch_to_frame(driver, frame_name):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_name)


## KOSPI
def cleaning_text(raw_text):
    # Retrieve regex patterns from .env
    pattern_one = os.getenv("PREPROCESSING_ONE")
    pattern_two = os.getenv("PREPROCESSING_TWO")
    pattern_three = os.getenv("PREPROCESSING_THREE")

    # Apply regex preprocessing
    raw_text = re.sub(pattern_one, '', raw_text)
    raw_text = re.sub(pattern_two, '', raw_text)
    raw_text = re.sub(pattern_three, ' ', raw_text).strip()

    return raw_text
