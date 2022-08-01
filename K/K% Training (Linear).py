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
    filename = 'best_model.pkl'
    pickle.dump(regr, open(filename, 'wb'))  # Save the model

prev_RMSE = 100
full_df = pd.read_csv('CSV_files/K%_data.csv')
result_df = pd.DataFrame(data={}, columns=["MAE", "RMSE", "R2"])
for j in range(50):
    train_df, test_df = train_test_split(full_df, test_size=0.15)
    X = train_df[["O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
    y = train_df["K%"]
    regr = linear_model.LinearRegression()
    regr.fit(X.values, y)

    regr_df = pd.DataFrame(data={}, columns=["Season", "Name", "xK%", "K%"])
    for i in range(0, test_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
        predictK = regr.predict([test_df.iloc[i][7:16]])  # feed in required data
        pid = test_df.iat[i, 0]
        xK = round(predictK[0] * 100, 3)
        K = round(test_df.at[pid, 'K%'] * 100, 2)
        row = [test_df.at[pid, 'Season'], test_df.at[pid, 'Name'], xK, K]
        regr_df.loc[pid] = row

    K_list, xK_list = regr_df["K%"].to_list(), regr_df["xK%"].to_list()
    RMSE = sqrt(mean_squared_error(K_list, xK_list))
    MAE = mean_absolute_error(K_list, xK_list)
    R2 = r2_score(K_list, xK_list)
    result_row = [MAE, RMSE, R2]
    result_df.loc[j] = result_row
    if RMSE < prev_RMSE:
        save_model(regr)
        print(RMSE)
        prev_RMSE = RMSE

print(result_df)
result_df.to_csv("result")
