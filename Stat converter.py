import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures


df = pd.read_csv('CSV_files/K_savant.csv')

for i in range(850, 1238): #1450
    Pitches = float(df.iat[i, 19])
    Swing_pct = float(df.iat[i, 20])
    Contact_pct = float(df.iat[i, 21])
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = float(df.iat[i, 22])
    FB = float(df.iat[i, 23])
    LD = float(df.iat[i, 24])
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/K_savant.csv')

