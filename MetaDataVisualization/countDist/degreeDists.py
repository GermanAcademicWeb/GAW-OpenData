# (inDegree, count)
# (3,15678358)
# (4,11029004)
# (11861,1)
# (5,4190025)
# (6,5611325)
import powerlaw
import os
import multiprocessing
from collections import Counter
# import matplotlib.pyplot as plt
import numpy as np


inDegreeDistPath = "InDeg/"
outDegreeDistPath = "OutDeg/"

cuts = ["gaw/", "ATSRH/", "NRH/"]
dataset = cuts[2]


os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
currentPath = inDegreeDistPath
dates = sorted(os.listdir(currentPath))
date = dates[5]
with open(currentPath + date) as dd:
    data_unstriped = dd.readlines()
    data_stripped = [d.rstrip() for d in data_unstriped]
    tupelStr = [line[1:-1].split(',') for line in data_stripped]
    tupelArray = np.array([(int(line[0]), int(line[1])) for line in tupelStr])

data_pre = []
for deg, count in tupelArray:
    data_pre.append([deg] * count)
data = [el for line in data_pre for el in line]

alphaList = []
xminList = []
sigmaList = []

data_sampled = data  ## change this to 'data' if no resampling is desired
np.random.shuffle(data_sampled)
results = powerlaw.Fit(data_sampled)
alphaList.append(results.alpha)
sigmaList.append(results.sigma)
xminList.append(results.xmin)

savepathPowerLaw = 'powerlawResultsFULL/' + dataset + inDegreeDistPath
if not os.path.isdir(savepathPowerLaw):
    os.makedirs(savepathPowerLaw)

with open(savepathPowerLaw + date, "w+") as pr:
    savedata = [results.alpha, results.sigma, results.xmin]
    output = " ".join([str(e) for e in savedata])
    pr.writelines(output)



def writeAlpha(date):
    with open(currentPath + date) as dd:
        data_unstriped = dd.readlines()
        data_stripped = [d.rstrip() for d in data_unstriped]
        tupelStr = [line[1:-1].split(',') for line in data_stripped]
        tupelArray = np.array(
            [(int(line[0]), int(line[1])) for line in tupelStr])  # deg = tupelArray[:,0], count  = tupelArray[:,1]

    normalization = tupelArray[:, 1].sum()
    yfraction = tupelArray[:, 1] / normalization
    xdegree = tupelArray[:, 0]

    data_pre = []
    for deg, count in tupelArray:
        data_pre.append([deg] * count)
    data = [el for line in data_pre for el in line]
    # for deg, count in tupelArray:
    #     dl=[deg]*count
    #     for e in dl:
    #         data.append(e)

    alphaList = []
    xminList = []

    # # sampled with and averaged
    # for i in range(50):
    #     data_sampled = np.random.choice(data,int(data.__len__() / 100))  ## change this to 'data' if no resampling is desired
    #     results = powerlaw.Fit(data_sampled)
    #     alphaList.append(results.alpha)
    #     xminList.append(results.xmin)


    data_sampled = np.random.shuffle(data)  ## change this to 'data' if no resampling is desired
    results = powerlaw.Fit(data_sampled)
    alphaList.append(results.alpha)
    xminList.append(results.xmin)

    # for pooling TODO
    # def chunks(l, n):
    #     n = max(1, n)
    #     return (l[i:i + n] for i in range(0, len(l), n))
    #
    # chunkedData = chunks(data,100)
    #
    # def getresultsWorker(chunkedData):



    alphamean = np.array(alphaList).mean()
    alphaSigma = np.array(alphaList).std()
    xminmean = np.array(xminList).mean()

    # reducedDir = Counter(data)
    # tups = [(k,v) for k,v in reducedDir.items()]
    # x = [k for k,v in tups]
    # y = [v for k,v in tups]
    # ymax = max(y) # I know that this is not the correct normalization, the slope is not affected

    savepathPowerLaw = 'powerlawResultsmean/' + dataset + inDegreeDistPath
    if not os.path.isdir('powerlawResultsmean'):
        os.makedirs(savepathPowerLaw)

    with open(savepathPowerLaw + date, "w+") as pr:
        savedata = [alphamean, alphaSigma, xminmean]
        output = " ".join([str(e) for e in savedata])
        pr.writelines(output)

pool = multiprocessing.Pool(10)
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preview=True)
# plt.rc('font', size=15)
# plt.rc('legend', fontsize=14)
# plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# local
# dataset = "gaw/"
#os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/'+dataset+'degreeDist/')
# local
# os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/degreeDist/'+dataset)
# regio
# os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/'+dataset)
# L3S
#os.chdir('/home/paris/resultData/MetaData/countDist/'+dataset+'degreeDist/')
inDegreeDistPath = "InDeg/"
outDegreeDistPath = "OutDeg/"

