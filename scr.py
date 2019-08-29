import template_matching                                                                                                                    
import numpy as np                                                                                                                          
import matplotlib.pyplot as plt

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
tst_sig[np.isnan(tst_sig)] = 0 

outsig, outcoord = template_matching.find_correlation(tst_sig,coord,2,2) 

plt.plot(outcoord,outsig)
plt.show()
