# -*- coding: utf-8 -*-
import os

HDF_Path = r"D:\LDPZZ\1\MOD17A2H"
var = "MOD17A2"
# MRT path -> need modify
MRT_path = r'F:\Hui_Zone\MRT\bin'
TIF_Path = HDF_Path + os.sep + "TIFF"
if not os.path.isdir(TIF_Path):
    os.makedirs(TIF_Path)
os.chdir(MRT_path)
# for var in varlist:
print(var + " is processing")
# read prm file
Fprm = 'F:/Hui_Zone/MOD_base/MOD17A2H.prm'
with open(Fprm) as fp:
    i = 0
    for line in fp:
        if i == 10:
            break
        i = i + 1
prm_strs = line.split("=")[1]
prm_str = prm_strs.strip('\n')[3:-2]
# prm_str = '0 0 0 0 1 0 0 0 0 0 0 0'
band_mark = " -s \"" + prm_str + "\" -o "

yr1 = 2014
yr2 = 2015
doy = 8
for y in range(yr1, yr2+1):
    if doy == 8:
        for d in range(0, 46):
            dmy = str(y * 1000 + d * 8 + 1)    
            print(var + ".A" + dmy)
    
            fhdf = HDF_Path + os.sep + var + "*" + dmy + "*.hdf"
            ftxt = HDF_Path + os.sep + var + dmy + ".txt"
            if os.path.isfile(ftxt):
                rm = "del " + ftxt
                os.system(rm)
    
            cmd1 = "dir /b/s " + fhdf + " >> " + ftxt
            print(cmd1)
            os.system(cmd1)
    
            tmpf = HDF_Path + os.sep + "msctmp_" + dmy + ".hdf"
            cmd2 = "mrtmosaic -i " + ftxt + band_mark + tmpf
            print(cmd2)
            os.system(cmd2)

            ftif = TIF_Path + os.sep + var + "_" + dmy + ".tif"
            cmd3 = "resample -p %s -i %s -o %s"%(Fprm, tmpf, ftif)

            print(cmd3)
            os.system(cmd3)

            # Delete temporal file
            cmd = "del " + tmpf
            os.system(cmd)
