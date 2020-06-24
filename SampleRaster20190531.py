# -*- coding: utf-8 -*-

# @author: HuiYe

# Created by Hui Ye on 2017-3-29 16:11
#import arcgisscripting
#import sys
#import string
import os, glob
#import math
import arcpy
from arcpy import env
from glob import glob as glb
from arcpy.sa import *
from shutil import copy
os.system("cls")
arcpy.CheckOutExtension("Spatial")

# FltDir = r'Z:\Database\Meteo1km\MeteoGrid'
FltDir = [r'Z:\Database\Meto_1km\China', r'Z:\Database\Meteo1km\MeteoGrid']
ShpDir = r'D:\OneDrive\WorkSpace\Sites'
# HdrDir = r'E:\OneDrive\DataBase\GeoDatabase_HuiYe\Project2File'
TableDir = r'F:\Hui_Zone\Temp\tables_qh'
Dest_dir = r'D:\OneDrive\WorkSpace\ZhangMiao\Lists'

# HdrName = HdrDir +'\Glopen_China8km_Albers_v110.hdr'
# PrjName = HdrDir + '\WGS84_Albers_v110.prj'

Shps = ['QingHai_110.shp', 'QingHai_clark.shp']
# vars = ['C8days', 'TEM', 'SSD']
# vars = ['TEM', 'SSD']
# vars = ['PRCP', 'TAVG', 'SSD', 'WIN']
# vars = ['TAVG', 'SSD', 'WIN']
vars = ['WIN']
# wks = FltDir + '\\temp'
if not os.path.exists(TableDir):
    os.mkdir(TableDir)
# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True
sampMethod = "NEAREST"

yrs = range(1990, 2015 + 1)

for var in vars:
    # tabels = []
    # i = 1
    for yr in yrs:
        if yr < 2000:
            rstDir = FltDir[1] + os.sep + var
            ShpFile = ShpDir + os.sep + Shps[1]
            if var == 'TAVG':
                rstDir = FltDir[1] + os.sep + 'TEM'
        else:
            rstDir = FltDir[0] + os.sep + var
            ShpFile = ShpDir + os.sep + Shps[0]
        env.workspace = rstDir
        fname = '*' + str(yr) + '*.flt'
        # rasts = sorted(glb(fname))
        rasters = arcpy.ListRasters(fname, 'FLT')
        if rasters:
            # if var == 'TAVG':
            #     Table = TableDir + os.sep + 'TEM' + str(yr)
            # else:
            Table = TableDir + os.sep + var + str(yr)
            # for raster in rasters:
            #     rst = arcpy.Raster(raster)
            #     fltname = raster[:-4]
            #     strname = os.path.basename(raster)[:-4]
            print Table
            Sample(rasters, ShpFile, Table, sampMethod)
            arcpy.TableToDBASE_conversion(Table, TableDir)
            arcpy.Delete_management(Table)
        else:
            print fname
            # HdrFile = fltname + '.hdr'
            # PrjFile = fltname + '.prj'
            # # HdrName = FltFile + '*.hdr'
            # if not os.path.exists(HdrFile):
            #     copyfile(HdrName, HdrFile)
            # if not os.path.exists(PrjFile):
            #     copyfile(PrjName, PrjFile)
try:
    copy(TableDir, Dest_dir)
except:
    print 'copy faild'
            # outTable = TableDir + Var + str(yr)
            # ID = yr * 100 + i
            # i = i + 1

            # Execute Sample



