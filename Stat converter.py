import pandas as pd

df = pd.read_csv('CSV_files/backup.csv')

for i in range(0, 311):
    Pitches = float(df.iat[i, 28])
    Swing_pct = float(df.iat[i, 29])
    Contact_pct = float(df.iat[i, 30])
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = float(df.iat[i, 31])
    FB = float(df.iat[i, 32])
    LD = float(df.iat[i, 33])
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/backup.csv')


