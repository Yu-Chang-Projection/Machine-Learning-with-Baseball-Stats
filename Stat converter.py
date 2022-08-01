import pandas as pd

df = pd.read_csv('CSV_files/BA_data.csv')

# for i in range(0, 2047): #1450
#     Pitches = float(df.iat[i, 15])
#     Swing_pct = float(df.iat[i, 16])
#     Contact_pct = float(df.iat[i, 17])
#     Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
#     GB = float(df.iat[i, 18])
#     FB = float(df.iat[i, 19])
#     LD = float(df.iat[i, 20])
#     Events = GB+FB+LD
#     Fouls = Contacted_Balls-Events
#     Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
#     print (Fair_Foul_ratio)
#     df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
#     df.to_csv('CSV_files/BB%_data.csv')

for i in range(0, 1239): #1450
    PA = float(df.iat[i, 5])
    H = float(df.iat[i, 6])
    Hits_Per_PA = H/PA
    print (Hits_Per_PA)
    df.at[i, "H_PA"] = Hits_Per_PA
    df.to_csv('CSV_files/BA_data.csv')

