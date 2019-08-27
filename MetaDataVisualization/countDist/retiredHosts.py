# (170555327,151114317,17043273)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import os
from matplotlib.text import Text
import matplotlib as mpl
from collections import defaultdict
from collections import Counter
import datetime
from matplotlib.ticker import FuncFormatter

plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

def number_formatter(number, pos=None):
    """Convert a number into a human readable format."""
    magnitude = 0
    while abs(number) >= 1000:
        magnitude += 1
        number /= 1000.0
    return '%.1f%s' % (number, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])


import os


# homepath='/home/parism/REGIO/'
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'
os.chdir(homepath +"resultData/MetaData/countDist/retiredHost/")

dates = os.listdir(".")
dataAsArray = []
for date in dates:
    with open(date) as f:
        data = f.readlines()
        cleanData = [line.rstrip()[1:-1].split(",") for line in data][0]
        countTot = int(cleanData[0])
        countUniqueSurt = int(cleanData[1])
        countretHost = int(cleanData[2])
        dateInFloat = float(date[:4]) + (float(date[5:]) - 1) / 12
        dataAsArray.append([dateInFloat,countTot,countUniqueSurt,countretHost])

dfCoherence = np.array(sorted(dataAsArray, key=lambda x:x[0]))

n=dates.__len__()
colorMap = 'RdYlBu'
color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
legendProxies = []
legendKeys = []

fig, ax = plt.subplots()
ax.plot(dfCoherence[:,0],dfCoherence[:,1])
ax.plot(dfCoherence[:,0],dfCoherence[:,2],'--')
ax.plot(dfCoherence[:,0],dfCoherence[:,3],'-.')
ax.set_xlabel(r'Crawl date')
ax.set_ylabel(r'$\#$ Captures')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# ax.legend(['Unique URLs','Unique SURTs','Retired Hosts'])
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.1,
#                  box.width, box.height * 0.9])
# ax.legend(['Unique URLs','Unique SURTs','Retired Hosts'],loc='upper center', bbox_to_anchor=(0.5, -0.05),
#           fancybox=True, shadow=True, ncol=5)
ax.legend(['Unique URLs','Unique SURTs','Retired hosts'],fontsize=12, loc='upper center', bbox_to_anchor=(0.5, 1.19),
          ncol=3,columnspacing=1, markerscale=0.3, fancybox=True, shadow=True)
ax.set_ylim(bottom=0)
ax.set_xlim(left=dfCoherence[:,0][0],right=dfCoherence[:,0][-1])
# ax.set_aspect(aspect='equal')
os.chdir(homepath+"resultDataVisualization/images/MetaData/countDist")
inDegreeimgPath = 'retiredHost/retiredHost'
#ax.yaxis.set_major_formatter(FuncFormatter(number_formatter))
fig.subplots_adjust(left=0.12, right=.99, top=0.83, bottom=0.12)

fig.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
fig.savefig(inDegreeimgPath + '.png', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()



averageRedundancySurt = (1-(dfCoherence[:,2]/dfCoherence[:,1])).mean()
stdRedundancySurt = (1-(dfCoherence[:,2]/dfCoherence[:,1])).std()


dfCoherence_afterRemoval = dfCoherence[2:,:]
averageRedundancySurt_afterRemoval = (1-(dfCoherence_afterRemoval[:,2]/dfCoherence_afterRemoval[:,1])).mean()
stdRedundancySurt_afterRemoval = (1-(dfCoherence_afterRemoval[:,2]/dfCoherence_afterRemoval[:,1])).std()


surtToURLdiff = ((dfCoherence[:,1]-dfCoherence[:,2])/dfCoherence[:,1])[0:].mean() # from 2012-10, which is intended