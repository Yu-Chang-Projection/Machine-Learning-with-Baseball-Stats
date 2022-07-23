import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

train_df = pd.read_excel('CSV_files/K_savant.xlsx', sheet_name='Training')
df = pd.read_excel('CSV_files/K_savant.xlsx', sheet_name='Testing')

X = train_df[["O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%","Fair/Foul ratio"]]
y = train_df["K%"]
regr = linear_model.LinearRegression()
regr.fit(X.values, y)

p = 170
total_deviation = 0
regr_df = pd.DataFrame(data={},columns=["Season","Name","xK%","K%","Deviation","Deviation%"])
for i in range(0, p): # iterate thru all players
    predictK = regr.predict([df.iloc[i][7:19]]) # feed in required data
    xK = round(predictK[0]*100,3)
    K = round(df.at[i,'K%']*100,2)
    deviation = round((xK-K),3) # the difference between x and real rate
    deviation_r = round((xK-K)/K*100,3) # the percentage of deviation (deviation value/real stat)
    row = [df.at[i,'Season'],df.at[i,'Name'],xK,K,deviation,deviation_r]
    regr_df.loc[i] = row
    total_deviation = total_deviation + deviation if deviation >= 0 else total_deviation - deviation

average_deviation = total_deviation/p
K_list, xK_list = regr_df["K%"].to_list(),regr_df["xK%"].to_list()
MSE = mean_squared_error(K_list, xK_list)
R2 = r2_score(K_list, xK_list)
print (f"Average Deviation: {average_deviation}% MSE: {MSE}  R2: {R2}")
print(regr_df)
regr_df.to_csv("linear_testing.csv")