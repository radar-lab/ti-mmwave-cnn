import numpy as np
import os

for root,dirs,files in os.walk('./database/'):
    for file in files:
        if file.endswith(".csv") and file.startswith("x_"):
            print('Loading '+file+'...')
            data = np.genfromtxt('./database/'+file, delimiter=',')
            newdata = np.zeros(data.shape)
            for i in range(data.shape[0]):
                if max(data[i,:])!=0:
                    newdata[i,:] = data[i,:]/max(data[i,:])
            np.savetxt('./a/'+file, newdata, delimiter=",")