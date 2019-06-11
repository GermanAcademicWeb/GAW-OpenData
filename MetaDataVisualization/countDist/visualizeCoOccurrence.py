import powerlaw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
from matplotlib.text import Text

crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06']


#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'


os.chdir(homepath+'resultData/MetaData/countDist/')

dataSource = 'gaw'

# coOccurrenceBasePath = '../urlPermanence/'+ dataSource


plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

coOccurrenceMatrix = []
with open("coOccurrenceMatrix.txt") as f:
    for l in f:
        coOccurrenceLine = [int(e) for e in l.split("(")[1].split(")")[0].split(",")]
        coOccurrenceMatrix.append(coOccurrenceLine)

normalizedcoOccurrenceMatrix = []
for i, l in enumerate(coOccurrenceMatrix):
    max = l[i]
    normalizedLine = [e/max for e in l]
    normalizedcoOccurrenceMatrix.append(normalizedLine)

normalizedcoOccurrenceMatrix=normalizedcoOccurrenceMatrix
fig, ax = plt.subplots()

# im = ax.matshow(normalizedcoOccurrenceMatrix, origin='lower', cmap=plt.get_cmap('RdYlBu'), interpolation='nearest', vmin=0, vmax=0.5)
# cb = fig.colorbar(im)
im = ax.matshow(normalizedcoOccurrenceMatrix, origin='lower', cmap=plt.get_cmap('RdYlBu'), interpolation='nearest', norm=colors.PowerNorm(gamma=1./3.))
cb = fig.colorbar(im,ticks=np.array(list(range(11)))/10)

ax.xaxis.tick_bottom()
ax.set_xticks(list(range(0,crawlDate.__len__(),2)))
ax.set_xticklabels(crawlDate[::2])
ax.set_yticks(list(range(0,crawlDate.__len__(),2)))
ax.set_yticklabels(crawlDate[::2])
#ax.tick_params(axis=u'both', which=u'both',length=0)
#plt.margins(0,0)
plt.xticks(rotation=-45)
# normalizedcoOccurrenceMatrix
plt.xlabel(r'Crawl date')
plt.ylabel(r'Crawl date')

for key,axe in ax.spines.items():
    axe.set_visible(False)

# oldTicks = cb.ax.get_yticks()
# newTicks = np.concatenate((np.array([0]),oldTicks))
cb.outline.set_visible(False)

#cb.ax.tick_params(axis=u'both', which=u'both',length=0)

# oldTicksLabels = cb.ax.get_yticklabels()
# newTicksLabels = [Text(1,0.0,'0.0')]
# newTicksLabels.append(oldTicksLabels)
# cb.ax.set_yticklabels([str(e) for e in newTicks])
#plt.gcf().subplots_adjust(bottom=0.15)
os.chdir(homepath+"resultDataVisualization/images/MetaData/countDist")
imgPath = 'intersection_matSurts'
# plt.savefig(imgPath + '.svg', dpi=300,bbox_inches='tight', transpartent=True)
plt.savefig(imgPath + '.eps', dpi=300,bbox_inches='tight', transpartent=True)
plt.show()


matrixInfo = np.array(normalizedcoOccurrenceMatrix)

# tupelData = []
#
dates = np.array([float(date[:4]) + (float(date[5:]) - 1) / 12 for date in crawlDate])
fig2, ax2 = plt.subplots()
# for series in a[0:]: # change this to not start from crawl 0
#     refDate = dates[series==1][0]
#     plotDates = np.abs(dates-refDate)
#     for date,overlap in zip(plotDates,series):
#         tupelData.append((date,overlap))

tupelData2 = []
j = 0
matrixInfo=matrixInfo[j:,j:]
dateCut=dates[j:]
for i, series in enumerate(matrixInfo):
    overlaps = matrixInfo[i,i:]
    refDate = dateCut[series==1][0]
    plotDates = np.abs(dateCut - refDate)[i:]
    for date, overlap in zip(plotDates,overlaps):
        tupelData2.append((date,overlap))

