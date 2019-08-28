# -*- coding: utf-8 -*-
"""
This script reads in ADCP files, which contain vertical profiles of zonal
and meridional velocities, along with info about the Latitude and timing info.
@author: Anna
"""
# import modules and functions
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import glob

# find files 
files = glob.glob('./SADCP*cdf')

# load the data 
nf = len(files)
datasets = {}
for i in range(nf):
	datasets[i] = xr.open_dataset(files[i])

# get the time axis names
time_axes = []                                                                                                                             
for i in range(nf): 
	time_axes.append(list(datasets[i].dims.keys())[0])


# example plot for one dataset
for i in range(len(datasets[0].YLAT)):
	datasets[0].UADCP_GRID.isel(TAX_4=0, YLAT=i).plot(y='Z750')
plt.gca().invert_yaxis()
plt.show()

# there's lots of vertical columns here, use some for examples
vert_col_array = np.zeros((datasets[0].TAX_4.shape[0],datasets[0].YLAT.shape[0], datasets[0].Z750.shape[0])) 
for times in range(vert_col_array.shape[0]):  
        for lats in range(vert_col_array.shape[1]): 
                vert_col_array[times,lats,:] = datasets[0].UADCP_GRID.isel({time_axes[0]:times, 'YLAT':lats}) 

depth_column = datasets[0].Z750.data


