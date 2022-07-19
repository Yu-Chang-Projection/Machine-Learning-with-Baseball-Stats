import pandas as pd
import numpy as np
import tensorflow as tf
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from sklearn import linear_model

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
#fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
#for file1 in fileList:
  #print('title: %s, id: %s' % (file1['title'], file1['id']))

K_percent = drive.CreateFile({'id':'1nwMZF6Zh5f_O-fRENcmVBmC_QKHoQgFD'})
K_percent.GetContentFile('K%.csv')
df = pd.read_csv('K%.csv')
#print (df)

for i in range(0, 2):
    Pitches = float(df.iat[i, 14])
    Swing_pct = float(df.iat[i, 15])
    Contact_pct = float(df.iat[i, 16])
    Contacted_Balls = round(Pitches*Swing_pct*Contact_pct)
    GB = float(df.iat[i, 17])
    FB = float(df.iat[i, 18])
    LD = float(df.iat[i, 19])
    Events = GB+FB+LD
    Fouls = Contacted_Balls-Events
    Fair_Foul_ratio = (Events/Contacted_Balls)/(Fouls/Contacted_Balls)
    print (Fair_Foul_ratio)
FFR = {
    'Fair/Foul ratio': [Fair_Foul_ratio]
    }
Fair_Foul_r = pd.DataFrame(FFR)
Fair_Foul_r.to_csv('K%.csv', mode='a', index=False, header=False)


#X = df[[O-Swing%, O-Contact%, Z-Swing%, Z-Contact%, Zone%, F-Strike%, SwStr%, CSW%, Fair/Foul ratio]]
#Y = df[K%]