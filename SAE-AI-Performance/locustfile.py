import time
import os
import pandas as pd
import random


from locust import HttpUser, task, between

def load_csv_data(filename = "test_request_locust.csv"):
    if (not os.path.exists(filename)):
        return None
    df = pd.read_csv(filename)
    return df.to_dict(orient="records")

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8000"
    stock_data = load_csv_data("request_examples/test_request_locust.csv")

    @task
    def stock_generation_requests(self):
        stock_request = random.choice(self.stock_data)
        
        payload = {
            "title":stock_request['title'],
            "url":stock_request['url'],
            "content":stock_request['content']
        }
        
        response = self.client.post("/ai/stock/generation", json=payload)
