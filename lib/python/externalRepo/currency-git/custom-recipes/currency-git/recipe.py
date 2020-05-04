import dataiku
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import requests
from pandas.io.json import json_normalize

from dataiku.customrecipe import *

# For outputs, the process is the same:
output = get_output_names_for_role('main_output')[0]

start_date = get_recipe_config()['start_date']
end_date = get_recipe_config()['end_date']

# parsing date
start_date = start_date.split('T')[0]
end_date = end_date.split('T')[0]

currency_base = get_recipe_config()['currency_base']
currency_to = get_recipe_config()['currency_to']

# output using the core code
url = "https://api.exchangeratesapi.io/history"

querystring = {"start_at":start_date,"end_at":end_date,"base":currency_base,"symbols":currency_to}

print('QUERY ----', querystring)

payload = ""
headers = ""

response = requests.request("GET", url, data=payload, headers="", params=querystring)

dates = response.json()['rates'].keys()
rates = []

currency_from = querystring['base']
currency_to = querystring['symbols']

for i in range(len(dates)):
    rates.append(response.json()['rates'].values()[i].values()[0])

df = pd.DataFrame({'day':dates,'exchange_rate_%s_to_%s'%(currency_from,currency_to):rates}).sort_values('day',ascending=False).reset_index(drop=True)

df['day'] = pd.to_datetime(df['day'])

# Write recipe outputs
add_exchange_rates = dataiku.Dataset(output)
add_exchange_rates.write_with_schema(df)