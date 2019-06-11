import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import defaultdict
import pathlib
import matplotlib.colors as colors


homepath='/home/parism/REGIO/'

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
displayMime = 2
# displayMime = 10

# create a decent data set
def PLDwiseDict():
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

    #merge the two source types
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
    return PLDwiseDict

PLDwiseDict = PLDwiseDict()

#pad missing mimeTypes
PLDwiseDictPadded = PLDwiseDict.copy()
sourceTypes = ['records','storage']
for sourceType in sourceTypes:
    for pldsurt, crawls in PLDwiseDictPadded.items():
        allMimeTypesInpldsurt = set.union(*[set(series[sourceType].keys()) for date, series in crawls.items()])
        for date, series in crawls.items():
            missingKeys = allMimeTypesInpldsurt.difference(set(series[sourceType].keys()))
            d = {}
            for key in missingKeys:
                d[key] = 0
            series[sourceType].update(d)


#pad missing dates
allDates = set.union(*[set(crawls.keys()) for pld, crawls in PLDwiseDictPadded.items()])
for pldsurt, crawls in PLDwiseDictPadded.items():
    missingDate = allDates.difference(set(crawls.keys()))
    filling_dict = dict.fromkeys(crawls[list(crawls.keys())[0]]['records'], 0)
    d={}
    d['records'] = filling_dict
    d['storage'] = filling_dict
    for date in missingDate:
        crawls[date] = d



selectedPLD = []
for key in PLDwiseDictPadded.keys():
    if key.__contains__(','):
        selectedPLD.append(key)


total = 0
i = 0
legendkeys = []
a1=[]
a2=[]
fig, ax = plt.subplots()
for key in selectedPLD:
    plotableSeries = sorted([[float(date[:4])+(float(date[5:])-1)/12,series['records']['text/html']] for date, series in PLDwiseDictPadded[key].items()],key=lambda x:x[0])
    # if plotableSeries[6][1]>4000000:
    if plotableSeries[6][1]>-1:
    # if plotableSeries[6][1]>1000 & plotableSeries[6][1]<4000000:
        i += 1
        total += plotableSeries[6][1]
        legendkeys.append(key)
        dates = [date for date, y in plotableSeries]
        ys = [y for date, y in plotableSeries]
        ax.plot(dates,ys)
        a1.append(dates)
        a2.append(ys)

ax.margins(0,0)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.autoscale(tight=True)
# ax.legend(legendkeys)
plt.show()


totalPLDs = legendkeys.__len__()
fhg = [key for key in legendkeys if key.__contains__('fraunhofer')].__len__()
mpg = [key for key in legendkeys if key.__contains__('mpg')].__len__()

rest = [key for key in legendkeys if not (key.__contains__('mpg') | key.__contains__('fraunhofer'))].__len__()

PLDwiseDictPadded_filtered = {pld: crawls for pld,crawls in PLDwiseDictPadded.items() if  (pld.__contains__('fraunhofer') | pld.__contains__('mpg') | pld.__contains__('mpi'))}


#normalized mimeTypes -> #records in mimeType of PLD/#records total of PLD
sourceType = 'records'
mimeType = 'text/html'
mimeSeriesNormalized_pldwise = {}
emptyPLDs = {}
for pld, crawls in PLDwiseDictPadded_filtered.items():
    mimeSeriesNormalized = []
    for date, series in crawls.items():
        total = sum(list(series[sourceType].values()))
        if total != 0:
           mimeSeriesNormalized.append((series[sourceType][mimeType]/total,total))
        else:
           mimeSeriesNormalized.append((series[sourceType][mimeType],total))
    mimeSeriesNormalized_pldwise[pld]=np.array(mimeSeriesNormalized)



figCorr, axCorr = plt.subplots()

im = axCorr.matshow(np.corrcoef(np.array([ e[:,0] for e in list(mimeSeriesNormalized_pldwise.values())])), origin='lower', cmap=plt.get_cmap('RdYlBu'), interpolation='nearest')#, norm=colors.PowerNorm(gamma=1./10.))
# im = axCorr.matshow(np.corrcoef(np.array([ e[:,0] for e in list(mimeSeriesNormalized_pldwise.values())]).T))#, origin='lower', cmap=plt.get_cmap('RdYlBu'), interpolation='nearest')#, norm=colors.PowerNorm(gamma=1./10.))
# axCorr.invert_yaxis()
cb = fig.colorbar(im)

axCorr.xaxis.tick_bottom()
axCorr.tick_params(axis=u'both', which=u'both',length=0)
plt.margins(0,0)

for key,axe in axCorr.spines.items():
    axe.set_visible(False)
plt.show()


#### PLDwise volatility window 3
volatility = {}
normalizedVolatility = {}
windowSize = 3

for pld, tupleSeries in mimeSeriesNormalized_pldwise.items():
    MimeTypeTrend = [tup[0]*tup[1] for tup in tupleSeries]
    normalizedMimeTypeTrend = tupleSeries[:,0]
    volatility[pld] = pd.Series(MimeTypeTrend).rolling(windowSize).std(1)
    # volatility[pld] = [np.array(MimeTypeTrend[i:i+windowSize]).std() for i,e in enumerate(MimeTypeTrend) if i+windowSize <= MimeTypeTrend.__len__()]
    normalizedVolatility[pld] = pd.Series(normalizedMimeTypeTrend).rolling(windowSize).std(1)
    # normalizedVolatility[pld] = [np.array(normalizedMimeTypeTrend[i:i+windowSize]).std() for i,e in enumerate(normalizedMimeTypeTrend) if i+windowSize <= normalizedMimeTypeTrend.__len__()]



figVolatility, axVolatility = plt.subplots()
for pld, volatilitySeries in normalizedVolatility.items():
    axVolatility.plot(range(np.array(volatilitySeries[windowSize-1::]).__len__()),np.array(volatilitySeries[windowSize-1::]))

ax.margins(0,0)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.autoscale(tight=True)
# ax.legend(legendkeys)
plt.show()


figVolatilitySum, axVolatilitySum = plt.subplots()
axVolatilitySum.plot(sum(normalizedVolatility.values()))
axVolatilitySum.spines['right'].set_visible(False)
axVolatilitySum.spines['top'].set_visible(False)
axVolatilitySum.margins(0,0)
# axVolatilitySum.autoscale(tight=True)
plt.show()

