import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import defaultdict
import pathlib


# homepath='/home/parism/REGIO/'

dataDir = 'resultData/'
dataSource = 'gaw/'
theme = 'CDXmimedist/'
subDir = 'MetaData/PLDlevel/bySurt/'
sourcePath = subDir + dataSource + theme


os.chdir(homepath+'resultDataVisualization/scripts')
os.chdir(homepath)

scriptPath = homepath+'resultDataVisualization/scripts/' + subDir

if not os.path.isdir(scriptPath):
    pathlib.Path(scriptPath).mkdir(parents=True)

# crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06']
# displayMime = 2
displayMime = 10

stats={}
alltimePLDs = set
dateNames = sorted(os.listdir(dataDir+sourcePath))
seriesType = ["records","storage"]
for key in seriesType:
    snapshotsDict = {}
    for date in dateNames:
        with open(dataDir+sourcePath+date) as f:
            dataText = f.readlines()
            PLDDict = {}
            for dataLine in dataText:
                PLDmimeList = dataLine.split(',List(')
                PLD = PLDmimeList[0][1::]
                mimeListText = PLDmimeList[1].rstrip()[0:-3]
                mimeList = mimeListText.split('), ')
                MimeDict = {}
                for mime in mimeList:
                    cleanmime = mime[1::]
                    mimeCSrec = cleanmime.split(',')
                    mimeType = ','.join(mimeCSrec[0:-2])
                    if key == 'storage':
                        compSize = int(mimeCSrec[-2])
                        MimeDict[mimeType] = compSize
                    elif key == 'records':
                        recCount = int(mimeCSrec[-1])
                        MimeDict[mimeType] = recCount
                PLDDict[PLD] = MimeDict
                alltimePLDs = alltimePLDs.union(set([PLD]))
        snapshotsDict[date] = PLDDict
    stats[key] = snapshotsDict


sourceType = 'records'
PLDwiseDict_rec = {}
for PLDwiseKey in alltimePLDs:
    d={}
    for date, vsnapshotsDict in stats[sourceType].items():
        for pldsurt, mimeDist in vsnapshotsDict.items():
            if PLDwiseKey == pldsurt:
                d.update( {date:{sourceType:mimeDist}})
        PLDwiseDict_rec.update({PLDwiseKey:d})

sourceType = 'storage'
PLDwiseDict = {}
for PLDwiseKey in alltimePLDs:
    d={}
    for date, vsnapshotsDict in stats[sourceType].items():
        for pldsurt, mimeDist in vsnapshotsDict.items():
            if PLDwiseKey == pldsurt:
                d.update( {date:{sourceType:mimeDist}})
                PLDwiseDict.update({PLDwiseKey:d})

for pld, crawls in PLDwiseDict.items():
    for date, sourceSeries in crawls.items():
        # for pld_rec, crawls_rec in PLDwiseDict_rec.items():
        #     for date_rec, sourceSeries_rec in crawls_rec.items():
        #
        PLDwiseDict[pld][date].update(PLDwiseDict_rec[pld][date])





def plotMimeDist(pldsurt,PLDwiseDict):
    MimeKeys = ["records","storage"]
    # MimeKeys = ["records"]
    stats = PLDwiseDict[pldsurt]

    for key in MimeKeys:
        stackArray = []
        xticks = []
        byMime = {}

        mimeInDate = set(stats[dateNames[0]][key].keys())
        for year in stats:
            mimeInDate = mimeInDate.intersection(set(stats[year][key].keys()))

        relevantMime = mimeInDate
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
        ax.set_xlabel("Date of crawl")
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
        plt.legend(legendProxies, lgendLabels,loc=4)

        plt.margins(0,0)


        #export figs
        imgDir = 'resultDataVisualization/images/'
        imgPath = imgDir + sourcePath + pldsurt +'/'

        if not os.path.isdir(imgPath):
            pathlib.Path(imgPath).mkdir(parents=True)
        plt.savefig(imgPath + key+ '.svg', dpi=300, transpartent=True)
        # plt.savefig(imgPath + key+ '.png', dpi=300, transpartent=True)

        #show fig
        plt.show()


for pldsurt,crawls in PLDwiseDict.items():
    plotMimeDist(pldsurt,PLDwiseDict)