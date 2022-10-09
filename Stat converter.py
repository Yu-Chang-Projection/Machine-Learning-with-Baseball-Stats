import pandas as pd

df = pd.read_csv('CSV_files/Stats.csv')

for i in range(0, df.shape[0]):
    pid = df.iat[i, 0]
    Pitches = df.at[pid, 'Pitches']
    Swing_pct = df.at[pid, 'Swing%']
    Contact_pct = df.at[pid, 'Contact%']
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = df.at[pid, 'GB']
    FB = df.at[pid, 'FB']
    LD = df.at[pid, 'LD']
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
    df.at[pid, "Fair/Foul ratio"] = Fair_Foul_ratio
    df.to_csv('CSV_files/Stats.csv')


