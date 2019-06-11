# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# from matplotlib import cm
# import os
# from matplotlib.text import Text
# import matplotlib as mpl
#
#
#
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preview=True)
# plt.rc('font', size=15)
# plt.rc('legend', fontsize=14)
# plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
#
# datasets = []
#
# crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06','2018-12']
# colorMap = 'RdYlBu'
# n=12
# SD_cut = 12
# # color_sequence = [cm.get_cmap('Greys')(i) for i in (np.linspace(20,200,n)/255)]
# # color_sequence = [cm.get_cmap('YlGnBu')(i) for i in (np.linspace(20,200,n+1)/255)]
# color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
#
# os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/SD_dist/gaw/')
# dates = os.listdir(".")
# SDinCrawlDict = {}
# for date in dates:
#     with open(date) as f:
#         lines = f.readlines()
#         SD = np.array([int(line.rstrip()[1:-1].split(',')[0]) for line in lines][1::])-1
#         counts = [int(line.rstrip()[1:-1].split(',')[1]) for line in lines][0:-1]
#         countNormalized = [count/max(counts) for count in counts]
#
#     SDinCrawlDict[date] = (SD,counts)
#
# fig, ax = plt.subplots()
# datesNum = []
# legendProxies=[]
# keys=[]
# SDarray = sorted([(date, series) for date, series in SDinCrawlDict.items()],key=lambda x:x[0])
# for i,(date, series) in enumerate(SDarray[2::]):
#     ax.plot(series[0]-1,series[1],color=color_sequence[i])
#     legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))
#     keys.append(date)
#
# ax.set_xlabel(r'SD')
# ax.set_ylabel(r'Captures')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.legend(legendProxies,keys,loc='upper center', bbox_to_anchor=(0.5, 1.25),   ncol=4, fancybox=True, shadow=True)
# # ax.legend(legendProxies,keys)
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0,right=SD_cut)
#
# # plt.show()
#
#
# fig2, ax2 = plt.subplots()
# dateNum=[]
# SDmax=[]
# CoM = []
# stdCoM = []
# for date, series in SDinCrawlDict.items():
#     dateNum.append(float(date[:4]) + (float(date[5:]) - 1) / 12 )
#     # SDmax.append(max(np.array(series).T,key=lambda x:x[1])[0]) investigating the maximum
#
#     # CoM.append(sum(series[1][0:SD_cut])/SD_cut)
#     CoM.append(sum([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:SD_cut]])/sum(series[1][0:SD_cut])-1)
#     stdCoM.append(np.std([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:SD_cut]])/sum(series[1][0:SD_cut]))
#     # CoM.append(sum(series[1][0:SD_cut])/SD_cut)
#
#
# # ax2.plot(dateNum,SDmax,'.')
# # ax2.set_ylabel(r'SD$_{max}$')
# # ax2.plot(dateNum,CoM,'.')
# plotData = sorted(list(zip(dateNum,CoM,stdCoM)),key=lambda x:x[0])[2:]
# dateNum = [e[0] for e in plotData]
# CoM = [e[1] for e in plotData]
# stdCoM = [e[2] for e in plotData]
# ax2.errorbar(dateNum,CoM,np.array(stdCoM)/2,label="Center of mass of the SD distribution", color='C0',
#              ecolor='lightgray', elinewidth=2, capsize=4)
# ax2.set_ylabel(r'SD$_{com}$')
#
# ax2.set_xlabel(r'Crawl date')
# ax2.spines['right'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=3, fancybox=True, shadow=True)
# # ax2.legend()
# ax2.set_ylim(bottom=3,top=4.7)
# ax2.set_xlim(left=min(dateNum)-0.05,right=max(dateNum)+0.05)
# os.chdir("/home/parism/REGIO/resultDataVisualization/images/MetaData/countDist/preproc/SD_vs_t")
# inDegreeimgPath = 'SDcom'
# fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
# plt.show()
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import cm
import os
from matplotlib.text import Text
import matplotlib as mpl



plt.rc('text', usetex=True)
plt.rc('text.latex', preview=True)
plt.rc('font', size=15)
plt.rc('legend', fontsize=14)
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
params= {'text.latex.preamble' : [r'\usepackage{amsfonts}']}
plt.rcParams.update(params)

datasets = ["ATSRH/","NRH/"]
# datasets = ["gaw/"]

crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06','2018-12']
colorMap = 'RdYlBu'
n=12
SD_cut = 12
# color_sequence = [cm.get_cmap('Greys')(i) for i in (np.linspace(20,200,n)/255)]
# color_sequence = [cm.get_cmap('YlGnBu')(i) for i in (np.linspace(20,200,n+1)/255)]
color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]



#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'


fig2, ax2 = plt.subplots()
for icolor,dataset in enumerate(datasets):
    os.chdir(homepath+'resultData/MetaData/countDist/SD_dist/' + dataset)
    dates = os.listdir(".")
    SDinCrawlDict = {}
    for date in dates:
        with open(date) as f:
            lines = f.readlines()
            SD = np.array([int(line.rstrip()[1:-1].split(',')[0]) for line in lines][1::])-1
            counts = [int(line.rstrip()[1:-1].split(',')[1]) for line in lines][0:-1]
            countNormalized = [count/max(counts) for count in counts]

        SDinCrawlDict[date] = (SD,counts)

    datesNum = []
    legendProxies=[]
    keys=[]
    SDarray = sorted([(date, series) for date, series in SDinCrawlDict.items()],key=lambda x:x[0])
    for i,(date, series) in enumerate(SDarray[2::]):
        legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))
        keys.append(date)


    dateNum=[]
    SDmax=[]
    CoM = []
    stdCoM = []
    for date, series in SDinCrawlDict.items():
        dateNum.append(float(date[:4]) + (float(date[5:]) - 1) / 12 )
        # SDmax.append(max(np.array(series).T,key=lambda x:x[1])[0]) investigating the maximum

        # CoM.append(sum(series[1][0:SD_cut])/SD_cut)
        CoM.append(sum([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:SD_cut]])/sum(series[1][0:SD_cut])-1)
        stdCoM.append(np.std([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:SD_cut]])/sum(series[1][0:SD_cut]))
        # CoM.append(sum(series[1][0:SD_cut])/SD_cut)


    # ax2.plot(dateNum,SDmax,'.')
    # ax2.set_ylabel(r'SD$_{max}$')
    # ax2.plot(dateNum,CoM,'.')
    plotData = sorted(list(zip(dateNum,CoM,stdCoM)),key=lambda x:x[0])[2:]
    dateNum = [e[0] for e in plotData]
    CoM = [e[1] for e in plotData]
    stdCoM = [e[2] for e in plotData]
    ax2.errorbar(dateNum,CoM,np.array(stdCoM)/2, color="C"+str(icolor),  ecolor='lightgray', elinewidth=2, capsize=4)
    # ax2.set_ylabel(r'SD$_{com}$')
    ax2.set_ylabel(r'$\mathbb{E}$[SD]')

    ax2.set_xlabel(r'Crawl date')
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    # ax2.legend()
    ax2.set_ylim(bottom=3,top=4.7)
    ax2.set_xlim(left=min(dateNum)-0.05,right=max(dateNum)+0.05)


ax2.legend(["ATSRH","ATSRH $\cap$ NRH"],loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=2, fancybox=True, shadow=True)
os.chdir(homepath+"resultDataVisualization/images/MetaData/countDist/preproc/SD_vs_t")
inDegreeimgPath = 'SDcom'
fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()

