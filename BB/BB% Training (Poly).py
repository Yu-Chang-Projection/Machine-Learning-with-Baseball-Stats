import pandas as pd
import numpy as np
import tensorflow as tf
from math import sqrt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle

def save_model(regr):
    filename = '../Best_Models/Poly_BB_(20).pkl'
    pickle.dump(regr, open(filename, 'wb')) #Save the model

prev_RMSE = 10
full_df = pd.read_csv('../CSV_files/BB%_data.csv')
result_df = pd.DataFrame(data={},columns=["MAE", "RMSE", "R2"])
for j in range(0, 50):
    train_df, test_df = train_test_split(full_df, test_size=0.15)
    X = train_df[["O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "Fair/Foul ratio"]]
    y = train_df["BB%"]
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    regr = linear_model.LinearRegression()
    regr.fit(X_poly, y)

    regr_df = pd.DataFrame(data={},columns=["Season","Name","xBB%","BB%"])
    for i in range(0, test_df.shape[0]): # iterate thru all players
        predictBB = regr.predict(poly.fit_transform([test_df.iloc[i][7:16]])) # feed in required data
        pid = test_df.iat[i, 0]
        xBB = round(predictBB[0]*100,3)
        BB = round(test_df.at[pid,'BB%']*100,2)
        row = [test_df.at[pid,'Season'],test_df.at[pid,'Name'],xBB,BB]
        regr_df.loc[pid] = row

    BB_list, xBB_list = regr_df["BB%"].to_list(), regr_df["xBB%"].to_list()
    MAE = mean_absolute_error(BB_list, xBB_list)
    RMSE = sqrt(mean_squared_error(BB_list, xBB_list))
    R2 = r2_score(BB_list, xBB_list)
    result_row = [MAE, RMSE, R2]
    result_df.loc[j] = result_row
    if RMSE < prev_RMSE:
        save_model(regr)
        print(RMSE)
        prev_RMSE = RMSE

print (result_df)