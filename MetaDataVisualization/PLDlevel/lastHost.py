# ( top-domain,sec domain, List( (subdomain, tsMin, tsMax, count) ) )
# (es,xn--nm-5ja,List((creationsite,20121028194204,20121028194231)))
# (de,falk-schulz,List((,20121022043947,20121022043954)))
# (com,accenture,List((careers,20121021174320,20121021174344), (careers3,20121016064710,20121016064734), (omni,20121028004027,20121028004153), (,20121022075359,20121022080348)))
# (info,jacobsohn,List((,20121012062303,20121012062403)))
# (de,immobilo,List((opendix,20121022211536,20121022211651), (ss,s9,20121017073737,20121017073827), (ss,s1,20121017073737,20121017075545), (ss,rl,20121017073737,20121017073752), (ss,s4,20121017073737,20121017073829), (ss,20121017073737,20121023200933), (images,20121017073737,20121017073801), (ox,20121017073737,20121017073805), (,20121012195210,20121022215024), (ss,s5,20121017073737,20121017073939)))
# (com,xwebtechnology,List((mediawiki,20121028150718,20121028150735)))
# (de,elbserver,List((piwik,20121022015736,20121022023009)))
# (com,wkhealth,List((pt,20121015175620,20121015175644)))
# (com,ucas,List((,20121027220529,20121027220602)))
# (org,pragmatism,List((,20121018060730,20121018060948)))
# (ca,dmsolutions,List((,20121013073329,20121013073349)))
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


########## load seeds and extract all of those always present ##############

#homepath
homepath = '/home/parism/PhD/REGIO/GAW_visualization_python/ProjectComparabilityAndExploration/'

os.chdir(homepath +"resultData/MetaData/seeds")
ls = os.listdir(".")

seeds = [e for e in ls if e.__contains__(".seeds")]

intersectionOfSeeds = set
for seed in seeds:
    with open(seed) as fs:
        lines = fs.readlines()
        cleanLines = set([line.rstrip() for line in lines])
        if not intersectionOfSeeds:
            intersectionOfSeeds = cleanLines
        else:
            intersectionOfSeeds = intersectionOfSeeds.intersection(cleanLines)

intersectionOfSeedsAsSurt = {",".join(e.split(".")[::-1]) for e in intersectionOfSeeds}


############### load the information about the hosts ###############
# lastHostDict = {date: {PLD: { subdomains:[tsMin,tsMax,countInstances] } } }

import os
os.chdir(homepath +"resultData/MetaData/PLDlevel/lastHost/gaw")
dates = os.listdir(".")

lastHostDict = {}
for date in dates:
    with open(date) as fs:
        lines = fs.readlines()
        trimmedLines = [line.rstrip() for line in lines]
        hostStringLists = [line.split(",List(")[0][1::] for line in trimmedLines]
        valuesStringLists = [line.split(",List(")[1][:-2] for line in trimmedLines]
        valuesLineElementLists = [line.split(", ") for line in valuesStringLists]
        d = {}
        for hostString, line in zip(hostStringLists,valuesLineElementLists):
            for e in line:
                trimmedElements = e[1:-1]
                subdomainString = ",".join(trimmedElements.split(',')[0:-3])
                tsMinString = trimmedElements.split(',')[-3]
                tsMaxString = trimmedElements.split(',')[-2]
                hostInstancesCount = int(trimmedElements.split(',')[-1])
                # lastHostDict[hostString] = {subdomainString: [tsMinString, tsMaxString, hostInstancesCount]}
                if hostString in d.keys():
                    d[hostString].update({subdomainString: [tsMinString, tsMaxString, hostInstancesCount]})
                else:
                    d[hostString]={subdomainString: [tsMinString, tsMaxString, hostInstancesCount]}
    lastHostDict.update({date:d})

############### filter the information by the seeds #################

lastHostDict_filteredToSeeds={}
for date, perHostDict in lastHostDict.items():
    perDateDict = {host: subDomainsDict for host, subDomainsDict in perHostDict.items() if host in intersectionOfSeedsAsSurt}
    lastHostDict_filteredToSeeds[date] = perDateDict


############### some helper functions ##################
#### seeds hosts specific