cuts = ["gaw/", "ATSRH/", "NRH/"]
for dataset in cuts:
    os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
    currentPath = inDegreeDistPath
    dates = sorted(os.listdir(currentPath))
    for date in dates:
        pool.map(writeAlpha,date)
        # with open(currentPath+date) as dd:
        #     data_unstriped = dd.readlines()
        #     data_stripped = [d.rstrip() for d in data_unstriped]
        #     tupelStr = [line[1:-1].split(',') for line in data_stripped]
        #     tupelArray = np.array([(int(line[0]),int(line[1])) for line in tupelStr]) #deg = tupelArray[:,0], count  = tupelArray[:,1]
        #
        # normalization = tupelArray[:,1].sum()
        # yfraction = tupelArray[:,1]/normalization
        # xdegree = tupelArray[:,0]
        #
        # data_pre = []
        # for deg, count in tupelArray:
        #     data_pre.append([deg]*count)
        # data = [el for line in data_pre for el in line]
        # # for deg, count in tupelArray:
        # #     dl=[deg]*count
        # #     for e in dl:
        # #         data.append(e)
        #
        # alphaList = []
        # xminList = []
        #
        # for i in range(50):
        #     data_sampled = np.random.choice(data,int(data.__len__()/100)) ## change this to 'data' if no resampling is desired
        #     results = powerlaw.Fit(data_sampled)
        #     alphaList.append(results.alpha)
        #     xminList.append(results.xmin)
        #
        #
        # alphamean = np.array(alphaList).mean()
        # alphaSigma = np.array(alphaList).std()
        # xminmean = np.array(xminList).mean()
        #
        #
        # # reducedDir = Counter(data)
        # # tups = [(k,v) for k,v in reducedDir.items()]
        # # x = [k for k,v in tups]
        # # y = [v for k,v in tups]
        # # ymax = max(y) # I know that this is not the correct normalization, the slope is not affected
        #
        #
        # savepathPowerLaw = 'powerlawResultsmean/'+dataset+inDegreeDistPath
        # if not os.path.isdir('powerlawResultsmean'):
        #      os.makedirs(savepathPowerLaw)
        #
        # with open(savepathPowerLaw+date,"w+") as pr:
        #     savedata = [alphamean,alphaSigma,xminmean]
        #     output = " ".join([str(e) for e in savedata])
        #     pr.writelines(output)






    # fig, ax = plt.subplots()
    # plt.plot(xdegree,yfraction,'.')
    # xfit = np.array(list(range(1000)))
    # #xmin = results.xmin
    # #yfit = (results.alpha-1)/results.xmin*np.power(xfit/xmin,-results.alpha)
    # #plt.plot(xfit,yfit)
    #
    # plt.xlabel(r'Indegree')
    # plt.ylabel(r'Fraction of Nodes')
    # ax.spines['right'].set_visible(False)
    # ax.spines['top'].set_visible(False)
    # ax.set_yscale('log')
    # ax.set_xscale('log')
    # ax.set_aspect(aspect='equal')
    # ax.legend(("Data","Fit"))
    # inDegreeimgPath = '/home/paris/resultDataVisualization/MetaData/countDist/'+dataset+'/degreeDist/'
    #
    # if not os.path.isdir(currentPath):
    #     os.makedirs('/home/paris/resultDataVisualization/MetaData/countDist/'+dataset+'/degreeDist/')
    #
    # fig.savefig(currentPath+'powerlawtest' + '.eps', dpi=300, transpartent=True, bbox_inches='tight')
    #
    # plt.show()

