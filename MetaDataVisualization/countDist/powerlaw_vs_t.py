# (results.alpha,results.sigma,results.xmin)
#1.999002535985063 693.0 0.012294077373599777 None

import powerlaw
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration'
os.chdir(homepath)

os.chdir('resultData/MetaData/countDist/powerlawFULLRUN')
# cuts = ["gaw/","ATSRH/","NRH/"]
cuts = ["ATSRH/","NRH/"]
fig, ax = plt.subplots()
# fig2, ax2 = plt.subplots()
for ic,dataset in enumerate(cuts):
    # dataset = "gaw/"
    degKind = "InDeg/"
    currentPath = dataset+degKind
    dates=sorted(os.listdir(dataset+degKind))
    resultsInfo = {}
    for date in dates[2:]:
        with open(currentPath+date) as df:
            data = df.readlines()
            infoline = [float(e) for e in data[0].split(" ") if not e=='None']

        resultsInfo[date]=infoline

    xfit = np.array(list(range(1000)))

    xcrawldate = []
    yalpha = []
    errSigma = []
    xmin = []
    for date,results in resultsInfo.items():
        dateInFloat = float(date[:4]) + (float(date[5:]) - 1) / 12
        yalpha.append(results[0])
        errSigma.append(results[1])
        xmin.append(results[2])
        xcrawldate.append(dateInFloat)

    # ax.plot(xcrawldate,yalpha,label=r'$\alpha$')
    ax.errorbar(xcrawldate,yalpha,np.array(errSigma)/2,label=dataset[:-1].upper(), color="C"+str(ic) ,
                 ecolor='lightgray', elinewidth=2, capsize=4)
    # ax2.plot(xcrawldate,xmin)
    # xmin = results.xmin
    #yfit = (results.alpha-1)/results.xmin*np.power(xfit/xmin,-results.alpha)
    #plt.plot(xfit,yfit)

plt.xlabel(r'Crawl date')
plt.ylabel(r'Slope $\alpha$ of indegree distribution')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.set_yscale('log')
# ax.set_xscale('log')
# ax.set_aspect(aspect='equal')
# ax.legend([r"gaw","ATSRH","ATSRH $\&$ NRH"],loc='upper center', bbox_to_anchor=(0.5, 1.18),
#           ncol=3, fancybox=True, shadow=True)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.legend([r"ATSRH","ATSRH $\cap$ NRH"],loc='upper center', bbox_to_anchor=(0.5, 1.18),
          ncol=3, fancybox=True, shadow=True)
# ax.set_xlim(left=min(xcrawldate)-0.05)
ax.set_xlim(left=min(xcrawldate)-0.05)
fig.subplots_adjust(left=0.12, right=.99, top=0.83, bottom=0.12)
os.chdir(homepath)
inDegreeimgPath = 'resultDataVisualization/images/MetaData/countDist/degreeDist/'
#
if not os.path.isdir(inDegreeimgPath):
    os.makedirs(inDegreeimgPath)
#
fig.savefig(inDegreeimgPath+'powerlawAlphaFULLRUN2' +'.eps', dpi=300, transpartent=True, bbox_inches='tight')

plt.show()



