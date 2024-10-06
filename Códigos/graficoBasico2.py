import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax, data1, data2, param_dict):  
    # A helper function to make a graph.
    out = ax.plot(data1, data2, **param_dict)   
    return out# make 4 random data sets

data1, data2, data3, data4 = np.random.randn(4, 100) 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
plt.show()