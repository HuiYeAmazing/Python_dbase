# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:36:22 2018

@author: Administrator
"""
import os
from pymodis import downmodis


# Variables for data download
#dest = r"G:/Hui_Zone/MOD15A2H" # This directory must already exist BTW
#tiles = "h23v05, h24v05, h25v05,h26v05, h27v05, h28v05, h23v04, h24v04, h25v04, h26v04, h27v04, h25v06, h26v06, h27v06, h28v06, h29v06, h28v07, h29v07, h28v08, h29v08" # That's the MODIS tile covering northern Europe
#day = "2002.01.01"
#enddate = "2004.01.01" # The download works backward, so that enddate is anterior to day=
#product = "MOD15A2H.006"
#
#
## Instantiate download class, connect and download
##modis_down = downmodis.downModis(destinationFolder=dest, password="4pgkyr7yXTY4pdg", user="HuiYe.cn", tiles=tiles, today=day, enddate=enddate, product=product)
#modis_down = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, user = "HuiYe.cn", password = "4pgkyr7yXTY4pdg",enddate=enddate, product=product)
#modis_down.connect()
#modis_down.downloadsAllDay()
#
#print('MOD15A2H 2002-2004 have finished.')

# Check that the data has been downloaded
dest = "D:\TMP" # This directory must already exist BTW
if not os.path.isdir(dest):
    os.makedirs(dest)
#tiles = "h25v05,h26v05"
tiles = "h23v04, h23v05, h24v04, h24v05, h25v03, h25v04, h25v05, h25v06, h26v03, h26v04, h26v05,  h26v06,  \
        h27v04, h27v05, h27v06, h28v05, h28v06, h28v07, h29v06" # That's the MODIS tile covering China except the islands in sourth
day = "2001.01.01"
enddate = "2018.01.01" # The download works backward, so that enddate is anterior to day=
product = "MCD12Q1.006"

modis_down = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, user = "HuiYe.cn", password = "4pgkyr7yXTY4pdg",enddate=enddate, product=product,path="MOTA")
modis_down.connect()
modis_down.downloadsAllDay()

#print('MOD15A2H 2013-2015 have finished.')

del day, enddate

#dest = r"G:/Hui_Zone/MOD15A2H" # This directory must already exist BTW
#tiles = "h23v05, h24v05, h25v05,h26v05, h27v05, h28v05, h23v04, h24v04, h25v04, h26v04, h27v04, h25v06, h26v06, h27v06, h28v06, h29v06, h28v07, h29v07, h28v08, h29v08"
#day = "2017.01.01"
#enddate = "2018.12.01" # The download works backward, so that enddate is anterior to day=
#product = "MOD15A2H.006"
#
#modis_down = downmodis.downModis(destinationFolder=dest, tiles=tiles, today=day, user = "HuiYe.cn", password = "4pgkyr7yXTY4pdg",enddate=enddate, product=product)
#modis_down.connect()
#modis_down.downloadsAllDay()
#
#print('MOD15A2H 2017-2018 have finished.')


