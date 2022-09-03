import pandas as pd

df = pd.read_csv('CSV_files/Stats.csv')

for i in range(0, 322):
    Pitches = float(df.iat[i, 3])
    Swing_pct = float(df.iat[i, 4])
    Contact_pct = float(df.iat[i, 5])
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = float(df.iat[i, 6])
    FB = float(df.iat[i, 7])
    LD = float(df.iat[i, 8])
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/Stats.csv')


