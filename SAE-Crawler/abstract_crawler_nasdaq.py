from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import pandas as pd
from time import sleep
from crawler_methods import *

SAVE_EVERY = 10
CSV_FILE = "nasdaq_1000.csv"

if __name__ == "__main__":
    print("Nasdaq Abstracts Crawling Started")

    # Load CSV
    loaded_csv = load_csv(csv_name=CSV_FILE)

    loaded_csv['company_abstract'] = loaded_csv['company_abstract'].astype(object)
    loaded_csv['korean_name'] = loaded_csv['korean_name'].astype(object)
    loaded_csv['english_name'] = loaded_csv['english_name'].astype(object)
    loaded_csv['industry'] = loaded_csv['industry'].astype(object)
    try:
        # Initialize Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        for i, row in loaded_csv.iterrows():
            print(f"{i+1}: {row['ticker_code']}")
            
            if pd.isna(row['company_abstract']):  # Check if 'company_abstract' is missing

                try:
                    driver.get(url=row['url_total'])
                    sleep(1)
                    industry = driver.find_element(By.XPATH, "//strong[text()='업종']/following-sibling::span").text
                    sleep(1)
                    driver.get(url=row['url_abs'])
                    sleep(1)
                    summary_info = driver.find_element(By.CSS_SELECTOR, "#stockContentWrapper > div.OverviewContainer_overviewContainer__bkkAQ > div.OverviewContainer_infoCorp__EFDdy")
                    korean_name = summary_info.find_element(By.CLASS_NAME, "OverviewContainer_name__6IrhS").text
                    english_name = summary_info.find_element(By.CLASS_NAME, "OverviewContainer_nameEng__PuxhR").text
                    abstract = summary_info.find_element(By.CLASS_NAME, "OverviewContainer_desc__ipokP").text
                    loaded_csv.at[i, 'industry'] = industry
                    loaded_csv.at[i, 'korean_name'] = korean_name
                    loaded_csv.at[i, 'english_name'] = english_name
                    loaded_csv.at[i, 'company_abstract'] = cleaning_text(abstract)
                except NoSuchElementException:
                    print("fucked")
                    loaded_csv.at[i, 'company_abstract'] = "Not Available"
            
            if (i%10 == 0):
                print("saved for 10")
                save_csv(csv_name=CSV_FILE, modified_df=loaded_csv)

        driver.quit()
    except WebDriverException as e:
        save_csv(csv_name=CSV_FILE, modified_df=loaded_csv)
        print(f"WebDriver error on {row['ticker_code']}: {e}")

    save_csv(csv_name = CSV_FILE,modified_df=loaded_csv)