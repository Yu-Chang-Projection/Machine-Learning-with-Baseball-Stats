import pandas as pd
import numpy as np
from keras.models import load_model
from keras import Sequential
from keras.optimizers import Adam
from keras.layers import Dense, Dropout
from keras.losses import MeanAbsoluteError
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from math import sqrt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

K = 'K%'
full_data = pd.read_csv('CSV_files/K%_data(ML).csv')
test_data = pd.read_csv('CSV_files/ML_testing.csv')
X = full_data[["K%", "O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
Test = test_data[["K%", "O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
x_train, y_train = X.drop(K, axis=1), full_data[K]
x_test, y_test = Test.drop(K, axis=1), test_data[K]

def scale_datasets(x_train, x_test):
    standard_scaler = StandardScaler()
    x_train_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_train),
        columns = x_train.columns
    )
    standard_scaler = StandardScaler()
    x_test_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_test),
        columns=x_test.columns
    )
    return x_train_scaled, x_test_scaled
x_train_scaled, x_test_scaled = scale_datasets(x_train, x_test)

def build_model():
    model = Sequential([
        Dense(49, kernel_initializer='normal', activation='relu'), Dropout(0.1),
        Dense(64, kernel_initializer='normal', activation='relu'), Dropout(0.1),
        Dense(49, kernel_initializer='normal', activation='relu'),
        Dense(1, kernel_initializer='normal', activation='sigmoid')
    ])
    return model

model = build_model()

mae = MeanAbsoluteError()
checkpoint = ModelCheckpoint('Best_Models/ML_(10_2).h5',monitor='val_loss',mode='min',save_best_only=True,verbose=1)
earlystop = EarlyStopping(monitor='val_loss',min_delta=0,patience=7,verbose=1,restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss',factor=0.2,patience=5,verbose=1,min_delta=0.01)
callbacks = [checkpoint, earlystop]

model.compile(loss = 'mean_absolute_error', optimizer = Adam(learning_rate=0.003), metrics=[mae]) #lr=0.001
history = model.fit(x_train_scaled.values,y_train.values,epochs=30,batch_size=8,validation_split=0.10,callbacks=callbacks)

best_model = load_model('Best_Models/ML_(10_2).h5', compile=False)
x_test['prediction'] = best_model.predict(x_test_scaled)
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