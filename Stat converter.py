import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


df = pd.read_csv('CSV_files/K%_training.csv')

for i in range(0, 1450): #1450
    Pitches = float(df.iat[i, 15])
    Swing_pct = float(df.iat[i, 16])
    Contact_pct = float(df.iat[i, 17])
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = float(df.iat[i, 18])
    FB = float(df.iat[i, 19])
    LD = float(df.iat[i, 20])
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/K%.csv')

