import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import defaultdict
import pathlib


from collections import Counter
import datetime

plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# homepath='/home/parism/REGIO/'
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'

dataDir = 'resultData/'
dataSource = 'gaw/'
theme = 'CDXmimedist/'
subDir = 'MetaData/countDist/'
sourcePath = subDir +theme + dataSource


os.chdir(homepath+'resultDataVisualization/scripts')
os.chdir(homepath)

scriptPath = homepath+'resultDataVisualization/scripts/' + subDir

if not os.path.isdir(scriptPath):
    pathlib.Path(scriptPath).mkdir(parents=True)

# crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06']
displayMime = 5

stats={}
dateNames = os.listdir(dataDir+sourcePath)

for date in dateNames:
    with open(dataDir+sourcePath+date) as f:
        year={}
        storage = {}
        records = {}
        data = csv.reader(f, delimiter=',')
        # print(date)
        for i,row in enumerate(reversed(list(data))):
        # for i,row in enumerate(data):
                keyName = ",".join(row[0:-2])
                storage[keyName] = float(row[-2])
                records[keyName] = float(row[-1])
        year["storage"] = storage
        year["records"] = records
        stats[date]=year

years = list(stats.keys())


# MimeKeys = ["records","storage"]
MimeKeys = ["records","storage"][::-1]

for key in MimeKeys:
    stackArray = []
    xticks = []
    byMime = {}

    mimeInYear = set(stats[years[0]][key].keys())
    for year in stats:
        mimeInYear = mimeInYear.intersection(set(stats[year][key].keys()))

    relevantMime = mimeInYear
    if (relevantMime.__contains__('other')):
        relevantMime.remove('other')

    byMime = defaultdict(list)

    for year, v in sorted(stats.items()):
        storage = v[key]
        totalDisplaySize = 0
        totalSize = 0
        for mime, size in storage.items():
            totalSize+=size
            if mime in relevantMime:
                byMime[mime].append(size)
                totalDisplaySize += size
        byMime['other'].append(totalSize-totalDisplaySize)
        xticks.append(year)

    for mime, array in byMime.items():
        stackArray.append(array)


    # Dataset
    df = pd.DataFrame(np.array(stackArray).transpose(), columns=list(byMime.keys()))
    xticksPos = [float(e[:4])+(float(e[5:])-1)/12 for e in xticks]
    xticksLab = xticks


    othersSum = df.iloc[:,displayMime::].sum(1)
    dfPlot = df.iloc[:,0:displayMime-1]
    dfPlot['other'] = othersSum
    df_ = dfPlot


    # plot
    fig, ax = plt.subplots()
    ax.set_xlabel("Crawl date")
    if key == 'records':
        ax.set_ylabel("Records (in million)")
        polys = ax.stackplot(xticksPos, df_.T/10**6)
    elif key == 'storage':
        ax.set_ylabel("Compressed size (in TB)")
        polys = ax.stackplot(xticksPos, df_.T/2**40)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)

    #legend
    legendProxies = []
    for poly in polys:
        legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=poly.get_facecolor()[0]))
    lgendLabels = list(df_.keys())
    # plt.legend(legendProxies, lgendLabels,loc=4)
    plt.legend(legendProxies,lgendLabels, loc='upper center', bbox_to_anchor=(0.5, 1.25),
              ncol=3, fancybox=True, shadow=True)
    plt.margins(0,0)


    #export figs
    imgDir = 'resultDataVisualization/images/'
    imgPath = imgDir + sourcePath

    if not os.path.isdir(imgPath):
        pathlib.Path(imgPath).mkdir(parents=True)
    plt.savefig(imgPath + key+ '.svg', dpi=300, transpartent=True,bbox_inches='tight')
    plt.savefig(imgPath + key+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')

    #show fig
    plt.show()

    #plot normalized stack
    normalizedDF = df_.div(df_.sum(axis=1), axis=0)

    # plot
    figNormal, axNormal = plt.subplots()
    axNormal.set_xlabel("Crawl date")
    if key == 'records':
        axNormal.set_ylabel("Captures (normalized)")
        polys = axNormal.stackplot(xticksPos, normalizedDF.T)
    elif key == 'storage':
        axNormal.set_ylabel("Compressed size (normalized)")
        polys = axNormal.stackplot(xticksPos, normalizedDF.T)

    axNormal.spines['right'].set_visible(False)
    axNormal.spines['top'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)

    #legend
    legendProxies = []
    for poly in polys:
        legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=poly.get_facecolor()[0]))
    lgendLabels = list(normalizedDF.keys())
    # plt.legend(legendProxies, lgendLabels,loc=4)
    axNormal.legend(legendProxies,lgendLabels, loc='upper center', fontsize=12, bbox_to_anchor=(0.5, 1.25),
              ncol=3, fancybox=True, shadow=True)
    figNormal.subplots_adjust(left=0.12, right=.99, top=0.83, bottom=0.12)
    axNormal.margins(0,0)

    #export figs
    imgDir = 'resultDataVisualization/images/'
    imgPath = imgDir + sourcePath

    if not os.path.isdir(imgPath):
        pathlib.Path(imgPath).mkdir(parents=True)
    # plt.savefig(imgPath + key+'_normalized' + '.svg', dpi=300, transpartent=True,bbox_inches='tight')
    figNormal.savefig(imgPath + key+'_normalized' + '.eps', dpi=300, transpartent=True,bbox_inches='tight')

    #show fig
    plt.show()


averageSTD = np.array([normalizedDF[i].std() for i in normalizedDF]).mean()