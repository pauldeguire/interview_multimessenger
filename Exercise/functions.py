import numpy as np
from matplotlib import pyplot as plt


def find_closer(array,braket):
    """
    Input: An array as well as a list [val_down,val_up] for the interval
    Output: A list [down,up] with index values from the initial array
    """
    idx_min,idx_max = (np.abs(array - braket[0])).argmin(),(np.abs(array - braket[1])).argmin()
    return [idx_min,idx_max+1]


def plot_zoom(xvals,to_plot,xlab='Frequency (Hz)',ylab='Amplification magnitude'):
    """
    Input:
    Output:
    """
    fig, ax1 = plt.subplots(figsize=(9,4))
    l, b, h, w = .25, .3, .3, .4
    ax2 = fig.add_axes([l, b, w, h])
    for i in to_plot:
        params,typ = i
        if typ=='plot':
            x,y,label=params
            down,up=find_closer(x,xvals)
            ax1.plot(x,y,label=label)
            ax2.plot(x[down:up],y[down:up])
        elif typ=='uncert':
            x,ymean,yerr = params
            down,up=find_closer(x,xvals)
            ax1.plot(x,ymean,label='Mean value')
            ax2.plot(x[down:up],ymean[down:up])
            ax1.fill_between(x,ymean-yerr,ymean+yerr,color='blue',alpha=0.2,label='Standard deviation (1$\\sigma$)')
            ax2.fill_between(x[down:up],ymean[down:up]-yerr[down:up],ymean[down:up]+yerr[down:up],color='blue',alpha=0.2)
    ax1.set_xlabel(xlab, fontsize = 15)
    ax1.set_ylabel(ylab, fontsize=15)
    ax1.legend()
    fig.tight_layout()
    plt.show()


if __name__=='__main__':
    x = np.arange(0,2*np.pi,0.01)
    y = -np.cos(x)
    plot_zoom([1,2],[((x,y,'test'),'plot')],xlab='x',ylab='y')
    