def getNumOfSubdomainsFromSeed(lastHostDict_filteredToSeeds,seedSurt,date):
    return lastHostDict_filteredToSeeds[date][seedSurt].keys().__len__()

def getLastCrawledHostStarted(lastHostDict_filteredToSeeds,date):
    l=[]
    hostsDict = lastHostDict_filteredToSeeds[date]
    for host, subdomainDict in hostsDict.items():
        for subdomain, tsList in subdomainDict.items():
            l.append((tsList[0], host, subdomain))
    tsMinOfLastHost = sorted(l,key=lambda x:x[0])[-1] #get last element in the list of sorted timeStamps tsMin,
    return (tsMinOfLastHost[1:3],lastHostDict_filteredToSeeds[date][tsMinOfLastHost[1]][tsMinOfLastHost[2]])

#### all hosts related
def getLastCrawledItem(lastHostDict,date):
    l = []
    hostsDict=lastHostDict[date]
    for host, subdomainDict in hostsDict.items():
        for subdomain, tsList in subdomainDict.items():
            l.append((tsList[1], host, subdomain))
    lastItemCrawled = sorted(l, key=lambda x: x[0])[-1] #get last
    return (lastItemCrawled[1:3],lastHostDict[date][lastItemCrawled[1]][lastItemCrawled[2]])


def getFirstCrawledItem(lastHostDict,date):
    l = []
    hostsDict=lastHostDict[date]
    for host, subdomainDict in hostsDict.items():
        for subdomain, tsList in subdomainDict.items():
            l.append((tsList[0], host, subdomain))
    firstItemCrawled = sorted(l, key=lambda x: x[0])[0] #get first
    return (firstItemCrawled[1:3],lastHostDict[date][firstItemCrawled[1]][firstItemCrawled[2]])


def getSortedtsMinInSubdomain(lastHostDict_filteredToSeeds,date):
    l=[]
    hostsDict = lastHostDict_filteredToSeeds[date]
    for host, subdomainDict in hostsDict.items():
        for subdomain, tsList in subdomainDict.items():
            l.append(tsList[0])
    tsMinFindingSeries = sorted(l)
    return (tsMinFindingSeries)

                        ##########  rja's idea  ##############
# dates =  ("2012-10","2013-02","2013-12","2014-05","2014-12","2015-05","2015-12","2016-06","2016-12","2017-06","2017-12","2018-06","2018-12")
dates =  ("2013-12","2014-05","2014-12","2015-05","2015-12","2016-06","2016-12","2017-06","2017-12","2018-06","2018-12")

n=dates.__len__()
colorMap = 'RdYlBu'
color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
legendProxies = []
legendKeys = []
fig, ax = plt.subplots()

for i,date in enumerate(dates):
    tsMinInSubdomain = getSortedtsMinInSubdomain(lastHostDict_filteredToSeeds,date)
    tup = list(Counter(tsMinInSubdomain).items()) # how many subdomain with this tsMin
    sortedTup = sorted(tup,key=lambda x:x[0])

    timeStamps = []
    accumCount = []

    c=0
    for ts, count in sortedTup:
        timeStamps.append(ts)
        if not accumCount:
            accumCount.append(count)
            c=count
        else:
            c+=count
            accumCount.append(c)

    accumulatedHostCountnormalized = np.array(accumCount)/np.array(accumCount).max()

    secEpoch = [datetime.datetime.strptime(ts,'%Y%m%d%H%M%S').timestamp() for ts in timeStamps]
    durationInSec = np.array(secEpoch)-np.array(secEpoch).min()
    plt.plot(durationInSec,accumulatedHostCountnormalized,'.',color=color_sequence[i])
    legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))
    legendKeys.append(date)


plt.xlabel('Time in s')
plt.ylabel('Fraction of hosts found')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.legend(legendProxies, legendKeys)
plt.show()


