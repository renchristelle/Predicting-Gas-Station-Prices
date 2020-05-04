# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
from pandas.io.json import json_normalize

# output using the shared function: rate_per_day()
# global shared code module
# from exchangeRate import rate_per_day
# df = rate_per_day("2017-08-26","2019-06-23","USD","BRL")

# output using the function from the github repository: rate_per_day()
# global shared code git module
# from externalRepo import exchangeRate
# df = exchangeRate.rate_per_day("2017-08-26","2019-06-23","USD","BRL")

# output using the core code
url = "https://api.exchangeratesapi.io/history"

# add comment for demo purposes

querystring = {"start_at":"2017-08-26","end_at":"2019-06-24","base":"USD","symbols":"BRL"}

payload = ""
headers = ""

response = requests.request("GET", url, data=payload, headers="", params=querystring)

dates = response.json()['rates'].keys()
rates = []
for i in range(len(dates)):
    rates.append(response.json()['rates'].values()[i].values()[0])

df = pd.DataFrame({'day':dates,'exchange_rate':rates}).sort_values('day',ascending=False).reset_index(drop=True)

df['day'] = pd.to_datetime(df['day'])


# Write recipe outputs
add_exchange_rates = dataiku.Dataset("add_exchange_rates")
add_exchange_rates.write_with_schema(df)