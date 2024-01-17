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
bandwidth = []

all_data = {} # The key will be the name of the file, the element will be the data

for file in list_files:
    name = file[:-4]
    all_data[name] = pd.read_csv(path+file,header=5) # We take header=5 because we don't want the first part of the csv file
    x,y = all_data[name]['Freq(Hz)'],all_data[name]['S21(MAG)']
    toplot1.append(((x,y,name),'plot'))
    ys.append(y)
    bandwidth.append(fun.bandwidth(x,y,0.5))
    
fun.plot_zoom([1.5e8,4.5e8],toplot1,name_fig='all_amp')

bandwidth = np.asarray(bandwidth)

##
## We see the amplifiers seem to obey the same pattern, but some have higher gains than others.
## Let's asssume all the amplifiers were designed to have the same characteristics and find a mean value and a std
##

ys = np.asarray(ys)
std = ys.std(0)
mean = ys.mean(0)
toplot2 = [((x,mean,std),'uncert')]
fun.plot_zoom([1.5e8,4.5e8],toplot2,name_fig='uncert')


toplot3 = [((x,std/mean,'$\\sigma/\\mu$'),'plot')]
fun.plot_zoom([1e8,6e8],toplot3,name_fig='cv',place='up',ylab='Coefficient of variation')

mean_down,mean_up = bandwidth.mean(0)
std_down,std_up = bandwidth.std(0)
print("Down frequency = %.2e +- %.2e"%(mean_down,std_down))
print("Up frequency = %.2e +- %.2e"%(mean_up,std_up))

