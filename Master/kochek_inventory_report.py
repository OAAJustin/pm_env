import pandas as pd

file = 'inventory_12.6.2022.csv'

df_master_inventory = pd.read_csv(file, usecols= (0, 1, 3, 4))

for part in df_master_inventory:
    df_master_inventory["Partnumber"] = df_master_inventory["Partnumber"].str.replace('=', '')
    df_master_inventory["Partnumber"] = df_master_inventory["Partnumber"].str.replace('"', '')
    df_master_inventory["Description"] = df_master_inventory["Description"].str.replace('=', '')
    df_master_inventory["Description"] = df_master_inventory["Description"].str.replace('"', '')

EX102 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX102) 1 RL 1.75 OD X .500 WA X 12' EXT"]
EX1522 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX1522) 1.5 RL 2.08 OD X .310 X 12' EXT"]
EX1524 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX1524) 1.5 RL 2.75 OD X .656 X 12' EXT"]
EX1525 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX1525) 1.5 RL 2.375 OD X .475 X 12' EXT"]
EX152S = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX152S) 1.5 RL 2.45 OD SOLID X 12' EXT"]
EX2522 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX2522) 2.5 RL 3.530 OD X 1.040 X 12' EXT"]
EX2524 = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX2524) 2.5 RL 3.625 OD x 12' EXT"]
EX252H = df_master_inventory.loc[df_master_inventory["Description"] == "6061-T6 (EX252H) 2.5 RL X .593"]
RS05 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 1/2 x 144']
RS100 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6 Round Bar 10']
RS1025 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 1-1/4 x 144']
RS110 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6 Round Bar 11']
RS15 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 1-1/2 x 144']
RS175 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 1-3/4 x 144']
RS20 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T651 CF Round Bar 2 x 144']
RS2125 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 2-1/8 x 144']
RS225 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 2-1/4 x 144']
RS25 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 2-1/2 x 144']
RS275 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round bar 2-3/4 x 144']
RS30 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 3 x 144']
RS3125 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 3-1/8 x 144']
RS34 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 3/4 x 144']
RS35 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 3-1/2 x 144']
RS38 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 3/8 x 144']
RS40 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 4 x 144']
RS45 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 4-1/2 x 144']
RS50 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 5 x 144']
RS55 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 5-1/2 x 144']
RS575 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 5-3/4 x 144']
RS60 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 6 x 144']
RS65 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 6-1/2 x 144']
RS70 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 7']
RS80 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6 Round Bar 8 x 144']
RS85 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6 Round Bar 8-1/2']
RS90 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Bar 9']
SRS187 = df_master_inventory.loc[df_master_inventory["Description"] == '304-SS Round Bar 3/16']
TB35E = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 3-1/2 x 9/16 WA x 144']
TB40A = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 Round Tube 4 x 1/8 WA x 288']
TB425D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/4 x 1 WA x 144']
TB45B = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/2 x 3/4 WA x 144']
TB45D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 4-1/2 x 1 WA x 144']
TB50B = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 5 x 3/4 WA x 144']
TB55D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 5-1/2 x 1 WA x 144']
TB575 = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 5-3/4 x 5/8 WA x 120']
TB60D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 6 x 1 WA x 144']
TB625D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 6-1/4 x 1 WA x 144']
TB70D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 7 x 1 WA x 120']
TB71A = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 7-1/8 x 3/4 WA x 120']
TB71F = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 7-1/8 x 1-5/16WA x 120']
TB775D = df_master_inventory.loc[df_master_inventory["Description"] == '6061-T6511 SMLS EXT TUBE 7-3/4 x 1 WA x 144']

kochek_list = [EX102, EX1522, EX1524, EX1525, EX152S, EX2522, EX2524, EX252H, RS05, RS100, RS1025, RS110, RS15,
                RS175, RS20, RS2125, RS225, RS25, RS275, RS30, RS3125, RS34, RS35, RS38, RS40, RS45, RS50, RS55,
                RS575, RS60, RS65, RS70, RS80, RS85, RS90, SRS187, TB35E, TB40A, TB425D, TB45B, TB45D, TB50B,
                TB55D, TB575, TB60D, TB625D, TB70D, TB71A, TB71F, TB775D]

kochek_list_index = ['EX102', 'EX1522', 'EX1524', 'EX1525', 'EX152S', 'EX2522', 'EX2524', 'EX252H', 'RS05', 'RS100', 'RS1025', 'RS110', 'RS15',
'RS175', 'RS20', 'RS2125', 'RS225', 'RS25', 'RS275', 'RS30', 'RS3125', 'RS34', 'RS35', 'RS38', 'RS40', 'RS45', 'RS50', 'RS55',
'RS575', 'RS60', 'RS65', 'RS70', 'RS80', 'RS85', 'RS90', 'SRS187', 'TB35E', 'TB40A', 'TB425D', 'TB45B', 'TB45D', 'TB50B',
'TB55D', 'TB575', 'TB60D', 'TB625D', 'TB70D', 'TB71A', 'TB71F', 'TB775D']


kochek_inventory = pd.concat(kochek_list)

kochek_inventory.to_csv('Kochek Inventory.csv', index = False)

kochek_inventory.to_excel('Kochek Inventory.xlsx', index = False)




