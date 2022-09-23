import urllib3
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv("Mon_API_key")


def get_data():
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token="+API_Key
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
