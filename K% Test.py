import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from math import sqrt

model = load_model('Best_Models/ML_(10).h5', compile=False)

k = 'K%'
test_data = pd.read_csv('CSV_files/ML_testing.csv')
Test = test_data[["K%", "O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
x_test, y_test = Test.drop(k, axis=1), test_data[k]

def scale_datasets(x_test):
    standard_scaler = StandardScaler()
    x_test_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_test),
        columns = x_test.columns
    )
    return x_test_scaled
x_test_scaled = scale_datasets(x_test)

x_test['prediction'] = model.predict(x_test_scaled)
regr_df = pd.DataFrame(data={},columns=["Season","Name","xK%","K%"])
result_df = pd.DataFrame(data={},columns=["MAE", "RMSE", "R2"])
for i in range(0, 38):
    xK = round(x_test['prediction'][i]*100, 3)
    K = round(test_data.iloc[i][6]*100, 3)
    row = [test_data.at[i, 'Season'], test_data.at[i, 'Name'], xK, K]
    regr_df.loc[i] = row
    print (f"K%: {K}%, xK%: {xK}")
K_list, xK_list = regr_df["K%"].to_list(), regr_df["xK%"].to_list()
MAE = mean_absolute_error(K_list, xK_list)
RMSE = sqrt(mean_squared_error(K_list, xK_list))
R2 = r2_score(K_list, xK_list)
result_row = [MAE, RMSE, R2]
result_df = result_row
print (result_df)