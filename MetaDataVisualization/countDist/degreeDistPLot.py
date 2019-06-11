import powerlaw
import os
import multiprocessing
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


crawldateKey = "2017-06"
datasetKey = "ATSRH/"


#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'
os.chdir(homepath)

# cuts = ["gaw/", "ATSRH/", "NRH/"]
cuts = ["ATSRH/", "NRH/"]
degDistDict = {}
for dataset in cuts:
    os.chdir(homepath+'resultData/MetaData/countDist/degreeDist/'+dataset+'InDeg/')
    dates = sorted(os.listdir("."))
    d={}
    for date in dates:
        with open(date) as dd:
            data_unstriped = dd.readlines()
            data_stripped = [d.rstrip() for d in data_unstriped]
            tupelStr = [line[1:-1].split(',') for line in data_stripped]
            tupelArray = np.array([(int(line[0]),int(line[1])) for line in tupelStr]) #deg = tupelArray[:,0], count  = tupelArray[:,1]

        normalization = tupelArray[:,1].sum()
        yfraction = tupelArray[:,1]/normalization
        xdegree = tupelArray[:,0]

        d[date] = [xdegree,yfraction]

    degDistDict[dataset]=d


resultsPath = homepath+"resultData/MetaData/countDist/powerlawFULLRUN/"
with open(resultsPath+datasetKey+"InDeg/"+crawldateKey) as f:
    lines = f.readlines()
    resultsData = [float(e) for e in lines[0].split(" ")]

alpha = resultsData[0]
sigma = resultsData[1]
xmin= resultsData[2]
xfit = np.array(list(range(1,1000)))
yfit = (alpha-1)/xmin*np.power(xfit/xmin,-alpha)


fig, ax = plt.subplots()
ax.plot(degDistDict[datasetKey][crawldateKey][0],degDistDict[datasetKey][crawldateKey][1],'.')
ax.plot(xfit,yfit,'.')

plt.xlabel(r'Indegree')
plt.ylabel(r'Fraction of Nodes')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_ylim(top=1)
ax.set_aspect(aspect='equal')
ax.legend(("Data","Fit"))

plt.show()

#
# resultsPath = "/home/parism/REGIO/resultData/MetaData/countDist/powerlawFULLRUN/"
# with open(resultsPath+datasetKey+"InDeg/"+crawldateKey) as f:
#     lines = f.readlines()
#     resultsData = [float(e) for e in lines[0].split(" ")]
#
# alpha = resultsData[0]
# sigma = resultsData[1]
# xmin= resultsData[2]
#
# figFit, axFit = plt.subplots()
# xfit = np.array(list(range(1000)))
# yfit = (alpha-1)/xmin*np.power(xfit/xmin,-alpha)
# axFit.plot(xfit,yfit,'.')
# axFit.set_yscale('log')
# axFit.set_xscale('log')
# plt.show()