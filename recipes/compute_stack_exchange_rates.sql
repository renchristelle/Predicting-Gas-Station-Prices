SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "PREDICTINGGASSTATIONPRICESBRAZIL_add_exchange_rates"
UNION ALL
SELECT 
    "day" AS "day",
    "exchange_rate" AS "exchange_rate"
  FROM "PREDICTINGGASSTATIONPRICESBRAZIL_stack_exchange_rates"