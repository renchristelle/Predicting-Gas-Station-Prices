library(dataiku)
library(dplyr, warn.conflicts = FALSE)

mydataset <- dkuReadDataset("gas_prices_brazil_filtered", samplingMethod="head", nbRows=100000)
grouped <- mydataset %>% group_by(date_start)

grouped <- grouped %>% summarise(
  baseline = mean(mean_distribution_price)
)

# Recipe outputs
dkuWriteDataset(grouped,"avg_mdp")