# hostFraction = 0.95
def distributionWithFraction(hostFraction):
    # dates =  ("2012-10","2013-02","2013-12","2014-05","2014-12","2015-05","2015-12","2016-06","2016-12","2017-06",
    #           "2017-12","2018-06","2018-12")
    dates =  ("2013-12","2014-05","2014-12","2015-05","2015-12","2016-06","2016-12","2017-06",
              "2017-12","2018-06","2018-12")
    # hostFraction = 0.95
    n=dates.__len__()
    colorMap = 'RdYlBu'
    color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
    legendProxies = []
    legendKeys = []

    t_threshold_List = []
    datesInNumeral = []
    for i,date in enumerate(dates):
        tsMinInSubdomain = getSortedtsMinInSubdomain(lastHostDict_filteredToSeeds,date)
        tup = list(Counter(tsMinInSubdomain).items()) # how many subdomain with this tsMin
        sortedTup = sorted(tup,key=lambda x:x[0])

        timeStamps = []
        accumCount = []

        c=0
        for ts, count in sortedTup:
            timeStamps.append(ts)
            if not accumCount:
                accumCount.append(count)
                c=count
            else:
                c+=count
                accumCount.append(c)

        accumulatedHostCountnormalized = np.array(accumCount)/np.array(accumCount).max()

        firstItem = getFirstCrawledItem(lastHostDict,date)
        lastItem = getLastCrawledItem(lastHostDict,date)

        t_start = datetime.datetime.strptime(firstItem[1][0],'%Y%m%d%H%M%S').timestamp()
        t_end = datetime.datetime.strptime(lastItem[1][1],'%Y%m%d%H%M%S').timestamp()

        secEpoch = [datetime.datetime.strptime(ts,'%Y%m%d%H%M%S').timestamp() for ts in timeStamps]
        durationInSec = np.array(secEpoch)-np.array(secEpoch).min()
        fulldurationInSec = t_end-t_start
        import bisect

        ind = bisect.bisect_left(accumulatedHostCountnormalized, hostFraction)
        # tcrit = durationInSec[ind] / durationInSec.max()
        tcrit = durationInSec[ind] / fulldurationInSec
        t = float(date[:4]) + (float(date[5:]) - 1) / 12
        t_threshold_List.append(tcrit)
        datesInNumeral.append(t)
        legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))
        legendKeys.append(date)

    return datesInNumeral,t_threshold_List

fig2, ax2 = plt.subplots()

datesInNumeral99,t_threshold_List99 = distributionWithFraction(0.99)
ax2.plot(datesInNumeral99,t_threshold_List99,color='g',label=r'99$\%$ of SRH found')
fractions=(np.array(list(range(1,6))))/5
for fraction in fractions:
    datesInNumeral1,t_threshold_List1 = distributionWithFraction(fraction)
    # ax2.plot(datesInNumeral1,t_threshold_List1,'--',label=r'$'+str(int(fraction*100))+'\%$ of SRH')
    ax2.plot(datesInNumeral1,t_threshold_List1,'--',color='k')


ax2.set_xlabel(r'Crawl date')
ax2.set_ylabel(r'Normalized $t_{D}$')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.set_ylim(bottom=0)
ax2.set_xlim(left=datesInNumeral1[0],right=datesInNumeral1[-1])
# ax2.legend()
#
ax2.legend([r'99$\%$ of SRH found',r'Equipartition of host in ATSRH'],fontsize=12,columnspacing=1, loc='upper center', bbox_to_anchor=(0.5, 1.12),
          ncol=2, fancybox=True, shadow=True)
os.chdir(homepath +"resultDataVisualization/images/MetaData/PLDlevel/lastHost")
inDegreeimgPath = 'lastHostfound'
fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()

#
#
# t1 =[]
# for date in dates:
#     t1.append(getLastCrawledItem(lastHostDict,date)[1][1])
# t0 = []
# for date in dates:
#     t0.append(getFirstCrawledItem(lastHostDict,date)[1][0])
#
#
# lastCrawledTime = [datetime.datetime.strptime(ts, '%Y%m%d%H%M%S').timestamp() for ts in t1]
# firstCrawledTime = [datetime.datetime.strptime(ts, '%Y%m%d%H%M%S').timestamp() for ts in t0]
# durationList = [(e[1]-e[0]) for e in zip(firstCrawledTime,lastCrawledTime)]
#
# fig4,ax4 = plt.subplots()
# width = 0.25
# datesInNumeral1,t_threshold_List1 = distributionWithFraction(0.99)
# lastHostInSec95 = [duration*tcrit for duration,tcrit in zip(durationList,t_threshold_List1)]


