import pandas as pd
rawDF = pd.read_csv("~/BusDataAnalytics/data/rt_leavetimes_DB_2018.txt", delimiter = ";")
sampleDF = rawDF.sample(frac=0.05)
sampleDF.to_csv("leavetimesRandomSample.csv", sep = ",")