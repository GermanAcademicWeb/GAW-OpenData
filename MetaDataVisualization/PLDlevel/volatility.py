import csv
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import defaultdict
import pathlib
from matplotlib.patches import Ellipse
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

#homepath
homepath = '/home/parism/PhD/REGIO/GAW_visualization_python/ProjectComparabilityAndExploration/'

os.chdir(homepath +'resultData/MetaData/seeds')
ls = os.listdir(".")

seeds = [e for e in ls if e.__contains__(".seeds")]

seedDict ={}
for seed in sorted(seeds):
    with open(seed) as sf:
        lines = sf.readlines()
        seedData = set([",".join(line.rstrip().split(".")[::-1]) for line in lines])
        seedDict[seed.split('.seeds')[0]] = seedData


seedIntersection = seedDict["2013-12"]

for date, seeds in seedDict.items():
    seedIntersection = seedIntersection.intersection(seeds)


# homepath='/home/parism/REGIO/'

dataDir = 'resultData/'
dataSource = 'gaw/'
theme = 'CDXmimedist/'
subDir = 'MetaData/PLDlevel/bySurt/' #resultData/MetaData/PLDlevel/bySurt/gaw/CDXmimedist
sourcePath = subDir + dataSource + theme


os.chdir(homepath+'resultDataVisualization/scripts')
# os.chdir(homepath)

scriptPath = homepath+'resultDataVisualization/scripts/' + subDir

if not os.path.isdir(scriptPath):
    pathlib.Path(scriptPath).mkdir(parents=True)


displayMime = 2

os.chdir(homepath)
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



## volatility
## create dataframe mime vs date, quasi matrix

PLDtoFrameDict = {}
for pld, crawlsDict in PLDwiseDictPadded.items():
    d={}
    if pld in seedIntersection:
        for date, sourceDict in crawlsDict.items():
            d[date]=sourceDict['records']
    PLDtoFrameDict[pld]=d

PLDdf = {pld: pd.DataFrame(frameDict).T for pld, frameDict in PLDtoFrameDict.items() }

#### perform a calculation on pld data frame, take only the top and previously mentions types if available
#### ["text/html","image/gif","application/pdf","image/png","image/jpeg",]
relevantMimes = ["text/html","image/gif","application/pdf","image/jpeg","other"]
reducedDF = {}
for pld, df in PLDdf.items():
    if pld in seedIntersection:
        a = df.filter(items=["text/html","image/gif","application/pdf","image/jpeg",])
        other = df.drop(["text/html", "image/gif", "application/pdf", "image/jpeg", ], axis=1).sum(1)
        a["other"] = other
        reducedDF[pld]=a


reducedDF2 = {pld:mimeDF.iloc[2:] for pld, mimeDF in reducedDF.items()}
# ATSRH without 2012-10 and 2013-02 in reducedDF2
reducedDF = reducedDF2


dateComposition = {}
pldVar = {}

countTotalInPLD = np.array([dfmime.sum(1) for pld,dfmime in reducedDF.items()]).T
countTotalInYear = [e.sum() for e in countTotalInPLD]
# mimeType = "text/html"

pldkeys = list(reducedDF.keys().__iter__())
crawlDates = list(reducedDF[reducedDF.keys().__iter__().__next__()].transpose().keys().__iter__())
d = {}
for date in crawlDates:
    for key in pldkeys:
        dfmime = reducedDF[key]
        dfmimeTransposed = dfmime.transpose()
        mimeSeries = dfmimeTransposed[date]
        d[key] = mimeSeries
    dateComposition[date] = pd.DataFrame(d)
    d={}




dateCompositionReduced = {date:pldmimeframe for date, pldmimeframe in dateComposition.items() if not (date == "2012-10" or date == "2013-02")}

dateComposition = dateCompositionReduced

equalWeight = {}
equalWeightStd = {}
weighted = {}
weightedStd = {}
for date, pldmimeframe in dateComposition.items():
    totalrecordCount = pldmimeframe.sum().sum()
    totalpldCount = pldmimeframe.__len__()
    pldweight = pldmimeframe.sum(0)/totalrecordCount

    #(pldmimeframe/pldmimeframe.sum(0)).sum(0) =[1, 1 ...]
    normalizedInPLDFrame = pldmimeframe/pldmimeframe.sum(0)

    averageMimeFraction = normalizedInPLDFrame.mean(1)
    averageMimeFractionStd = normalizedInPLDFrame.std(1)
    averageMimeFractionweighted = ((normalizedInPLDFrame*pldweight).mean(1)/((normalizedInPLDFrame*pldweight).mean(1)).sum(0))
    averageMimeFractionweightedStd = ((normalizedInPLDFrame*pldweight).std(1)/((normalizedInPLDFrame*pldweight).mean(1)).sum(0))
    equalWeight[date] = averageMimeFraction
    equalWeightStd[date] = averageMimeFractionStd
    weighted[date] = averageMimeFractionweighted
    weightedStd[date] = averageMimeFractionweightedStd


equalWeightDF = pd.DataFrame(equalWeight)
equalWeightStdDF = pd.DataFrame(equalWeightStd)
weightedDF = pd.DataFrame(weighted)
weightedStdDF = pd.DataFrame(weightedStd)

# plot
xticksPos = [float(e[:4])+(float(e[5:])-1)/12 for e in equalWeightDF.keys()]

figNormal, axNormal = plt.subplots()
axNormal.set_xlabel("Crawl date")
axNormal.set_ylabel("Average fraction in PLD")
axNormal.plot(xticksPos, list(equalWeightDF.T['text/html']), color="C0")
axNormal.plot(xticksPos, list(weightedDF.T['text/html']),'--', color="C0")
axNormal.plot(xticksPos, list(equalWeightDF.T['image/jpeg']), color="C1")
axNormal.plot(xticksPos, list(weightedDF.T['image/jpeg']),'--', color="C1")


