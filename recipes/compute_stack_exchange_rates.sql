SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "PREDICTINGGASSTATIONPRICES_add_exchange_rates"
UNION ALL
SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "PREDICTINGGASSTATIONPRICES_exchange_rates_prepared"