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


#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'
os.chdir(homepath)

datasets = ["ATSRH/","NRH/"]

fig2, ax2 = plt.subplots()
crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06','2018-12']
colorMap = 'RdYlBu'
n=12
# color_sequence = [cm.get_cmap('Greys')(i) for i in (np.linspace(20,200,n)/255)]
# color_sequence = [cm.get_cmap('YlGnBu')(i) for i in (np.linspace(20,200,n+1)/255)]
color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
for icolor, dataset in enumerate(datasets):
    os.chdir(homepath+'resultData/MetaData/countDist/CD_dist/'+dataset )
    dates = os.listdir(".")
    CDinCrawlDict = {}
    for date in dates:
        with open(date) as f:
            lines = f.readlines()
            CD = np.array([int(line.rstrip()[1:-1].split(',')[0]) for line in lines][1::])-1
            counts = [int(line.rstrip()[1:-1].split(',')[1]) for line in lines][0:-1]
            countNormalized = [count/max(counts) for count in counts]

        CDinCrawlDict[date] = (CD,counts)


    ########### center of mass of distribution
    CD_cut = 20
    # fig2, ax2 = plt.subplots()
    dateNum=[]
    CDmax=[]
    CoM = []
    stdCoM = []
    for date, series in CDinCrawlDict.items():
        dateNum.append(float(date[:4]) + (float(date[5:]) - 1) / 12 )
        # SDmax.append(max(np.array(series).T,key=lambda x:x[1])[0]) investigating the maximum

        # CoM.append(sum(series[1][0:CD_cut])/CD_cut)
        CoM.append(sum([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:CD_cut]])/sum(series[1][0:CD_cut]))
        stdCoM.append(np.std([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:CD_cut]])/sum(series[1][0:CD_cut]))
        # CoM.append(sum(series[1][0:CD_cut])/CD_cut)


    # ax2.plot(dateNum,SDmax,'.')
    # ax2.set_ylabel(r'SD$_{max}$')
    # ax2.plot(dateNum,CoM,'.')
    plotData = sorted(list(zip(dateNum,CoM,stdCoM)),key=lambda x:x[0])
    dateNum = [e[0] for e in plotData]
    CoM = [e[1] for e in plotData]
    stdCoM = [e[2] for e in plotData]
    ax2.errorbar(dateNum,CoM,np.array(stdCoM)/2,color="C"+str(icolor) ,ecolor='lightgray', elinewidth=2, capsize=4)

ax2.set_ylabel(r'$\mathbb{E}$[CD]')

ax2.set_xlabel(r'Crawl date')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.legend(["ATSRH","ATSRH $\cap$ NRH"],loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=2, fancybox=True, shadow=True)
# ax2.legend()
# ax2.set_ylim(bottom=0)
ax2.set_xlim(left=min(dateNum)-0.05,right=max(dateNum)+0.05)
os.chdir(homepath+"resultDataVisualization/images/MetaData/countDist/preproc/CD_vs_t")
inDegreeimgPath = 'CDcom'
fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
plt.show()