tupelData=tupelData2


xdate = [e[0] for e in tupelData]
yoverlap = [e[1] for e in tupelData]
from scipy.optimize import curve_fit

def funcPower(x, a, c, d):
    return a*np.power(x,c)+d

def funcPower2(x, a, xmin):
    return (a-0.999)/xmin*np.power(x/xmin,-a)

def funcExp(x, a, c, d):
    return a*np.exp(-c*x)+d



# popt, pcov = curve_fit(func, xdate, yoverlap, p0=(1, 2, 1))
poptpower, pcovpower = curve_fit(funcPower, xdate, yoverlap)
perrpower = np.sqrt(np.diag(pcovpower))

poptpower2, pcovpower2 = curve_fit(funcPower2, xdate, yoverlap)
perrpower2 = np.sqrt(np.diag(pcovpower2))

poptexp, pcovexp = curve_fit(funcExp, xdate, yoverlap)
perrexp = np.sqrt(np.diag(pcovexp))



xx = np.linspace(np.array(xdate).min(),np.array(xdate).max(),1000)
yyPower = funcPower(xx, *poptpower)
yyPower2 = funcPower2(xx, *poptpower2)
yyExp = funcExp(xx, *poptexp)


ax2.plot(xdate,yoverlap,'.',color='b')

yregionpower  = funcPower(xx, *poptpower)
y1power = funcPower(xx, *(poptpower+0.5*perrpower**0.5))
y2power = funcPower(xx, *(poptpower-0.5*perrpower**0.5))

yregionpower2  = funcPower2(xx, *poptpower2)
y1power2 = funcPower2(xx, *(poptpower2+0.5*perrpower2**0.5))
y2power2 = funcPower2(xx, *(poptpower2-0.5*perrpower2**0.5))

# power law clauset
data_pre = []
for deg,count in zip(xdate,yoverlap):
    data_pre.append([int(deg*120)] * int(count*100))
data = [el for line in data_pre for el in line]
# powerlaw.Fit()


ax2.plot(xx, yregionpower, 'k-')
ax2.plot(xx, y1power, 'g--')
ax2.plot(xx, y2power, 'g--')
ax2.fill_between(xx, y1power, y2power, facecolor="lightgray", alpha=0.15)


# yregionexp  = funcExp(xx, *poptexp)
# y1exp = funcExp(xx, *(poptexp+0.5*perrexp**0.5))
# y2exp = funcExp(xx, *(poptexp-0.5*perrexp**0.5))
#
# ax2.plot(xx, yregionexp, 'k')
# ax2.plot(xx, y1exp, 'g--')
# ax2.plot(xx, y2exp, 'g--')
# ax2.fill_between(xx, y1exp, y2exp, facecolor="gray", alpha=0.15)


ax2.set_xlabel(r'$\Delta$t in years')
ax2.set_ylabel(r'Relative overlap of SURTs')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
# ax2.legend(['Unique URLs','Unique SURTs','Retired Hosts'],loc='upper center', bbox_to_anchor=(0.5, 1.175),
#           ncol=3, fancybox=True, shadow=True)
ax2.set_ylim(bottom=0,top=1)
ax2.set_xlim(left=min(xx))
# ax2.legend([r'SURT overlap', r'Fit for $a(\Delta t)^c +d$', r'Fit for $ae^{-c \Delta t} +d$'],loc='upper center', bbox_to_anchor=(0.5, 1.18),
#           ncol=1, fancybox=True, shadow=True)
ax2.legend([r'SURT overlap', r'Fit for $a(\Delta t)^c +d$'],loc='upper center', bbox_to_anchor=(0.5, 1.18),
          ncol=2, fancybox=True, shadow=True)
inDegreeimgPath = 'intersectionSurtsFit'
fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')

plt.show()