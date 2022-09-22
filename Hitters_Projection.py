import pandas as pd
import pickle
from sklearn.preprocessing import PolynomialFeatures

full_df = pd.read_csv('CSV_files/Stats.csv')
every_df = pd.read_csv('xStats.csv')

def K_BB_projection(selected_stats, target_stat, type, total_stat):

    filename = f'Best_Models/{target_stat}.pkl'

    if type == "P" or type == "Poly":
        poly = PolynomialFeatures(degree=2)
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict(poly.fit_transform([columns.loc[pid]]))  # feed in required data
            expected_stat = round(predict[0], 3)
            total = round(full_df.at[pid, 'PA'] * expected_stat, 0)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.at[i, f"x{total_stat}"] = total
            every_df.to_csv('xStats.csv', index=None)

    elif type == "L" or type == "Linear":
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict([columns.loc[pid]])  # feed in required data
            expected_stat = round(predict[0], 3)
            total = round(full_df.at[pid, 'PA'] * expected_stat, 0)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.at[i, f"x{total_stat}"] = total
            every_df.to_csv('xStats.csv', index=None)

def BABIP_ISO_projection(selected_stats, target_stat, type):

    filename = f'Best_Models/{target_stat}.pkl'

    if type == "P" or type == "Poly":
        poly = PolynomialFeatures(degree=2)
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict(poly.fit_transform([columns.loc[pid]]))  # feed in required data
            expected_stat = round(predict[0], 3)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.to_csv('xStats.csv', index=None)

    elif type == "L" or type == "Linear":
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict([columns.loc[pid]])  # feed in required data
            expected_stat = round(predict[0], 3)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.to_csv('xStats.csv', index=None)

def HR_projection(selected_stats, target_stat, type, total_stat):

    filename = f'Best_Models/{target_stat}.pkl'

    if type == "P" or type == "Poly":
        poly = PolynomialFeatures(degree=2)
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict(poly.fit_transform([columns.loc[pid]]))  # feed in required data
            expected_stat = round(predict[0], 3)
            total = round(full_df.at[pid, 'PA'] * (expected_stat/10), 0)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.at[i, f"x{total_stat}"] = total
            every_df.to_csv('xStats.csv', index=None)

    elif type == "L" or type == "Linear":
        model = pickle.load(open(filename, 'rb'))
        columns = full_df.loc[:, selected_stats]
        for i in range(0, full_df.shape[0]):  # iterate thru all players, shape[0]: the row count of df
            pid = full_df.iat[i, 0]
            predict = model.predict([columns.loc[pid]])  # feed in required data
            expected_stat = round(predict[0], 3)
            total = round(full_df.at[pid, 'PA'] * (expected_stat/10), 0)
            every_df.at[i, f"x{target_stat}"] = expected_stat
            every_df.at[i, f"x{total_stat}"] = total
            every_df.to_csv('xStats.csv', index=None)

#K%
def K_proj():
    selected_stats = ["O-Swing%","O-Contact%","Z-Swing%","Z-Contact%","Zone%","F-Strike%","SwStr%","CSW%","M-Swing%","Meat%","Edge%","Fair/Foul ratio"]
    target_stat = "K%"
    selected_stats = list(selected_stats)
    K_BB_projection(
        selected_stats = selected_stats,
        target_stat = target_stat,
        type = "Poly",
        total_stat = "K"
    )

#BB%
def BB_proj():
    selected_stats = ["O-Swing%","O-Contact%","Z-Swing%","Z-Contact%","Zone%","F-Strike%","SwStr%","CSW%","Fair/Foul ratio"]
    target_stat = "BB%"
    selected_stats = list(selected_stats)
    K_BB_projection(
        selected_stats = selected_stats,
        target_stat = target_stat,
        type = "Poly",
        total_stat = "BB"
    )

#BABIP
def BABIP_proj():
    selected_stats = ["LD%","GB%","FB%","SweetSpot%","Barrel%","HardHit%","Cent%","Oppo%","Spd","LDFB_EV"]
    target_stat = "BABIP"
    selected_stats = list(selected_stats)
    BABIP_ISO_projection(
        selected_stats = selected_stats,
        target_stat = target_stat,
        type = "Linear",
    )

#HR%
def HR_proj():
    selected_stats = ["LA","FB%","LD%","HR/FB","Pull%","Barrel%","HardHit%","LDFB_EV"]
    target_stat = "HR%"
    selected_stats = list(selected_stats)
    HR_projection(
        selected_stats = selected_stats,
        target_stat = target_stat,
        type = "Poly",
        total_stat = "HR"
    )

#ISO
def ISO_proj():
    selected_stats = ["FB%","GB%","LD%","SweetSpot%","Barrel%","HardHit%","LDFB_EV","Pull%","Cent%","Oppo%"]
    target_stat = "ISO"
    selected_stats = list(selected_stats)
    BABIP_ISO_projection(
        selected_stats = selected_stats,
        target_stat = target_stat,
        type = "Linear",
    )

K_proj()
BB_proj()
BABIP_proj()
HR_proj()
ISO_proj()

def hitter_projections():
    for i in range(0, full_df.shape[0]):
        plate_appearance = every_df.at[i, 'PA']
        at_bat = every_df.at[i, 'AB']
        hbp = every_df.at[i, 'HBP']
        sf = every_df.at[i, 'SF']
        k = every_df.at[i, 'xK']
        bb = every_df.at[i, 'xBB']
        hr = every_df.at[i, 'xHR']
        babip = every_df.at[i, 'xBABIP']
        iso = every_df.at[i, 'xISO']
        Events = plate_appearance-hbp-sf-k-bb
        BIP = Events-hr
        xHits = round(BIP*babip + hr)
        xAVG = round(xHits/at_bat, 3)
        xOBP = round((xHits+bb+hbp)/(at_bat+bb+hbp+sf), 3)
        xSLG = xAVG + iso
        xOPS = xOBP + xSLG
        AVG = every_df.at[i, 'AVG']
        OPS = every_df.at[i, 'OPS']
        HR = every_df.at[i, 'HR']
        every_df.at[i, "xEvents"] = Events
        every_df.at[i, "xBIP"] = BIP
        every_df.at[i, "xH"] = xHits
        every_df.at[i, "xAVG"] = xAVG
        every_df.at[i, "xOBP"] = xOBP
        every_df.at[i, "xSLG"] = xSLG
        every_df.at[i, "xOPS"] = xOPS
        every_df.at[i, "AVG-xAVG"] = AVG-xAVG
        every_df.at[i, "OPS-xOPS"] = OPS-xOPS
        every_df.at[i, "HR-xHR"] = HR-hr
        every_df.to_csv('xStats.csv', index=None)
hitter_projections()