axNormal.legend(["text/html","text/html weighted","image/jpeg","image/jpeg weighted"],loc='upper center', bbox_to_anchor=(0.5, 1.18),
          ncol=2, fancybox=True, shadow=True)
axNormal.set_xlim(left=min(xticksPos)-0.05)

axNormal.spines['right'].set_visible(False)
axNormal.spines['top'].set_visible(False)
plt.show()


PLDstd = {}
#### std shift with total number of records
for pld, mimeDF in reducedDF.items():
    normalizedPLD = mimeDF.transpose() / mimeDF.sum(1)
    stdOfPLDoverAllTime = normalizedPLD.std(1)
    averagetotalCountperCrawl = mimeDF.transpose().mean(1)
    PLDstd[pld]=np.array([list(averagetotalCountperCrawl),list(stdOfPLDoverAllTime)])


fig, ax = plt.subplots()

stdplotList = []
recCountplotList = []
for pld, v in PLDstd.items():
    stdplotList.append(v[1])
    recCountplotList.append(v[0])


stdplot = np.array(stdplotList).T
recCountplot = np.array(recCountplotList).T

# text/html
# all
mimeList = ["text/html","image/gif","application/pdf","image/jpeg","other"]
plotDict = {mime: [rec,std] for mime,rec,std in zip(mimeList,recCountplot,stdplot)}

xStd = np.array(list(range(0,1000000,10)))
yStd = np.power(xStd,0.5)

# for mime, v in plotDict.items():
#     #ax.plot(recCountplot[:,0],stdplot[:,0],'.')
#     if mime == "other":
#         continue
#     else:
#         recCount = v[0]
#         std = v[1]
#         ax.plot(recCount,std,'.',label=mime,markersize=14)
ax.plot(plotDict["text/html"][0],plotDict['text/html'][1],'.',label="text/html",markersize=12,color="C0")
ax.plot(plotDict["image/jpeg"][0],plotDict["image/jpeg"][1],'<',label="image/jpeg",markersize=6,color="C1")
ax.plot(plotDict["image/gif"][0],plotDict["image/gif"][1],'<',label="image/gif",markersize=6,color="C2")
ax.plot(plotDict["application/pdf"][0],plotDict["application/pdf"][1],'.',label="application/pdf",markersize=12,color="C3")
ax.plot(plotDict["other"][0],plotDict["other"][1],'x',label="other",markersize=6,color="C4")
#ax.plot(xStd,yStd/yStd.max(),'-.',color='C6')

ax.set_xlabel(r"Average $\#$ captures/snapshot")
ax.set_ylabel(r"Standard deviation of MIME type fraction")

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2),
          ncol=3,columnspacing=1, markerscale=1, fancybox=True, shadow=True)

# ax.legend(loc='upper center', fontsize=12, bbox_to_anchor=(0.5, 1.25),
#                 ncol=3, fancybox=True, shadow=True)
fig.subplots_adjust(left=0.12, right=.99, top=0.83, bottom=0.12)
axNormal.margins(0, 0)

#ax.set_xlim(left=min(xticksPos)-0.05)
#ax.set_ylim(bottom=0)
ax.set_xscale('log')
ax.set_yscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

imgPath = homepath+'resultDataVisualization/images/MetaData/PLDlevel/mimecomposition/'
#
if not os.path.isdir(imgPath):
    os.makedirs(imgPath)
#
fig.savefig(imgPath+'std_vs_records' +'.eps', dpi=300, transpartent=True, bbox_inches='tight')

plt.show()



figCap, axCap = plt.subplots()

y = sorted([frame.sum(1).mean() for pld,frame in reducedDF.items()],reverse=True)
axCap.plot(y,'.',color='C6',label="Average captures on PLD")

axCap.set_xlabel(r"Rank by count of PLDs")
axCap.set_ylabel(r"Average $\#$ captures/snapshot")

axCap.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2),
          ncol=3,columnspacing=1, markerscale=1, fancybox=True, shadow=True)

figCap.subplots_adjust(left=0.12, right=.99, top=0.83, bottom=0.12)
axCap.margins(0, 0)
#axCap.set_xscale('log')
axCap.set_xlim(left=-0.05)
axCap.set_ylim(top=max(y)*(1.05))

axCap.spines['right'].set_visible(False)
axCap.spines['top'].set_visible(False)
axCap.yaxis.set_major_formatter(FuncFormatter(number_formatter))

imgPath = homepath+'resultDataVisualization/images/MetaData/PLDlevel/count/'
#
if not os.path.isdir(imgPath):
    os.makedirs(imgPath)
#
figCap.savefig(imgPath+'averageCapture' +'.eps', dpi=300, transpartent=True, bbox_inches='tight')


plt.show()






#
# def eigsorted(cov):
#     vals, vecs = np.linalg.eigh(cov)
#     order = vals.argsort()[::-1]
#     return vals[order], vecs[:,order]
#
# nstd = 2
# #fig, ax = plt.subplot(111)
#
# cov = np.cov(plotDict["application/pdf"][0],plotDict["application/pdf"][1])
# vals, vecs = eigsorted(cov)
# theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
# w, h = 2 * nstd * np.sqrt(vals)
# ell = Ellipse(xy=(plotDict["application/pdf"][0].mean(),plotDict["application/pdf"][1].mean()),
#               width=w, height=h,
#               angle=theta.__float__(), color='black')
# ell.set_facecolor('none')
# ell.set_alpha(0.2)
# ell.width
# ax.add_artist(ell)
