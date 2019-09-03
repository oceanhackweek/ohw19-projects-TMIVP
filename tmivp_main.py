import template_matching as tm
import numpy as np
import matplotlib.pyplot as plt
import scipy.io  # only needed for reading in .mat file
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# template_num = 1  # exponential
template_num = 2  # gaussian
# template_num = 3  # step

# List of scale factors of template size to try
scale_factors = [1, 2, 3, 4, 5]

# # Load data
# Anna's data
# import xarray as xr
# file  = 'SADCP_TAO5b_uv_5_140W_gridded.cdf'
# ds = xr.open_dataset(file)
# t = ds.UADCP_GRID.isel(TAX_5=0).sel(YLAT=slice(-4,4)).values
# lat = ds.YLAT.sel(YLAT=slice(-4,4)).values
# z = np.expand_dims(ds.Z750.values,1)+np.zeros_like(t)
# lon  = np.ones(len(lat)) * 140

# Paige's data
mat = scipy.io.loadmat('NorthAtlanticCTDData_A05_AR01_1998.mat')
t = np.squeeze(mat.get('t'))  # temperature
s = np.squeeze(mat.get('s'))  # salinity
z = np.squeeze(mat.get('z'))  # depth
lat = np.squeeze(mat.get('lat'))
lon = np.squeeze(mat.get('lon'))
del(s, mat)  # clean up workspace

nstations = len(lat)

# Use cross-correlation to find location of template in each profile
# and calculate mse between template and profile chunk
MSE = np.zeros((nstations, 1))
scale_factor_best = np.zeros((nstations, 1))
for i in range(nstations):
    t_prof = t[:, i]
    z_prof = z[:, i]
    t_prof = t_prof[np.isfinite(t_prof)]
    z_prof = z_prof[np.isfinite(t_prof)]
    MSE_sf = np.zeros((len(scale_factors), 1))
    for j, scale_factor in zip(range(len(scale_factors)), scale_factors):
        chunk_value, chunk_depth = tm.find_correlation(t_prof, z_prof,
                                                       template_num,
                                                       scale_factor)

        chunk_value = chunk_value[np.isfinite(chunk_value)]
        chunk_depth = chunk_depth[np.isfinite(chunk_value)]
        if template_num == 1:
            # For now only using top 60 pts because chunk is causing errors
            MSE_sf[j] = tm.fit_exp(t_prof[:60], z_prof[:60])
        elif template_num == 2:
            MSE_sf[j] = tm.fit_gauss(chunk_value, chunk_depth)
        else:
            print('Function for fitting this template is not yet available')
        print(i)
    try:
        scale_factor_best[i] = scale_factors[np.nanargmin(MSE_sf)]
        MSE[i] = np.nanmin(MSE_sf)
    except ValueError:
        MSE[i] = np.nan

# Temporary plotting code

plt.scatter(np.arange(nstations), np.sqrt(MSE))
plt.xlabel('Profile')
plt.ylabel('RMSE')
plt.show()

plt.scatter(np.arange(nstations), scale_factor_best)
plt.xlabel('Profile')
plt.ylabel('Scale Factor')
plt.show()
