import pandas as pd
import numpy as np
import tensorflow as tf
from keras import Model
from keras import Sequential
from keras.optimizers import Adam
from keras.layers import Dense, Dropout
from keras.losses import MeanAbsoluteError
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

K = 'K%'
full_data = pd.read_csv('CSV_files/K%_data(ML).csv')
# train_data, test_data = train_test_split(full_data, test_size=0.3)
X = full_data[["K%", "O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
# Y = test_data[["K%", "O-Swing%", "O-Contact%", "Z-Swing%", "Z-Contact%", "Zone%", "F-Strike%", "SwStr%", "CSW%", "M-Swing%", "Meat%", "Edge%", "Fair/Foul ratio"]]
x_train, y_train = X.drop(K, axis=1), full_data[K]
# x_test, y_test = Y.drop(K, axis=1), test_data[K]

def scale_datasets(x_train):
    standard_scaler = StandardScaler()
    x_train_scaled = pd.DataFrame(
        standard_scaler.fit_transform(x_train),
        columns = x_train.columns
    )
    # x_test_scaled = pd.DataFrame(
    #     standard_scaler.fit_transform(x_test),
    #     columns=x_test.columns
    # )
    return x_train_scaled
x_train_scaled = scale_datasets(x_train)

def build_model():
    model = Sequential([
        Dense(49, kernel_initializer='normal', activation='relu'), Dropout(0.2),
        Dense(49, kernel_initializer='normal', activation='relu'), Dropout(0.2),
        Dense(49, kernel_initializer='normal', activation='relu'),
        Dense(1, kernel_initializer='normal', activation='sigmoid')
    ])
    return model

model = build_model()

mae = MeanAbsoluteError()
checkpoint = ModelCheckpoint('Best_Models/ML_(30).h5',monitor='val_loss',mode='min',save_best_only=True,verbose=1)
earlystop = EarlyStopping(monitor='val_loss',min_delta=0,patience=5,verbose=1,restore_best_weights=True)
# reduce_lr = ReduceLROnPlateau(monitor='val_loss',factor=0.2,patience=5,verbose=1,min_delta=0.01)
callbacks = [checkpoint, earlystop]

model.compile(loss = 'mean_absolute_error', optimizer = Adam(learning_rate=0.002), metrics=[mae]) #lr=0.001
history = model.fit(x_train_scaled.values,y_train.values,epochs=20,batch_size=8,validation_split=0.10,callbacks=callbacks)