# fit = powerlaw.Fit(data)
# fit.distribution_compare('power_law', 'exponential')
# fit.power_law.plot_pdf( color= 'b',linestyle='--',label='fit ccdf')
# fit.plot_pdf( color= 'g')
# plt.show()
#
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# from matplotlib import cm
# import os
# from matplotlib.text import Text
# import matplotlib as mpl
# from collections import defaultdict
#
#
# os.chdir('/home/parism/REGIO/resultDataVisualization/images/MetaData/countDist/degreeDist/')
# outDegreeDistPath = "inDegree/"
# outDegreeDistPath = "outDegree/"
# dates = os.listdir("inDegreeDistPath/")
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preview=True)
#
#
# with open(inDegreeDistPath) as f:
#     lines = f.readlines()
#
# data = [(int(line.rstrip().split(",")[0][1::]),int(line.rstrip().split(",")[1][:-1])) for line in lines]
#
# countNodes = [e[1] for e in data]
# totalNumerOfNodesIn = sum(countNodes)
#
# countNodesNormal = [c/totalNumerOfNodesIn for c in countNodes]
# countNodesNormalLog = [np.log10(c) for c in countNodesNormal]
# countNodesLog = [np.log10(c) for c in countNodes]
#
# inDegree = [e[0] for e in data]
# inDegreeNormal = [id/totalNumerOfNodesIn for id in inDegree]
# inDegreeNormalLog = [np.log10(id) for id in inDegreeNormal]
# inDegreeLog = [np.log10(id) for id in inDegree]
#
# fig, ax = plt.subplots()
# plt.plot(inDegreeNormalLog,countNodesNormalLog,'.')
# plt.xlabel(r'$Log_{10}$ Indegree normalized')
# plt.ylabel(r'$Log_{10}$ Fraction of Nodes')
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.set_ylim(top=0,bottom=-8.5)
# ax.set_xlim(left=-8.5,right=0)
# ax.set_aspect(aspect='equal')
# inDegreeimgPath = '../../images/graphs/IndegreeDist'
# # fig.savefig(inDegreeimgPath + '.svg', dpi=300, transpartent=True)
# fig.savefig(inDegreeimgPath + '.png', dpi=300, transpartent=True,bbox_inches='tight')
# plt.show()
#
#
#
# with open(outDegreeDistPath) as f:
#     lines = f.readlines()
#
# data = [(int(line.rstrip().split(",")[0][1::]),int(line.rstrip().split(",")[1][:-1])) for line in lines]
#
# countNodes = [e[1] for e in data]
# totalNumerOfNodesOut = sum(countNodes)
#
# countNodesNormal = [c/totalNumerOfNodesOut for c in countNodes]
# countNodesNormalLog = [np.log10(c) for c in countNodesNormal]
# countNodesLog = [np.log10(c) for c in countNodes]
#
# outDegree = [e[0] for e in data]
# outDegreeNormal = [id/totalNumerOfNodesOut for id in outDegree]
# outDegreeNormalLog = [np.log10(id) for id in outDegreeNormal]
# outDegreeLog = [np.log10(id) for id in outDegree]
#
# fig2, ax2 = plt.subplots()
# plt.plot(outDegreeNormalLog,countNodesNormalLog,'.')
# plt.xlabel(r'$Log_{10}$ Outdegree normalized')
# plt.ylabel(r'$Log_{10}$ Fraction of Nodes')
# ax2.spines['right'].set_visible(False)
# ax2.spines['top'].set_visible(False)
# ax2.set_ylim(top=0,bottom=-8.5)
# ax2.set_xlim(left=-8.5,right=0)
# ax2.set_aspect(aspect='equal')
# outDegreeimgPath = '../../images/graphs/OutdegreeDist'
# # fig2.savefig(outDegreeimgPath + '.svg', dpi=300, transpartent=True)
# fig2.savefig(outDegreeimgPath + '.png', dpi=300, transpartent=True, bbox_inches='tight')
# plt.show()
#
# d = defaultdict(list)
# for x,y in zip(outDegreeNormalLog,countNodesNormalLog):
#     d[y].append(x)
#
#
# for y,xlist in d.items():
#     d[y]=(np.mean(xlist),np.std(xlist))
#
# outDegreeNormalLog2=[]
# countNodesNormalLog2=[]
# t = []
# for y,xmean in d.items():
#     t.append((xmean,y))
#     outDegreeNormalLog2.append(xmean)
#     countNodesNormalLog2.append(y)
#
# tsorted = sorted(t,key=lambda x:x[0])
# outDegreeNormalLog = [e[0] for e in tsorted]
# countNodesNormalLog = [e[1] for e in tsorted]
#
# fig3, ax3 = plt.subplots()
# plt.plot(outDegreeNormalLog,countNodesNormalLog,'.')
# plt.xlabel(r'$Log_{10}$ Outdegree normalized')
# plt.ylabel(r'$Log_{10}$ Fraction of Nodes')
# ax3.spines['right'].set_visible(False)
# ax3.spines['top'].set_visible(False)
# ax3.set_ylim(top=0,bottom=-8.5)
# ax3.set_xlim(left=-8.5,right=0)
# ax3.set_aspect(aspect='equal')
# outDegreeimgPath = '../../images/graphs/OutdegreeDist'
# # fig3.savefig(outDegreeimgPath + '.svg', dpi=300, transpartent=True)
# fig3.savefig(outDegreeimgPath + '.png', dpi=300, transpartent=True, bbox_inches='tight')
# plt.show()
#
