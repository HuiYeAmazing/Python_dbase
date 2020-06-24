# -*- coding: utf-8 -*-
import os
"""
mrtmosaic –i </directory/input_file_name_list.prm> 
        -s spectral_subset ["b1 b2 ... bN"] 
        -o </directory/output_mosaic.hdf>
Example: mrtmosaic –I TmpMosaic.prm –s “1 1 0 1” –o mosaic.hdf
resample -p <parameter_file> -i <input_file_name> -o <output_file_name>
"""
HDF_Path = r"Z:\HuiYe\MOD17A3"
var = "MOD17a3"
# MRT path -> need modify
MRT_path = r'F:\Hui_Zone\MRT\bin'
#out path of MRT processing
TIF_Path = HDF_Path + os.sep + "TIFF"
if not os.path.exists(TIF_Path):
    os.makedirs(TIF_Path)
    
os.chdir(MRT_path) # change directory to MRT path (important)
# read prm file
Fprm = 'F:/Hui_Zone/MOD_base/MOD17A3.prm'
with open(Fprm) as fp:
    i = 0
    for line in fp:
        if i == 10:
            prm_strs = line.split("=")[1]
            break
        i = i + 1
bands = prm_strs.strip('\n')[3:-2]
band_mark = " -s \"" + bands + "\" -o "
year = 2001, 2018
for y in range(year[1], year[2]+1):
    dmy = str(y * 1000 + 1)
    fhdf = HDF_Path + os.sep + var + ".A" + dmy + "*.hdf"
    ftxt = HDF_Path + os.sep + var + dmy + ".txt"
    if os.path.isfile(ftxt):
        os.remove(ftxt)

    cmd1 = "dir /b/s " + fhdf + " >> " + ftxt
    print(cmd1)
    os.system(cmd1)
#    tmpf is the temporal hdf file which mosaic by hdfs
    tmpf = HDF_Path + os.sep + "msctmp_" + dmy + ".hdf"
    cmd2 = "mrtmosaic -i " + ftxt + band_mark + tmpf
    print(cmd2)
    os.system(cmd2)

    ftif = TIF_Path + os.sep + var + "_" + str(y) + ".tif"
    cmd3 = "resample -p %s -i %s -o %s" %(Fprm, tmpf, ftif)
    print(cmd3)
    os.system(cmd3)
    # Delete temporal file
    os.remove(tmpf)

























