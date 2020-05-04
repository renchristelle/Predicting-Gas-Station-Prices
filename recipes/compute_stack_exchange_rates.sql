SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "dataiku_all"."PREDICTINGGASSTATIONPRICES_add_exchange_rates"
UNION ALL
SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "dataiku_all"."PREDICTINGGASSTATIONPRICES_exchange_rates_prepared"