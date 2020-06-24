import arcpy
import numpy

inRaster='C:/workspace/test1.tif'
outRaster='C:/workspace/test2.tif'

dsc=arcpy.Describe(inRaster)
arcpy.env.extent=dsc.Extent
arcpy.env.outputCoordinateSystem=dsc.SpatialReference
arcpy.env.cellSize=dsc.meanCellWidth

myArray = arcpy.RasterToNumPyArray(r)
myArraySum = myArray.sum(1)
myArraySum.shape = (myArray.shape[0],1)
myArrayPerc = (myArray * 1.0)/ myArraySum

newRaster = arcpy.NumPyArrayToRaster(myArrayPerc)
newRaster.save(outRaster)