import requests
from pandas.io.json import json_normalize
import pandas as pd

## test for demo SEs
url = "https://api.exchangeratesapi.io/history"
payload = ""
headers = ""

def rate_per_day(start_at,end_at,base,symbols):
    
    """
    This function retrieves the exchange rate per day, from exchangeratesapi.io
    You must specify the start date:start_at, the end date:end_at, the base currency:base and the output currency:symbols
    It returns a two-columns dataframe 
    """
        #temptemp
    querystring = {"start_at":start_at,"end_at":end_at,"base":base,"symbols":symbols}
    response = requests.request("GET", url, data=payload, headers="", params=querystring)
    dates = response.json()['rates'].keys()
    rates = []
    for i in range(len(dates)):
        rates.append(response.json()['rates'].values()[i].values()[0])
    df = pd.DataFrame({'day':dates,'exchange_rate':rates}).sort_values('day',ascending=False).reset_index(drop=True)
    df['day'] = pd.to_datetime(df['day'])
    return df
