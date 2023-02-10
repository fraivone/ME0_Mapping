# ME0_Mapping

The mapping is split into:
* Strip - Hirose Pin
* Hirose Pin - Channel

The mapping Hirose Pin - Channel is independent on the VFAT position. It is provided in the file [hrs_connector.csv](MappingFiles/hrs_connector.csv).
The Hirose Pin numbers are sketched [here](./Figure/HirosePin_Scheme.png).

The mapping Strip - Hirose Pin depends on the particular way in which the strips are routed on the readout board.
The ME0 24 VFATs have 5 different strip routings, sketched [here](./Figure/ReadoutBoard.png).
From the sketch one can easily tell apart `Type 1` from `Type 4` and `Type 5`.
and might think that for `VFAT 7` and `VFAT 23` the routing `Type 1` also applies.

**No!** (M.B.).

These 2 VFATs position are special: they've lost 5 strips each during the creative ME0 design. Indeed in this eta partition there are only 374 active strips rather than the usual 384. That calls for special routing for `VFAT 7` and `VFAT 23`. Yes, they could've made it easier.

The `VFAT 7` routing sketch is reported [here](./Figure/VFAT7_Type3.png) to be compared with `VFAT 15` routing [here](./Figure/VFAT15_Type1.png).

The python script loops takes into account the two mapping stages and produces a `.csv` file containing the mapping with columns  `vfatId` `vfatCh`	`iEta`	`strip`.

Typical execution 
```
python3 GenerateMapping.py
```