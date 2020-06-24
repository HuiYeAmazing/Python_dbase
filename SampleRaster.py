# -*- coding: utf-8 -*-

# @author: HuiYe

# Created by Hui Ye on 2017-3-29 16:11
#import arcgisscripting
#import sys
#import string
import os
#import math
import arcpy
from arcpy import env
from arcpy.sa import *
from shutil import copyfile
os.system("cls")
arcpy.CheckOutExtension("Spatial")

FltDir = r'D:\Model\Model_Results'
ShpDir = r'D:\Model\Flux_Database'
HdrDir = r'E:\OneDrive\DataBase\GeoDatabase_HuiYe\Project2File'
TableDir = r'D:\Model\Validation\\'

HdrName = HdrDir +'\Glopen_China8km_Albers_v110.hdr'
PrjName = HdrDir + '\WGS84_Albers_v110.prj'

ShpFile = ShpDir + '\Flux2Sites.shp'
Var = 'GPP'
wks = FltDir + '\\temp'
if not os.path.exists(wks):
    os.mkdir(wks)


env.workspace = FltDir
for yr in range(2002, 2009+1):
    FltName = '%s\\%s%d' %(FltDir, Var, yr)
    FltFile = FltName + '.flt'
    HdrFile = FltName + '.hdr'
    PrjFile = FltName + '.prj'
    # HdrName = FltFile + '*.hdr'
    if os.path.exists(FltName + '*.hdr'):
        os.remove(FltName + '*.hdr')
    if os.path.exists(FltName + '*.prj'):
        os.remove(FltName + '*.prj')
    copyfile(HdrName, HdrFile)
    copyfile(PrjName, PrjFile)
    TempRaster = wks + "\\" + Var + str(yr)
    arcpy.FloatToRaster_conversion(FltFile, TempRaster)

    outTable = TableDir + Var + str(yr)
    sampMethod = "NEAREST"

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Execute Sample
    Sample(TempRaster, ShpFile, outTable, sampMethod)



