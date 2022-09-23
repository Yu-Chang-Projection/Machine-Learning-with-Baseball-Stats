import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle
from sklearn.preprocessing import PolynomialFeatures

# functions
def training_function(selected_stats, target_stat, type, test_size, prev_R2 = 0.99, loops = 100):

    def save_model(regr):
        filename = f'../Best_Models/{target_stat}_best.pkl'
        pickle.dump(regr, open(filename, 'wb'))  # Save the model

    # create Dataframes
    full_df = pd.read_csv(f'../CSV_files/{target_stat}_data.csv')
    result_df = pd.DataFrame(data={}, columns=["MAE", "RMSE", "R2"])

    # main loop
    for j in range(loops):
        train_df, test_df = train_test_split(full_df, test_size = test_size)
        X = train_df[selected_stats]
        y = train_df[target_stat]

        # run different regr according to Parameters
        regr = None
        if type == "P" or type == "Poly":
            poly = PolynomialFeatures(degree=2)
            X_poly = poly.fit_transform(X)
            regr = linear_model.LinearRegression()
            regr.fit(X_poly, y)
            columns = test_df.loc[:, selected_stats]
            regr_df = pd.DataFrame(data={}, columns=["Season", "Name", f"x{target_stat}", target_stat])
            for i in range(0, test_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
                pid = test_df.iat[i, 0]
                predict = regr.predict(poly.fit_transform([columns.loc[pid]]))  # feed in required data
                expected_stat = round(predict[0], 3)
                real_stat = round(test_df.at[pid, target_stat], 3)
                row = [test_df.at[pid, 'Season'], test_df.at[pid, 'Name'], expected_stat, real_stat]
                regr_df.loc[pid] = row

        elif type == "L" or type == "Linear":
            regr = linear_model.LinearRegression()
            regr.fit(X.values, y)
            columns = test_df.loc[:, selected_stats]
            regr_df = pd.DataFrame(data={}, columns=["Season", "Name", f"x{target_stat}", target_stat])
            for i in range(0, test_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
                pid = test_df.iat[i, 0]
                predict = regr.predict([columns.loc[pid]])  # feed in required data
                expected_stat = round(predict[0], 3)
                real_stat = round(test_df.at[pid, target_stat], 3)
                row = [test_df.at[pid, 'Season'], test_df.at[pid, 'Name'], expected_stat, real_stat]
                regr_df.loc[pid] = row

        real_list, x_list = regr_df[target_stat].to_list(), regr_df[f"x{target_stat}"].to_list()
        RMSE = sqrt(mean_squared_error(real_list, x_list))
        MAE = mean_absolute_error(real_list, x_list)
        R2 = r2_score(real_list, x_list)
        result_row = [MAE, RMSE, R2]
        result_df.loc[j] = result_row
        if R2 > prev_R2:
            save_model(regr)
            prev_R2 = R2
            regr_df.to_csv(f"{type}_every_player_{target_stat}.csv")

    print (test_size)
    print(f"MAX R2: {max(result_df['R2'].to_list())}", f"AVG R2: {sum(result_df['R2'].to_list())/loops}", f"MAE: {sum(result_df['MAE'].to_list())/loops}")