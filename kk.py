# from PIL import Image
import matplotlib.pyplot as plt
import xarray as xr
import sacpy 
sst = xr.open_dataset("../DATA/HadISST_sst_2x2.nc")['sst']

sst.plot()
plt.show()