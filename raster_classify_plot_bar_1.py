# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 16:08:18 2020

@author: YeHui

"""
import os, gdal
import pandas as pd
import numpy as np
from glob import glob as glb
import matplotlib.pyplot as plt
# from matplotlib.pyplot import savefig
from matplotlib.ticker import FuncFormatter
import xml.etree.ElementTree as ET

dir_input = 'D:\f_work\E_public\E1_wangwei\data\Water_save'
raster_f = dir_input + os.sep + 'water_avg'
# raster_type = 'tif'
f_xml = r'C:\Users\YeHui\Downloads\NPP80-18.tif.breaks.xml'

cond = [0, 2000]  # 数据有效范围
tree = ET.parse(f_xml)
lst = tree.findall('break')

class_values = []
for i in lst:
    class_values.append(float(i.text))
n_class = len(class_values)
# for i in root.iter('ClassBreaks'):
    
#     print('break', "=", i.attrib['break'])


color_lst = [[0,92,230],[0,112,225],[115,178,225],[190,210,225],[225,225,225],[204,204,204],[178,178,178],[156,156,156],[255,235,175],[255,211,127],[255,170,0],[230,152,0],[255,0,0],[168,0,0],[115,0,0]]
colors = list(map(lambda x: x / 255, np.array(color_lst)))

class MyPlt:
    font_porp = 'Times New Roman'
    linestyle = ''
    font_xlabel = ''
    font_ylabel = ''
    font_porp = ''
    fontsz = ''
    tick_labelsz = ''
    facecolor = ''
    ax_facecolor = ''
    ed_color = ''
    width_bar = ''
    width_spines = ''
    dpi = ''
    

def read_raster(raster_f):  
    raster_type = raster_f.split('.')[-1] 
    if raster_type == 'flt':
        raster_arr = np.fromfile(raster_f)
    else:
        ds = gdal.Open(raster_f)
        raster_arr = ds.ReadAsArray()
        im_width = ds.RasterXSize  # 行
        im_height = ds.RasterYSize  # 列
        im_bands = ds.RasterCount  # 波段数
        band1 = ds.GetRasterBand(1)  # 波段的indice起始为1，不为0
        img_datatype = band1.DataType  # 数据类型
    return raster_arr

def plot_bar(x, y):
    fig = plt.figure() # 11*5cm
    plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
    ax1 = fig.add_subplot(1,1,1)
    ax1.barh(x, y, ls=MyPlt.linestyle, ec=MyPlt.edcolor, lw=w=MyPlt.width_bar, color=MyPlt.facecolor)
    plt.xticks(fontproperties=MyPlt.font_porp)
    plt.yticks(fontproperties=MyPlt.font_prop)
    ax1.tick_params(axis='both', labelsize=MyPlt.tick_labelsz)
    ax1.set_facecolor(MyPlt.ax_facecolor)
    ax1.spines['top'].set_visible(False) #去掉上边框
    ax1.spines['right'].set_visible(False) #去掉右边框
    # ax1.spines['left'].set_linewidth(lw_spines) #设置左坐标轴宽度
    # ax1.spines['bottom'].set_linewidth(lw_spines) #设置底部坐标轴宽度
    # ax1.spines['right'].set_linewidth(lw_spines) #设置左坐标轴宽度
    # ax1.spines['top'].set_linewidth(lw_spines) #设置底部坐标轴宽度
    ax1.yaxis.set_ticks_position('none')
    ax1.xaxis.set_ticks_position('none')
    
raster_arr = read_raster(raster_f)
data = raster_arr[(raster_arr > cond[1]) | (raster_arr <= cond[0])]
pixels = len(data)
value_min, value_max = min(data), max(data)

class_counts = []
for i in range(0, n_class+1):   
    if i == n_class:
        break
    # print(str(i))
    counts = len(data((data >= class_values[i])&(data < class_values[i+1])))
    class_counts.append(counts)

X_data = np.array(class_values)   
Y_data = np.array(class_counts)
Y_percnt = Y_data / pixels * 100
df = pd.DataFrame([X_data, Y_data], columns = ['class'])


# for i, class_value in enumerate(0, class_values):
#     counts = len(data((data >= class_value)&(data < class_value)))
    # if i == 0:
    #     counts = len(data((data >= value_min)&(data < class_value)))
    # elif i == n_class:
    #     counts = len(data((data >= value_min)&(data < class_value)))
            
    









