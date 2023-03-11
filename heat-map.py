import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def create_heat_map (data):
    
    ax = sns.heatmap(uniform_data, linewidth=0.5)
    plt.show()
    
uniform_data = np.array([[0,0,0],[0,5,0],[10,5,0],[0,10,5],[0,0,10]])
create_heat_map(data = uniform_data)