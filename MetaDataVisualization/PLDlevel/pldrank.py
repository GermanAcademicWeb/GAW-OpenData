import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import defaultdict
import pathlib
from matplotlib.patches import Ellipse
from matplotlib.ticker import FuncFormatter
from matplotlib import cm

def number_formatter(number, pos=None):
    """Convert a number into a human readable format."""
    magnitude = 0
    while abs(number) >= 1000:
        magnitude += 1
        number /= 1000.0
    return '%.1f%s' % (number, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])


plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})



datasets = ["ATSRH/","NRH/"]
facecolors = ["lightgray","gray"]
alphas = [0.15,0.1]
# datasets = ["gaw/"]

crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06','2018-12']
colorMap = 'RdYlBu'
n=12
SD_cut = 12
# color_sequence = [cm.get_cmap('Greys')(i) for i in (np.linspace(20,200,n)/255)]
# color_sequence = [cm.get_cmap('YlGnBu')(i) for i in (np.linspace(20,200,n+1)/255)]
color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]

#homepath
homepath = '/home/parism/PhD/REGIO/GAW_visualization_python/ProjectComparabilityAndExploration/'


fig2, ax2 = plt.subplots()
for a,fc,dataset in zip(alphas,facecolors,datasets):
    os.chdir(homepath+'resultData/MetaData/PLDlevel/pldcaptures/' + dataset)
    dates = sorted(os.listdir("."))
    pldaverage = defaultdict(list)
    for date in dates:
        with open(date) as f:
            lines = f.readlines()
            pldandcount = [line.lstrip()[1:-2].split(",") for line in lines]
            for e in pldandcount:
                pld = ",".join(e[0:-1])
                count = int(e[-1])
                pldaverage[pld].append(count)

    plotdata = np.array(sorted([[np.array(c).mean(),np.array(c).std()] for pld,c in pldaverage.items()],key=lambda x:x[0],reverse=True))
    # ax2.errorbar(list(range(plotdata[:,1].__len__())), plotdata[:,0], plotdata[:,1]/ 2, color="C" + str(icolor), ecolor='lightgray', elinewidth=2, capsize=4)
    # ax2.errorbar(list(range(plotdata[:,1].__len__())), plotdata[:,0], plotdata[:,1]/ 2,linestyle=':')
    # plt.show()

    y1 = plotdata[:,0] + plotdata[:,1]/ 2
    y2 = plotdata[:,0] - plotdata[:,1]/ 2


    ax2.plot(list(range(plotdata[:,1].__len__())),  plotdata[:,0], '.')
    # ax2.plot(list(range(plotdata[:,1].__len__())), y1, 'w--')
    # ax2.plot(list(range(plotdata[:,1].__len__())), y2, 'w--')
    # ax2.fill_between(list(range(plotdata[:,1].__len__())), y1, y2, facecolor="lightgray", alpha=0.15)
    ax2.fill_between(list(range(plotdata[:,1].__len__())), y1, y2, facecolor=fc, alpha=a)


ax2.yaxis.set_major_formatter(FuncFormatter(number_formatter))
ax2.set_ylabel(r'Captures')
ax2.set_xlabel(r'Rank of PLD by $\#$ captures')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.legend(["ATSRH","ATSRH $\cap$ NRH"],loc='upper center', bbox_to_anchor=(0.5, 1.1),   ncol=2, fancybox=True, shadow=True)
# ax2.legend()
# ax2.set_ylim(bottom=0)
ax2.set_xlim(left=-2,right=max(list(range(plotdata[:,1].__len__())))+0.05)
os.chdir(homepath+"resultDataVisualization/images/MetaData/PLDlevel/pldcaptures/")
inDegreeimgPath = 'averageCapture'
fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()
