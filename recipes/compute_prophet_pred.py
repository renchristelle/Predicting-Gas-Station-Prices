# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
# Python
import pandas as pd
from dateutil.easter import easter
from fbprophet import Prophet
import datetime

# Read recipe inputs
historical_mod = dataiku.Dataset("historical_mod")
his_df = historical_mod.get_dataframe()
his_df = his_df[['date_start','mean_distribution_price']].rename(columns={'date_start':'ds','mean_distribution_price':'y'})

to_predict_mod = dataiku.Dataset("to_predict_mod")
fut_df = to_predict_mod.get_dataframe()
fut_df = fut_df[['date_start','mean_distribution_price']].rename(columns={'date_start':'ds','mean_distribution_price':'y'})

real = dataiku.Dataset("to_predict_mod")
real_df = to_predict_mod.get_dataframe()
real_df = real_df[['date_start','mean_distribution_price']]

m = Prophet()
m.fit(his_df)

future = m.make_future_dataframe(periods=25,freq='W')

forecast = m.predict(future)
forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(25)
forecast = forecast.rename(columns={'ds':'date_start','yhat':'forecast_MDP_prophet'})[['date_start','forecast_MDP_prophet']]

his_df = his_df.rename(columns={'ds':'date_start','y':'real_MDP'})

prophet_pred_df = pd.concat([forecast,his_df]).reset_index(drop=True)

prophet_pred_df = prophet_pred_df.merge(real_df, how='left')

prophet_pred_df['date_start'] = pd.to_datetime(prophet_pred_df['date_start'])
prophet_pred_df = prophet_pred_df.sort_values('date_start')

prophet_pred_df['date_start'] = prophet_pred_df['date_start'] + datetime.timedelta(days=1)

# Write recipe outputs
prophet_pred = dataiku.Dataset("prophet_pred")
prophet_pred.write_with_schema(prophet_pred_df)