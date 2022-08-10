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
    filename = '../Best_Models/Linear_BA_(15).pkl'
    pickle.dump(regr, open(filename, 'wb'))  # Save the model

prev_R2 = 0.5
full_df = pd.read_csv('../CSV_files/BA_data.csv')
result_df = pd.DataFrame(data={}, columns=["MAE", "RMSE", "R2"])
for j in range(20):
    train_df, test_df = train_test_split(full_df, test_size=0.15)
    X = train_df[["LD%","GB%","FB%","IFFB%","SweetSpot%","Barrel%","HardHit%"]]
    y = train_df["BABIP"]
    regr = linear_model.LinearRegression()
    regr.fit(X.values, y)

    regr_df = pd.DataFrame(data={}, columns=["Season", "Name", "xBABIP", "BABIP"])
    for i in range(0, test_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
        predictBA = regr.predict([test_df.iloc[i][9:16]])  # feed in required data
        pid = test_df.iat[i, 0]
        xBA = round(predictBA[0], 3)
        BA = round(test_df.at[pid, 'BABIP'], 3)
        row = [test_df.at[pid, 'Season'], test_df.at[pid, 'Name'], xBA, BA]
        regr_df.loc[pid] = row

    BA_list, xBA_list = regr_df["BABIP"].to_list(), regr_df["xBABIP"].to_list()
    RMSE = sqrt(mean_squared_error(BA_list, xBA_list))
    MAE = mean_absolute_error(BA_list, xBA_list)
    R2 = r2_score(BA_list, xBA_list)
    result_row = [MAE, RMSE, R2]
    result_df.loc[j] = result_row
    if R2 > prev_R2:
        save_model(regr)
        print(R2)
        prev_R2 = R2
        regr_df.to_csv("Linear_every.csv")

print(result_df)
result_df.to_csv("Linear_BA.csv")