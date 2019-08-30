import template_matching as tm
import numpy as np
import matplotlib.pyplot as plt
import scipy.io  # only needed for reading in .mat file
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

#template_num = 1  # exponential
template_num = 2  # gaussian
# template_num = 3  # step
cut_range = 2

# Load data
mat = scipy.io.loadmat('NorthAtlanticCTDData_A05_AR01_1998.mat')
t = np.squeeze(mat.get('t'))  # temperature
s = np.squeeze(mat.get('s'))  # salinity
z = np.squeeze(mat.get('z'))  # depth
lat = np.squeeze(mat.get('lat'))
lon = np.squeeze(mat.get('lon'))
nstations = len(lat)
del(s, mat)  # clean up workspace


# Use cross-correlation to find location of template in each profile
# and calculate mse between template and profile chunk
MSE = np.zeros((nstations, 1))
for i in range(nstations):
    t_prof = t[:, i]
    z_prof = z[:, i]
    t_prof = t_prof[np.isfinite(t_prof)]
    z_prof = z_prof[np.isfinite(z_prof)]

    chunk_value, chunk_depth = tm.find_correlation(t_prof, z_prof, template_num, cut_range)
    if template_num == 1:
        MSE[i] = tm.fit_exp(chunk_value, chunk_depth)
    elif template_num == 2:
        MSE[i] = tm.fit_gauss(chunk_value, chunk_depth)
    else:
        print('Function for fitting this template is not yet available')
    print(i)
plt.scatter(np.arange(nstations), np.sqrt(MSE))
plt.xlabel('Profile')
plt.ylabel('RMSE')
plt.show()
