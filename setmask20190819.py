import os, arcpy
from arcpy import env
from arcpy.sa import *

fpath = 'D:/f_work/E_public/E5_wxx/spei_float'
Dir_yr = 'D:/f_work/E_public/E5_wxx/spei_China_50_15'

if not os.path.exists(Dir_yr):
    os.mkdir(Dir_yr)
inMaskData = 'D:/f_work/E_public/E5_wxx/China_boundary_WGS84/China_WGS84.shp'
env.workspace = fpath
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = True

for yr in range(1950, 2015+1, 1):
    fstr = 'spei*' + str(yr) + '*.flt'
    fname = Dir_yr + os.sep + 'spei_' + str(yr) + '.tif'
    rasters = arcpy.ListRasters(fstr, 'FLT')
    print str(yr)
    outCell = CellStatistics(rasters, "MEAN", "NODATA")
    outRaster = ExtractByMask(outCell, inMaskData)
    print fname
    outRaster.save(fname)
    arcpy.Delete_management(outCell)
