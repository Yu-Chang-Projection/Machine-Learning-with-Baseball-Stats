import pandas as pd

df = pd.read_csv('CSV_files/Stats.csv')

for i in range(0, df.shape[0]):
    Pitches = df.at[i, 'Pitches']
    Swing_pct = df.iat[i, 'Swing%']
    Contact_pct = df.iat[i, 'Contact%']
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = df.iat[i, 'GB']
    FB = df.iat[i, 'FB']
    LD = df.iat[i, 'LD']
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[i, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/Stats.csv')


