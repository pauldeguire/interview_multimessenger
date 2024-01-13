##
## Import required packages
##
import functions as fun
import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np

##
## Import csv files
##
path = 'Exercise/Data/'
list_files = os.listdir(path)
ys = []
toplot1 = []

all_data = {} # The key will be the name of the file, the element will be the data

for file in list_files:
    name = file[:-4]
    all_data[name] = pd.read_csv(path+file,header=5) # We take header=5 because we don't want the first part of the csv file
    x,y = all_data[name]['Freq(Hz)'],all_data[name]['S21(MAG)']
    toplot1.append(((x,y,name),'plot'))
    ys.append(y)
    
fun.plot_zoom([1.5e8,4.5e8],toplot1)



##
## We see the amplifiers seem to obey the same pattern
##

ys = np.asarray(ys)
std = ys.std(0)
mean = ys.mean(0)
toplot2 = [((x,mean,std),'uncert')]
fun.plot_zoom([1.5e8,4e8],toplot2)


plt.plot(x,std/mean)
#plt.xlim([1.5e8,4.5e8])
#plt.ylim([0.01,0.02])
plt.show()
