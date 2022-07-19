import pandas as pd

# file name: /Users/ywchang/Desktop/Baseball Project/Class/All.csv
# division: file_avg = file.sum().div(4).round
# specific values: file.iat[i, j], i:row
# write into a CSV file: player.to_csv('')
file = pd.read_csv('/Users/ywchang/Desktop/Baseball Project/Class/All.csv', header=0) #import the CSV file into the pandas dataframe
for i in range(0, 23):
    Name = file.iat[i, 0]
    AVG = file.iat[i, 4]
    BB_percent = file.iat[i, 5]
    PWR = file.iat[i, 6]
    HR = file.iat[i, 8]
    SB = file.iat[i, 10]
    if (AVG >= 0.254 and BB_percent >= 0.1 and PWR >= 0.190 and HR >= 35 and SB >= 12):
        print (Name, "is a Certified 5 tool player")
        #ft = {
            #'Name': [Name]
        #}
        #Five_tool = pd.DataFrame(ft)
        #Five_tool.to_csv('C:/Users/eda/Desktop/Class/5_tool.csv', mode='a', index=False, header=False)
    elif (AVG >= 0.253 and BB_percent >= 0.0823 and PWR >= 0.195 and HR >= 34 and SB <= 12):
        print (Name, "is a David Ortiz type player")
        #do = {
            #'Name': [Name]
        #}
        #David_Ortiz = pd.DataFrame(do)
        #David_Ortiz.to_csv('C:/Users/eda/Desktop/Class/David_Ortiz.csv', mode='a', index=False, header=False)
    elif (AVG <= 0.246 and BB_percent >= 0.093 and PWR >= 0.18 and HR >= 33):
        print (Name, "is a Joey Gallo type player")
        #jg = {
            #'Name': [Name]
        #}
        #Joey_Gallo = pd.DataFrame(jg)
        #Joey_Gallo.to_csv('C:/Users/eda/Desktop/Class/Joey_Gallo.csv', mode='a', index=False, header=False)
    elif (AVG >= 0.262 and BB_percent <= 0.085 and PWR >= 0.18 and HR >= 33):
        print (Name, "is a Bo Bichette type player")
        #bo = {
            #'Name': [Name]
        #}
        #Bo_Bichette = pd.DataFrame(bo)
        #Bo_Bichette.to_csv('C:/Users/eda/Desktop/Class/Bo_Bichette.csv', mode='a', index=False, header=False)
    elif (AVG <= 0.265 and AVG >= .246 and BB_percent <= 0.084 and PWR >= 0.195 and HR >= 33):
        print (Name, "is a Javy Baez type player")
        #jb = {
            #'Name': [Name]
        #}
        #Javy_Baez = pd.DataFrame(jb)
        #Javy_Baez.to_csv('C:/Users/eda/Desktop/Class/Javy_Baez.csv', mode='a', index=False, header=False)
    elif (AVG <= 0.246 and BB_percent <= 0.087 and PWR >= 0.185 and HR >= 33):
        print (Name, "is a Bobby Dalbec type player")
        #bd = {
            #'Name': [Name]
        #}
        #Bobby_Dalbec = pd.DataFrame(bd)
        #Bobby_Dalbec.to_csv('C:/Users/eda/Desktop/Class/Bobby_Dalbec.csv', mode='a', index=False, header=False)
    elif (AVG <= 0.266 and AVG >= .23 and BB_percent >= 0.061 and PWR <= 0.195 and PWR >= 0.160 and HR <= 34 and  HR >= 20 and SB >= 5):
        print (Name, "is a Swiss Army Knife player")
        #sak = {
            #'Name': [Name]
         #}
        #SAK = pd.DataFrame(sak)
        #SAK.to_csv('C:/Users/eda/Desktop/Class/Swiss_Army_Knife.csv', mode='a', index=False, header=False)
    elif (AVG >= .265 and BB_percent >= 0.062 and PWR >= 0.157 and HR <= 32):
        print (Name, "is a Wander Franco type player")
        #wf = {
            #'Name': [Name]
        # }
        #Wander_Franco = pd.DataFrame(wf)
        #Wander_Franco.to_csv('C:/Users/eda/Desktop/Class/Wander_Franco.csv', mode='a', index=False, header=False)
    elif (AVG >= .20 and BB_percent >= 0.048 and BB_percent <= 0.085 and PWR <= 0.160 and HR <= 25 and SB >= 20):
        print (Name, "is a Billy Hamilton type player")
        #bh = {
         #'Name': [Name]
        #}
        #Billy_Hamilton = pd.DataFrame(bh)
        #Billy_Hamilton.to_csv('C:/Users/eda/Desktop/Class/Billy_Hamilton.csv', mode='a', index=False, header=False)
    elif (AVG >= .255 and BB_percent <= 0.08 and PWR <= 0.160 and HR <= 25 and SB <= 20):
        print (Name, "is a David Fletcher type player")
        #df = {
            #'Name': [Name]
        #}
        #David_Fletcher = pd.DataFrame(df)
        #David_Fletcher.to_csv('C:/Users/eda/Desktop/Class/David_Fletcher.csv', mode='a', index=False, header=False)
    elif (AVG >= .24 and BB_percent >= 0.081 and PWR <= 0.160 and HR <= 25):
        print (Name, "is a Tony Kemp type player")
        #tk = {
            #'Name': [Name]
        #}
        #Tony_Kemp = pd.DataFrame(tk)
        #Tony_Kemp.to_csv('C:/Users/eda/Desktop/Class/Tony_Kemp.csv', mode='a', index=False, header=False)
    else:
        print (Name, ": Others")
        #others = {
            #'Name': [Name]
        #}
        #Others = pd.DataFrame(others)
        #Others.to_csv('C:/Users/eda/Desktop/Class/Others.csv', mode='a', index=False, header=False)

