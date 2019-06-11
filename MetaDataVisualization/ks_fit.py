import powerlaw
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd
import matplotlib.colors as colors
from matplotlib import cm
from matplotlib.text import Text
import matplotlib as mpl
from collections import defaultdict

plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'

os.chdir(homepath)

with open("OLD/"+"subgraphInDegDistTEST.txt") as sf:
    data_unstriped = sf.readlines()
    data = [int(d.rstrip()) for d in data_unstriped]


reducedDir = Counter(data)
tups = [(k,v) for k,v in reducedDir.items()]
x = [k for k,v in tups]
y = [v for k,v in tups]
ymax = max(y) # I know that this is not the correct normalization, the slope is not affected


fig, ax = plt.subplots()

results = powerlaw.Fit(data)
# ynormalization = (results.alpha-1)/np.power(results.xmin,-results.alpha+1) # xmin

plt.plot(x,np.array(y)/ymax,'.')
xfit = np.array(list(range(1000)))
xmin = results.xmin
yfit = (results.alpha-1)/results.xmin*np.power(xfit/xmin,-results.alpha)
plt.plot(xfit,yfit)

plt.xlabel(r'Indegree')
plt.ylabel(r'Fraction of Nodes')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_aspect(aspect='equal')
ax.legend(("Data","Fit"))
plt.show()

# fit = powerlaw.Fit(data)
# fit.distribution_compare('power_law', 'exponential')
# fit.power_law.plot_pdf( color= 'b',linestyle='--',label='fit ccdf')
# fit.plot_pdf( color= 'g')
# plt.show()