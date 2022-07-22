import numpy
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

df = pd.read_csv('CSV_files/K%_testing.csv')

# for i in range(0, 1450): #1450
#     Pitches = float(df.iat[i, 15])
#     Swing_pct = float(df.iat[i, 16])
#     Contact_pct = float(df.iat[i, 17])
#     Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
#     GB = float(df.iat[i, 18])
#     FB = float(df.iat[i, 19])
#     LD = float(df.iat[i, 20])
#     Events = GB+FB+LD
#     Fouls = Contacted_Balls-Events
#     Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
#     print (Fair_Foul_ratio)
#     df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
#     df.to_csv('CSV_files/K%.csv')

X = df[["O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "Fair/Foul ratio"]]
y = df["K%"]
poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(X)
poly.fit(X_poly, y)
regr = linear_model.LinearRegression()
regr.fit(X_poly, y)

total_deviation = 0
for i in range(0, 135): # iterate thru all players
    predictK = regr.predict(poly.fit_transform([df.iloc[i][7:16]])) # feed in required data
    xK = round(predictK[0]*100,3)
    K = round(df.at[i,'K%']*100,2)
    deviation = round((xK-K),3) # the difference between x and real rate
    deviation_r = round((xK-K)/K*100,3) # the percentage of deviation (deviation value/real stat)
    #MSE = mean_squared_error(K, predictK)
    print(f"Player: {df.at[i,'Season']} {df.at[i,'Name']} xK%: {xK}%  K%: {K}%  Deviation: {deviation}%  Deviation%: {deviation_r}%")
    if deviation >= 0:
        total_deviation += deviation
    else:
        total_deviation += deviation*(-1)

average_deviation = total_deviation/135
print (f"Average Deviation: {average_deviation}%")

# d = {}
# linear_regr_testing_df = pd.DataFrame(data=d,columns=["Season","Name","xK%","K%","Deviation","Deviation%"])
# print(linear_regr_testing_df)
# for i in range(0,135):
#     predictK = regr.predict([df.iloc[i][7:16]]) # feed in required data
#     xK = round(predictK[0]*100,3)
#     K = round(df.at[i,'K%']*100,2)
#     deviation = round((xK-K),3) # the difference between x and real rate
#     deviation_r = round((xK-K)/K*100,3) # the percentage of deviation (deviation value/real stat)
#     row = [df.at[i,'Season'],df.at[i,'Name'],xK,K,deviation,deviation_r]
#     linear_regr_testing_df.loc[i]=row
# print(linear_regr_testing_df)
# linear_regr_testing_df.to_csv("linear_regr_testing_result.csv")