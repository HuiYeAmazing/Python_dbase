# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 20:55:47 2019

@author: admin
"""

import os
from glob import glob as glb
from shutil import copyfile

fpath = r'C:\Users\admin\Downloads\课件丨遥感大数据工具Google_Earth_Engine'
dir_out = r'D:\E_学习'
flists = sorted(glb(fpath + os.sep + '*'), key=os.path.getmtime)
i = 1
for f_strs in flists:
    fname = 'GEE_' + str('%03d' %i) + '.' + f_strs.split('.')[-1]
    print(fname)
    copyfile(f_strs, dir_out + os.sep + fname)
    i += 1


