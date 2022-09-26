import urllib3
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv("Mon_API_key")

def get_data_lambda(event, context):
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token="+API_Key
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    return values
