import requests
import pandas as pd
from retrying import retry

@retry(stop_max_attempt_number=5, wait_fixed=5000)
def fetch_data():
    api_url = "https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/orbits-for-near-earth-asteroids-neas@datastro/records?limit=100&refine=last_obs%3A%222023%22"
    response = requests.get(api_url, timeout=20)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception("API request failed")
    
try:
    nea_data = fetch_data()

    if nea_data is not None:
        nea_data.to_csv("nea_data.csv", index = False)
except Exception as e:
    print("An error occurred:", str(e))