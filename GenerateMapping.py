import pandas as pd
import sys
import math

## 5 different mapping types for ME0 depeneding on VFAT_N
## Hirose to channel mapping is common
## Strip to hirose is typical 


## Mapping type to mapping dataframe
hiroseMapping = pd.read_csv("MappingFiles/hrs_connector.csv")
mappings = {
    1:pd.read_csv("MappingFiles/ME0Type1.csv"),
    2:pd.read_csv("MappingFiles/ME0Type2.csv"),
    3:pd.read_csv("MappingFiles/ME0Type3.csv"),
    4:pd.read_csv("MappingFiles/ME0Type4.csv"),
    5:pd.read_csv("MappingFiles/ME0Type5.csv"),
    6:pd.read_csv("MappingFiles/ME0Type6.csv"),
}
vfatToRoutingType = {
    0:4,
    1:4,
    2:4,
    3:4,
    4:1,
    5:1,
    6:1,
    7:3,
    8:6,
    9:1,
    10:5,
    11:1,
    12:5,
    13:1,
    14:1,
    15:1,
    16:5,
    17:5,
    18:5,
    19:5,
    20:1,
    21:1,
    22:1,
    23:2
}

def VFAT2iEta_iPhi(VFATN):
    try:
        vfatPosition = int(VFATN)
    except:
        print("VFAT Number provided is not a number.\nExiting...")
        sys.exit(0)

    if vfatPosition <0 or vfatPosition>23:
        print("Invalid VFAT position.\nExiting...")
        sys.exit(0)

    iEta = (8 - vfatPosition%8)
    iPhi = int(vfatPosition/8 + 1)
    return iEta,math.ceil(iPhi)

def getVFATMapping(vfat):
    print(f"producing VFAT {vfat} mapping")    
    eta,phi = VFAT2iEta_iPhi(vfat)

    tmp_data = []
    mappingType = vfatToRoutingType[vfat]
    df_mapping = mappings[mappingType]
    for ch in range(128):
        hrs = hiroseMapping[ hiroseMapping["vfatCh"] ==ch]["hrsPin"].iloc[0]
        strip = df_mapping[ df_mapping["Hirose"] ==hrs]["stripN"].iloc[0]
        if strip != -1:  ## Strip -1 reserved for "disconnected hirose pin"
            strip=strip+128*(phi-1)
        tmp_data.append([vfat,ch,eta,strip])
    df = pd.DataFrame(tmp_data,columns=["vfatId","vfatCh","iEta","strip"])
    return df
    
df = pd.DataFrame()
for vfatN in range(24):
    df = pd.concat([getVFATMapping(vfatN),df])

df.to_csv("me0_mapping.csv",index=False)
