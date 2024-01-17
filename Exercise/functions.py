import numpy as np
from matplotlib import pyplot as plt


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


def find_closer(array,braket):
    """
    Input: An array as well as a list [val_down,val_up] for the interval
    Output: A list [down,up] with index values from the initial array
    """
    idx_min,idx_max = find_nearest(array,braket[0]),find_nearest(array,braket[1])
    return [idx_min,idx_max+1]


def plot_zoom(xvals,to_plot,place='down',name_fig='test',xlab='Frequency (Hz)',ylab='Amplification magnitude'):
    """
    Input: A list with a x interval for the subplot inside the big plot, and a list to know what to plot 
    Output: The figure is saved in the Figures folder and is shown
    """
    fig, ax1 = plt.subplots(figsize=(9,4))
    if place=='down':l, b, h, w = .25, .3, .3, .4 # To place the subplot
    elif place=='up':l, b, h, w = .25, .5, .3, .4 # To place the subplot
    ax2 = fig.add_axes([l, b, w, h])
    for i in to_plot:
        params,typ = i
        if typ=='plot': # Used for the first figure of the exercise
            x,y,label=params
            down,up=find_closer(x,xvals)
            ax1.plot(x,y,label=label)
            ax2.plot(x[down:up],y[down:up])
        elif typ=='uncert': # Used for the second figure of the exercise
            x,ymean,yerr = params
            down,up=find_closer(x,xvals)
            ax1.plot(x,ymean,label='Mean value')
            ax2.plot(x[down:up],ymean[down:up])
            ax1.fill_between(x,ymean-yerr,ymean+yerr,color='blue',alpha=0.2,label='Standard deviation (1$\\sigma$)')
            ax2.fill_between(x[down:up],ymean[down:up]-yerr[down:up],ymean[down:up]+yerr[down:up],color='blue',alpha=0.2)
        else: raise ValueError('You need to chose between \'plot\' and \'uncert\' for the type')
    ax1.set_xlabel(xlab, fontsize = 15)
    ax1.set_ylabel(ylab, fontsize=15)
    ax1.legend()
    fig.tight_layout()
    plt.savefig('Exercise/Figures/'+name_fig+'.png')
    plt.show()


def bandwidth(x,y,fraction):
    maximum,idx_max = np.max(y),np.argmax(y)
    down,up = find_nearest(y[:idx_max],fraction*maximum),find_nearest(y[idx_max:],fraction*maximum)
    return np.array([x[down],x[up+idx_max-1]])


if __name__=='__main__':
    x = np.arange(0,2*np.pi,0.01)
    y = -np.cos(x)
    plot_zoom([1,2],[((x,y,'test'),'plot')],xlab='x',ylab='y',place='up')
    