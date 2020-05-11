import numpy as np
import pandas as pd
#import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as seabornInstance 

columns=["date","site","SO2","CO","CO2","O3","PM10","PM25","Nox","NO","NO2","THC","NMHC","CH4"]
dalidf = pd.read_csv(r"D:/Data/中部日測值/dali_all_2019.csv",
                  index_col=[0], parse_dates=[0],names=columns)

dalidf=dalidf.drop(['date'])
dalidf

print(dalidf.info())
for i in ["SO2","CO","CO2","O3","PM10","PM25","Nox","NO","NO2","THC","NMHC","CH4"]:
    dalidf[[i]]=(dalidf[[i]]).astype(float)
print(dalidf.info())

f, ax = plt.subplots(figsize=(16, 9),dpi=256)

sns.heatmap(dalidf.corr(),annot=True, cmap="Reds")