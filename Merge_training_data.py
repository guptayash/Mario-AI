import os
import numpy as np
import glob
from os import path
fpath ="J:\\Machine Learning Project\\Data files\\Final File\\train_data.npy"
npyfilespath ='J:\\Machine Learning Project\\Data files'   
os.chdir(npyfilespath)

with open(fpath, 'wb') as f_handle:
    for npfile in glob.glob("*.npy"):

        # Find the path of the file
        filepath = os.path.join(path, npfile)
        print (filepath)
        # Load file
        dataArray= np.load(filepath)
        print (dataArray)
        np.save(f_handle,dataArray)
dataArray= np.load(fpath)
print (dataArray)
