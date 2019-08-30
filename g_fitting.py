#!/Users/kathryngunn/miniconda3/bin/python


import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import numpy as np

from scipy.optimize import curve_fit
coord = np.array([  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100., 
              110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210., 
              220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320., 
              330., 340., 350., 360., 370., 380., 390., 400., 410., 420., 430., 
              440., 450., 460., 470., 480., 490., 500., 510., 520., 530., 540., 
              550., 560., 570., 580., 590., 600., 610., 620., 630., 640.,  
              650., 660., 670., 680., 690., 700., 710., 720., 730., 740., 750.])  

tst_sig = np.array([        np.nan,         np.nan,  0.11651988,  0.11869922,  0.1366819 , 
               0.14823426,  0.21569708,  0.32249379,  0.45955832,  0.60181144, 
               0.70348985,  0.80934128,  0.91615298,  0.95992051,  0.863076  , 
               0.69336652,  0.52049277,  0.38300575,  0.31645564,  0.26290439, 
               0.21254273,  0.16937823,  0.13970553,  0.10487252,  0.04537953, 
              -0.02918168, -0.10864066, -0.17158342, -0.21602282, -0.24900891, 
              -0.27375611, -0.29035206, -0.29797157, -0.30768049, -0.31547794, 
              -0.31590211,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan,         np.nan,         np.nan,         np.nan,         np.nan, 
                      np.nan])  

#test data
#x = ar(range(10))
#y = ar([0,1,2,3,4,5,4,3,2,1])

tst_sig[np.isnan(tst_sig)] = 0 # Replace nan with 0


y = tst_sig[5:22] # slice to approximate gaussian, this cut will be provided by the cross-correlation part in the end
x = coord[5:22] 

 #Initial guesses
mean = sum(x * y) / sum(y)
sigma = np.sqrt(sum(y * (x - mean)**2) / sum(y))

#print(mean)
#print(sigma)

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))

popt,pcov = curve_fit(gaus,x,y,p0=[1,mean,sigma])

plt.plot(x,y,'b+:',label='data')
plt.plot(x,gaus(x,*popt),'ro:',label='fit')
plt.legend()
plt.title('Fit to Gaussian')
plt.xlabel('Depth/Time')
plt.ylabel('Variable')
plt.show()

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

rmse_val = rmse(y, gaus(x,*popt))
print("rms error is: " + str(rmse_val))
