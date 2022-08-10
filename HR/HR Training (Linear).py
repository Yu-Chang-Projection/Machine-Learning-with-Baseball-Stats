import pandas as pd
import numpy as np
import tensorflow as tf
from math import sqrt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle

# functions
def save_model(regr):
    filename = '../Best_Models/Linear_HR_(15).pkl'
    pickle.dump(regr, open(filename, 'wb'))  # Save the model

prev_R2 = 0.75
full_df = pd.read_csv('../CSV_files/HR_data.csv')
result_df = pd.DataFrame(data={}, columns=["MAE", "RMSE", "R2"])
for j in range(30):
    train_df, test_df = train_test_split(full_df, test_size=0.15)
    X = train_df[["FB%", "LD%", "HR/FB", "Pull%", "Barrel%", "HardHit%"]]
    y = train_df["HR%"]
    regr = linear_model.LinearRegression()
    regr.fit(X.values, y)
    regr_df = pd.DataFrame(data={}, columns=["Season", "Name", "xHR%", "HR%"])
    for i in range(0, test_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
        predictHR = regr.predict([test_df.iloc[i][7:13]])  # feed in required data
        pid = test_df.iat[i, 0]
        xHR = round(predictHR[0]*10,3)
        HR = round(test_df.at[pid, 'HR%']*10,2)
        row = [test_df.at[pid, 'Season'], test_df.at[pid, 'Name'], xHR, HR]
        regr_df.loc[pid] = row

    HR_list, xHR_list = regr_df["HR%"].to_list(), regr_df["xHR%"].to_list()
    RMSE = sqrt(mean_squared_error(HR_list, xHR_list))
    MAE = mean_absolute_error(HR_list, xHR_list)
    R2 = r2_score(HR_list, xHR_list)
    result_row = [MAE, RMSE, R2]
    result_df.loc[j] = result_row
    if R2 > prev_R2:
        save_model(regr)
        print(R2)
        prev_R2 = R2
        regr_df.to_csv("Linear_every.csv")

print(result_df)
result_df.to_csv("Linear_HR.csv")