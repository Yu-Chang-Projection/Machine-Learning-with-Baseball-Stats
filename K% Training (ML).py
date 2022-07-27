import pandas as pd
import numpy as np
import tensorflow as tf
from keras import Model
from keras import Sequential
from keras.optimizers import Adam
from keras.layers import Dense, Dropout
from keras.losses import MeanSquaredError
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

# def save_model(regr):
#     filename = 'Best_Models/Poly_(10).pkl'
#     pickle.dump(regr, open(filename, 'wb')) #Save the model

K = 'K%'
full_data = pd.read_csv('CSV_files/K%_data(ML).csv')
train_data, test_data = train_test_split(full_data, test_size=0.3)
x_train, y_train = train_data.drop(K, axis=1), train_data[K]
x_test, y_test = test_data.drop(K, axis=1), test_data[K]

def scale_datasets(x_train, x_test):
    standard_scaler = StandardScaler()
    x_train_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_train),
        columns = x_train.columns
    )
    x_test_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_test),
        columns=x_test.columns
    )
    return x_train_scaled, x_test_scaled
x_train_scaled, x_test_scaled = scale_datasets(x_train, x_test)

#     regr_df = pd.DataFrame(data={},columns=["Season","Name","xK%","K%"])
#     for i in range(0, test_df.shape[0]): # iterate thru all players
#         predictK = regr.predict(poly.fit_transform([test_df.iloc[i][7:19]])) # feed in required data
#         pid = test_df.iat[i, 0]
#         xK = round(predictK[0]*100,3)
#         K = round(test_df.at[pid,'K%']*100,2)
#         row = [test_df.at[pid,'Season'],test_df.at[pid,'Name'],xK,K]
#         regr_df.loc[pid] = row
#
#     K_list, xK_list = regr_df["K%"].to_list(), regr_df["xK%"].to_list()
#     MAE = mean_absolute_error(K_list, xK_list)
#     RMSE = sqrt(mean_squared_error(K_list, xK_list))
#     R2 = r2_score(K_list, xK_list)
#     result_row = [MAE, RMSE, R2]
#     result_df.loc[j] = result_row
#     if RMSE < prev_RMSE:
#         save_model(regr)
#         print(RMSE)
#         prev_RMSE = RMSE
#
# print(result_df)
# result_df.to_csv("Poly_results.csv")