#
# crawlDate = ['2012-10','2013-02','2013-12','2014-05','2014-12','2015-05','2015-12','2016-06','2016-12','2017-06','2017-12','2018-06','2018-12']
# colorMap = 'RdYlBu'
# n=12
# # color_sequence = [cm.get_cmap('Greys')(i) for i in (np.linspace(20,200,n)/255)]
# # color_sequence = [cm.get_cmap('YlGnBu')(i) for i in (np.linspace(20,200,n+1)/255)]
# color_sequence = [cm.get_cmap(colorMap)(i) for i in (np.linspace(20,200,n+1)/255)]
#
# os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/CD_dist/preproc')
# dates = os.listdir(".")
# CDinCrawlDict = {}
# for date in dates:
#     with open(date) as f:
#         lines = f.readlines()
#         CD = np.array([int(line.rstrip()[1:-1].split(',')[0]) for line in lines][1::])-1
#         counts = [int(line.rstrip()[1:-1].split(',')[1]) for line in lines][0:-1]
#         countNormalized = [count/max(counts) for count in counts]
#
#     CDinCrawlDict[date] = (CD,counts)
#
# fig, ax = plt.subplots()
# datesNum = []
# legendProxies=[]
# keys=[]
# CDarray = sorted([(date, series) for date, series in CDinCrawlDict.items()],key=lambda x:x[0])
# for i,(date, series) in enumerate(CDarray):
#     ax.plot(series[0],series[1],color=color_sequence[i])
#     legendProxies.append(plt.Rectangle((0, 0), 1, 1, fc=color_sequence[i]))
#     keys.append(date)
#
# ax.set_xlabel(r'CD')
# ax.set_ylabel(r'Captures')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.legend(legendProxies,keys,loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=3, fancybox=True, shadow=True)
# # ax.legend()
# ax.set_ylim(bottom=0)
# ax.set_xlim(left=0,right=20)
#
# plt.show()
#
#
# ########### center of mass of distribution
# CD_cut = 20
# fig2, ax2 = plt.subplots()
# dateNum=[]
# CDmax=[]
# CoM = []
# stdCoM = []
# for date, series in CDinCrawlDict.items():
#     dateNum.append(float(date[:4]) + (float(date[5:]) - 1) / 12 )
#     # SDmax.append(max(np.array(series).T,key=lambda x:x[1])[0]) investigating the maximum
#
#     # CoM.append(sum(series[1][0:CD_cut])/CD_cut)
#     CoM.append(sum([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:CD_cut]])/sum(series[1][0:CD_cut]))
#     stdCoM.append(np.std([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:CD_cut]])/sum(series[1][0:CD_cut]))
#     # CoM.append(sum(series[1][0:CD_cut])/CD_cut)
#
#
# # ax2.plot(dateNum,SDmax,'.')
# # ax2.set_ylabel(r'SD$_{max}$')
# # ax2.plot(dateNum,CoM,'.')
# plotData = sorted(list(zip(dateNum,CoM,stdCoM)),key=lambda x:x[0])
# dateNum = [e[0] for e in plotData]
# CoM = [e[1] for e in plotData]
# stdCoM = [e[2] for e in plotData]
# ax2.errorbar(dateNum,CoM,np.array(stdCoM)/2,label='Center of mass of the CD distribution', color='C0',
#              ecolor='lightgray', elinewidth=2, capsize=4)
# ax2.set_ylabel(r'CD$_{com}$')
#
# ax2.set_xlabel(r'Crawl date')
# ax2.spines['right'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=3, fancybox=True, shadow=True)
# # ax2.legend()
# # ax2.set_ylim(bottom=0)
# ax2.set_xlim(left=min(dateNum)-0.05,right=max(dateNum)+0.05)
# os.chdir("/home/parism/REGIO/resultDataVisualization/images/MetaData/countDist/preproc/CD_vs_t")
# inDegreeimgPath = 'CDcom'
# fig2.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
# plt.show()



####### maximum position
# CD_cut = 20
# fig3, ax3 = plt.subplots()
# dateNum=[]
# CDmax=[]
# argMax = []
# stdCoM = []
# for date, series in CDinCrawlDict.items():
#     dateNum.append(float(date[:4]) + (float(date[5:]) - 1) / 12 )
#     # SDmax.append(max(np.array(series).T,key=lambda x:x[1])[0]) investigating the maximum
#
#     # CoM.append(sum(series[1][0:CD_cut])/CD_cut)
#     argMax.append(max(list(zip(series[0],series[1])),key=lambda x:x[1]))
#     stdCoM.append(np.std([e[0]*e[1] for e in list(zip(series[0],series[1]))[0:CD_cut]])/sum(series[1][0:CD_cut]))
#     # CoM.append(sum(series[1][0:CD_cut])/CD_cut)
#
#
# # ax3.plot(dateNum,SDmax,'.')
# # ax3.set_ylabel(r'SD$_{max}$')
# # ax3.plot(dateNum,CoM,'.')
# plotData = sorted(list(zip(dateNum,CoM,stdCoM)),key=lambda x:x[0])
# dateNum = [e[0] for e in plotData]
# CoM = [e[1] for e in plotData]
# stdCoM = [e[2] for e in plotData]
# ax3.errorbar(dateNum,CoM,stdCoM,label='CD of maximum records')
# ax3.set_ylabel(r'CD$_{max}$')
#
# ax3.set_xlabel(r'Crawl date')
# ax3.spines['right'].set_visible(False)
# ax3.spines['top'].set_visible(False)
# ax3.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=3, fancybox=True, shadow=True)
# ax3.legend()
# # ax3.set_ylim(bottom=0)
# ax3.set_xlim(left=min(dateNum)-0.05,right=max(dateNum)+0.05)
# os.chdir("/home/parism/REGIO/resultDataVisualization/images/MetaData/countDist/preproc/CD_vs_t")
# inDegreeimgPath = 'CDcom'
# fig3.savefig(inDegreeimgPath+ '.eps', dpi=300, transpartent=True,bbox_inches='tight')
# plt.show()

