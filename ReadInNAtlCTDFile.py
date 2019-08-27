# -*- coding: utf-8 -*-
"""
This script reads in the file NorthAtlanticCTDData_A05_AR01_1998.mat, which
contains CTD profiles for the A05/AR01 1998 line along 24.5N in the North
Atlantic, and plots the temperature and salinity profiles versus depth.
@author: paige
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

#Load data
mat = scipy.io.loadmat('NorthAtlanticCTDData_A05_AR01_1998.mat')

t = np.squeeze(mat.get('t')) #temperature
s = np.squeeze(mat.get('s')) #salinity
z = np.squeeze(mat.get('z')) #depth
nstations = 130

# Plot a single profile
ix = 100;
plt.plot(t[:,0],z[:,0])
plt.xlabel(r"$\theta$ (℃)"); plt.ylabel('Depth (meters)')
#plt.title('Station Number XX')
plt.gca().invert_yaxis()
plt.show() 

plt.plot(s[:,0],z[:,0],"-o")
plt.xlabel('Absolute Salinity'); plt.ylabel('Depth (meters)')
#plt.title('Station Number XX')
plt.gca().invert_yaxis()
plt.show() 

#Plot all temperature profiles
for i in range(nstations):
    plt.plot(t[:,i],z[:,i])
plt.gca().invert_yaxis()
plt.show()

#Plot all salinity profiles
for i in range(nstations):
    plt.plot(s[:,i],z[:,i])
plt.gca().invert_yaxis()
plt.show()