##### No. of host vs crawl date

with open(homepath + "resultData/MetaData/retiredHost.txt") as rh:
    retiredHostsLines = rh.readlines()
    retiredHosts = [line.rstrip() for line in retiredHostsLines]


fig3, ax3 = plt.subplots()

subdomainsCount=0
retiredHostInDicts = 0
d = []
t=[]
for date, pldDict in lastHostDict_filteredToSeeds.items():
    t.append(float(date[:4]) + (float(date[5:]) - 1) / 12)
    # subdomainsCount=[]
    subdomainsCount=0
    for pld, subDomainsDict in pldDict.items():
        for subdomain in subDomainsDict.keys():
            fullHost = pld + ',' + subdomain
            if fullHost in retiredHosts: #disable for no retiredhost removal
                retiredHostInDicts+=1
            else:
                subdomainsCount+=1
    d.append(subdomainsCount)

plotHostData = [e for e in zip(t,d)]
crawldate = [e[0] for e in sorted(plotHostData,key=lambda x:x[0])]
subdomains = [e[1] for e in sorted(plotHostData,key=lambda x:x[0])]


subdomainsCount=0
retiredHostInDicts = 0
d = []
t=[]
for date, pldDict in lastHostDict_filteredToSeeds.items():
    t.append(float(date[:4]) + (float(date[5:]) - 1) / 12)
    # subdomainsCount=[]
    subdomainsCount=0
    for pld, subDomainsDict in pldDict.items():
        for subdomain in subDomainsDict.keys():
            fullHost = pld + ',' + subdomain
            if False: #disable for no retiredhost removal
                retiredHostInDicts+=1
            else:
                subdomainsCount+=1
    d.append(subdomainsCount)

td = np.array(sorted(zip(t,d),key=lambda x:x[0]))
# plt.tight_layout()

ax3.plot(td[:,0][2:],td[:,1][2:],label=r'ATSRH')
ax3.plot(crawldate[2:],np.array(subdomains)[2:],label=r'ATSRH $\cap$ NRH')
ax3.set_xlabel(r'Crawl date')
ax3.set_ylabel(r'Subdomains ')
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
# ax3.set_ylim(bottom=0)
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.19),
          ncol=2, fancybox=True, shadow=True)
ax3.set_xlim(left=min(td[:,0][2:]),right=max(t))
ax3.yaxis.set_major_formatter(FuncFormatter(number_formatter))
os.chdir(homepath + "resultDataVisualization/images/MetaData/PLDlevel/lastHost")
inDegreeimgPath3 = 'subdomaincount'
fig3.savefig(inDegreeimgPath3 + '.eps', dpi=300, transpartent=True,bbox_inches='tight')
# fig3.savefig(inDegreeimgPath3 + '.eps', dpi=300, transpartent=True)
plt.show()

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(crawldate,np.array(subdomains))

#### crawlduration
crawlDuraction=[]
for date in dates:
    firstItem = getFirstCrawledItem(lastHostDict, date)
    lastItem = getLastCrawledItem(lastHostDict, date)

    t_start = datetime.datetime.strptime(firstItem[1][0], '%Y%m%d%H%M%S').timestamp()
    t_end = datetime.datetime.strptime(lastItem[1][1], '%Y%m%d%H%M%S').timestamp()

    fulldurationInSec = t_end - t_start
    t = float(date[:4]) + (float(date[5:]) - 1) / 12
    crawlDuraction.append((t,fulldurationInSec))

durationPlot = np.array(sorted(crawlDuraction,key=lambda x:x[0]))

fig4, ax4 = plt.subplots()
ax4.plot(durationPlot[:,0],durationPlot[:,1]/(60*60*24),label=r'Duration')
ax4.set_xlabel(r'Crawl date')
ax4.set_ylabel(r'Duration in days')
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),
          ncol=1, fancybox=True, shadow=True)
ax4.set_ylim(bottom=0)
ax4.set_xlim(left=min(durationPlot[:,0]),right=max(durationPlot[:,0]))
os.chdir(homepath +"resultDataVisualization/images/MetaData/PLDlevel/lastHost")
inDegreeimgPath3 = 'duration'
fig4.savefig(inDegreeimgPath3 + '.eps', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()
