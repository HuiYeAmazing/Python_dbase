# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:57:55 2020

@author: YeHui
"""
import os, rasterio, time
import numpy as np
from rasterio.windows import get_data_window
from multiprocessing import Pool
import multiprocessing
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.feature_selection import f_regression

dir_raster = r'D:\f_work\C_workspace\Sanjy'
year_set = 2000, 2018
var_str = 'NPP'
raster_type = '.flt'

x_var_time = np.range(1, 19)

def fun_regress(data_1):
    """
    :param data_1: 需要计算趋势和显著性水平的数组
    :return: 返回趋势r2score和显著性水平pvalue
    """
    x_data = data_1
    y_data = x_var_time
    x_data = x_data.reshape(-1, 1)
    regr = LinearRegression()
    regr.fit(x_data, y_data)
    y_pred = regr.predict(x_data)
    r2score = r2_score(y_data, y_pred)              # 趋势
    pvalue = f_regression(x_data, y_data)[1][0]     # 显著性水平
    return pvalue, r2score                          # 返回趋势和显著性水平

# def Write_raster(file, data, ds):
#     """
#     :param file: tif文件名
#     :param data: 写入的数组
#     :param ds: 所需要的数据集
#     """
#     band1 = ds.GetRasterBand(1)
#     img_datatype = band1.DataType
#     driver = gdal.GetDriverByName('GTiff')                  # 明确写入数据驱动类型
#     out_ds = driver.Create(
#         r'E:/study/资料/数据/趋势与显著性水平/' + file,         # tif文件所保存的路径
#         ds.RasterXSize,                                     # 行
#         ds.RasterYSize,                                     # 列
#         ds.RasterCount,                                     # 波段数
#         img_datatype)                                       # 数据类型
#     out_ds.SetProjection(ds.GetProjection())                # 投影信息
#     out_ds.SetGeoTransform(ds.GetGeoTransform())            # 仿射信息
#     for i in range(1, ds.RasterCount + 1):                  # 循环逐波段写入
#         out_band = out_ds.GetRasterBand(i)
#         out_band.WriteArray(data)                           # 写入数据
#     out_ds.FlushCache()
#     del out_ds
def Read_raster():
    for year in range(year_set[0], year_set[1]+1):
        f_raster = dir_raster + os.sep + var_str + str(year) + raster_type
        with rasterio.open(f_raster) as src:
            profile = src.profile
            for block_index, window in src.block_windows(1): # 1 was band of raster dataset
                block_array = src.read(window=window)
                # dat.append(block_array)
                # idx.append(block_index)
                # wid.append(window)
def fun(File1, File2, File3, File4, File5):
    """
    以路径E:/study/资料/数据/prcp_year/PRCP1980SUM.tif为例
    :param File1:为r'prcp_year/PRCP1980SUM.tif'
    :param File2:为r'prcp_year/PRCP'
    :param File3:为r'SUM.tif'
    :param File4:需要写入的趋势tif文件名，比如r'prcp趋势.tif'
    :param File5:需要写入的显著性水平tif文件名，比如r'prcp显著性水平.tif'
    """
    if __name__ == '__main__':                              # 程序入口
                        # 需要读取的tif文件所在的文件夹的所在文件夹的路径
        ds = gdal.Open(dir_raster + File1)                       # 打开文件
        # 影像数据基本情况 波段数、行、列等
        im_width = ds.RasterXSize                           # 行
        im_height = ds.RasterYSize                          # 列
        im_bands = ds.RasterCount                           # 波段数
        # 影像数据读取
        band1 = ds.GetRasterBand(1)                         # 波段的indice起始为1，不为0
        img_datatype = band1.DataType                       # 数据类型
        data1 = np.full((39, im_height * im_width), 1.0)    # 建立数组
        for year in range(1980, 2019):
            file2 = file1 + File2 + str(year) + File3
            ds = gdal.Open(file2)
            img_data = ds.ReadAsArray()                     # 读取整幅图像转化为数组
            img_data = img_data.reshape(1, -1)              # 将数组转化为1行，自定义列的数组
            data1[year - 1980] = img_data                   # 将读取的数组合并成一个大数组
        # 将数组转换成以象元数为行数，年份为列数的数组
        data1 = pd.DataFrame(data1).T                       # 数组转化为dataframe，并进行行列互换
        data1 = data1.values                                # dataframe转化为数组
        # 多核并行计算
        cores = multiprocessing.cpu_count()                 # 计算机cpu的核心数（核心数=线程数，但具有多线程技术和超线程技术的线程数一般为核心数的两倍）
        pool = Pool(cores)                                  # 开启线程池
        data2 = pool.map(fun1, data1)                       # 进行并行计算，得到的data2是一个列表，map是按行读取数组来计算
        # 将data2转换成对应数组
        data2 = pd.DataFrame(data2)
        data2 = data2.values
        data3 = data2[:, 0]
        data4 = data2[:, 1]
        data3 = data3.reshape(im_height, im_width)
        data4 = data4.reshape(im_height, im_width)
        # 写入文件
        Write(File4, data3, ds)                             # 调用Write函数
        Write(File5, data4, ds)
