import pandas as pd

file = "inventory_12.5.2022.csv"
file2 = "kochek 9.12.2022.csv"

d2_col = ("EX102", "EX1522", "EX1524", "EX1525", "EX152S", "EX2522", "EX2524", "EX252H", "RS05", "RS100", "RS1025", "RS110", "RS15",
                "RS175", "RS20", "RS2125", "RS225", "RS25", "RS275", "RS30", "RS3125", "RS34", "RS35", "RS38", "RS40", "RS45", "RS50", "RS55",
                "RS575", "RS60", "RS65", "RS70", "RS80", "RS85", "RS90", "SRS187", "TB35E", "TB40A", "TB425D", "TB45B", "TB45D", "TB50B",
                "TB55D", "TB575", "TB60D", "TB625D", "TB70D", "TB71A", "TB71F", "TB775D")

data = pd.read_csv(file, usecols= (0, 1, 3, 4, 6, 8))
data2 = pd.read_csv(file, usecols= (1, 3, 4))

kdata = pd.read_csv(file2)

kochek_frame = pd.DataFrame()

for column in data.columns:
    index = data.columns.get_loc(column)
    print(index, column)

for part in data:
    data["Partnumber"] = data["Partnumber"].str.replace('=', '')
    data["Partnumber"] = data["Partnumber"].str.replace('"', '')
    data["Description"] = data["Description"].str.replace('=', '')
    data["Description"] = data["Description"].str.replace('"', '')

for part in data2:
    data2["Description"] = data2["Description"].str.replace('=','')
    data2["Description"] = data2["Description"].str.replace('"','')

kochek_frame.index = d2_col

for (ind, row) in data.iterrows():
    EX102 = data.loc[data["Description"] == "6061-T6 (EX102) 1 RL 1.75 OD X .500 WA X 12' EXT"]
    EX1522 = data.loc[data["Description"] == "6061-T6 (EX1522) 1.5 RL 2.08 OD X .310 X 12' EXT"]
    EX1524 = data.loc[data["Description"] == "6061-T6 (EX1524) 1.5 RL 2.75 OD X .656 X 12' EXT"]
    EX1525 = data.loc[data["Description"] == "6061-T6 (EX1525) 1.5 RL 2.375 OD X .475 X 12' EXT"]
    EX152S = data.loc[data["Description"] == "6061-T6 (EX152S) 1.5 RL 2.45 OD SOLID X 12' EXT"]
    EX2522 = data.loc[data["Description"] == "6061-T6 (EX2522) 2.5 RL 3.530 OD X 1.040 X 12' EXT"]
    EX2524 = data.loc[data["Description"] == "6061-T6 (EX2524) 2.5 RL 3.625 OD x 12' EXT"]
    EX252H = data.loc[data["Description"] == "6061-T6 (EX252H) 2.5 RL X .593"]
    RS05 = data.loc[data["Description"] == '6061-T6511 Round Bar 1/2 x 144']
    RS100 = data.loc[data["Description"] == '6061-T6 Round Bar 10']
    RS1025 = data.loc[data["Description"] == '6061-T6511 Round Bar 1-1/4 x 144']
    RS110 = data.loc[data["Description"] == '6061-T6 Round Bar 11']
    RS15 = data.loc[data["Description"] == '6061-T6511 Round Bar 1-1/2 x 144']
    RS175 = data.loc[data["Description"] == '6061-T6511 Round Bar 1-3/4 x 144']
    RS20 = data.loc[data["Description"] == '6061-T651 CF Round Bar 2 x 144']
    RS2125 = data.loc[data["Description"] == '6061-T6511 Round Bar 2-1/8 x 144']
    RS225 = data.loc[data["Description"] == '6061-T6511 Round Bar 2-1/4 x 144']
    RS25 = data.loc[data["Description"] == '6061-T6511 Round Bar 2-1/2 x 144']
    RS275 = data.loc[data["Description"] == '6061-T6511 Round bar 2-3/4 x 144']
    RS30 = data.loc[data["Description"] == '6061-T6511 Round Bar 3 x 144']
    RS3125 = data.loc[data["Description"] == '6061-T6511 Round Bar 3-1/8 x 144']
    RS34 = data.loc[data["Description"] == '6061-T6511 Round Bar 3/4 x 144']
    RS35 = data.loc[data["Description"] == '6061-T6511 Round Bar 3-1/2 x 144']
    RS38 = data.loc[data["Description"] == '6061-T6511 Round Bar 3/8 x 144']
    RS40 = data.loc[data["Description"] == '6061-T6511 Round Bar 4 x 144']
    RS45 = data.loc[data["Description"] == '6061-T6511 Round Bar 4-1/2 x 144']
    RS50 = data.loc[data["Description"] == '6061-T6511 Round Bar 5 x 144']
    RS55 = data.loc[data["Description"] == '6061-T6511 Round Bar 5-1/2 x 144']
    RS575 = data.loc[data["Description"] == '6061-T6511 Round Bar 5-3/4 x 144']
    RS60 = data.loc[data["Description"] == '6061-T6511 Round Bar 6 x 144']
    RS65 = data.loc[data["Description"] == '6061-T6511 Round Bar 6-1/2 x 144']
    RS70 = data.loc[data["Description"] == '6061-T6511 Round Bar 7']
    RS80 = data.loc[data["Description"] == '6061-T6 Round Bar 8 x 144']
    RS85 = data.loc[data["Description"] == '6061-T6 Round Bar 8-1/2']
    RS90 = data.loc[data["Description"] == '6061-T6511 Round Bar 9']
    SRS187 = data.loc[data["Description"] == '304-SS Round Bar 3/16']
    TB35E = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 3-1/2 x 9/16 WA x 144']
    TB40A = data.loc[data["Description"] == '6061-T6511 Round Tube 4 x 1/8 WA x 288']
    TB425D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/4 x 1 WA x 144']
    TB45B = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/2 x 3/4 WA x 144']
    TB45D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/2 x 1 WA x 144']
    TB50B = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 5 x 3/4 WA x 144']
    TB55D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 5-1/2 x 1 WA x 144']
    TB575 = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 5-3/4 x 5/8 WA x 120']
    TB60D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 6 x 1 WA x 144']
    TB625D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 6-1/4 x 1 WA x 144']
    TB70D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 7 x 1 WA x 120']
    TB71A = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 7-1/8 x 3/4 WA x 120']
    TB71F = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 7-1/8 x 1-5/16WA x 120']
    TB775D = data.loc[data["Description"] == '6061-T6511 SMLS EXT TUBE 7-3/4 x 1 WA x 144']

    print(ind)
    print(row)


kochek_list = [EX102, EX1522, EX1524, EX1525, EX152S, EX2522, EX2524, EX252H, RS05, RS100, RS1025, RS110, RS15,
                RS175, RS20, RS2125, RS225, RS25, RS275, RS30, RS3125, RS34, RS35, RS38, RS40, RS45, RS50, RS55,
                RS575, RS60, RS65, RS70, RS80, RS85, RS90, SRS187, TB35E, TB40A, TB425D, TB45B, TB45D, TB50B,
                TB55D, TB575, TB60D, TB625D, TB70D, TB71A, TB71F, TB775D]
