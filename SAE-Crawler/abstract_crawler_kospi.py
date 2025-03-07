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
CSV_FILE = "kospi_900.csv"

if __name__ == "__main__":
    print("Kospi Abstracts Crawling Started\n")

    # Load CSV
    loaded_csv = load_csv(csv_name=CSV_FILE)
    loaded_csv['company_abstract'] = loaded_csv['company_abstract'].astype(object)
    
    try:
        # Initialize Chrome Driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        for i,row in loaded_csv.iterrows():
            if pd.isna(row['company_abstract']):  # Check if 'company_abstract' is missing
                driver.get(url=row['ur'])
                sleep(1)

                # Button
                try:
                    company_abstract_button = driver.find_element(By.CSS_SELECTOR, "#middle > div.h_company > div.wrap_company > div > em.summary > a")
                    company_abstract_button.click()
                    sleep(1)

                    # Get abstract text
                    summary_info = driver.find_element(By.CSS_SELECTOR, "#summary_info")
                    loaded_csv.at[i, 'company_abstract'] = cleaning_text(summary_info.text)
                    print(f"{i+1}: {row['ticker_code']} - Crawled")
                except NoSuchElementException:
                    loaded_csv.at[i, 'company_abstract'] = "Not Available"
                    print(f"{i+1}: {row['ticker_code']} - NA")
            
            if (i%10 == 0):
                print("saved for 10")
                save_csv(csv_name=CSV_FILE, modified_df=loaded_csv)
        
        driver.quit()      

    except WebDriverException as e:
        save_csv(csv_name=CSV_FILE, modified_df=loaded_csv)
        print(f"WebDriver error on {row['ticker_code']}: {e}")
    
    save_csv(csv_name=CSV_FILE, modified_df=loaded_csv)
