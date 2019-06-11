import powerlaw
import os
from multiprocessing import Pool
from collections import Counter
# import matplotlib.pyplot as plt
import numpy as np





def writeAlpha(date):
    dataset = "ATSRH/"
    #   # local
    #os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
    os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
    inDegreeDistPath = "InDeg/"
    currentPath = "InDeg/"
    print(os.getcwd())
    with open(currentPath + date) as dd:
        data_unstriped = dd.readlines()
        data_stripped = [d.rstrip() for d in data_unstriped]
        tupelStr = [line[1:-1].split(',') for line in data_stripped]
        tupelArray = np.array(
            [(int(line[0]), int(line[1])) for line in tupelStr])  # deg = tupelArray[:,0], count  = tupelArray[:,1]

    normalization = tupelArray[:, 1].sum()

    data_pre = []
    for deg, count in tupelArray:
        data_pre.append([deg] * count)
    data = [el for line in data_pre for el in line]

    np.random.shuffle(data)  ## change this to 'data' if no resampling is desired
    results = powerlaw.Fit(data)


    savepathPowerLaw = 'powerlawResultsFULLRUN/' + dataset + inDegreeDistPath
    if not os.path.isdir('powerlawResultsFULLRUN'):
        os.makedirs(savepathPowerLaw)

    with open(savepathPowerLaw + date, "w+") as pr:
        savedata = [results.alpha, results.sigma, results.xmin]
        output = " ".join([str(e) for e in savedata])
        pr.writelines(output)



p = Pool(7)


inDegreeDistPath = "InDeg/"
outDegreeDistPath = "OutDeg/"

#cuts = [ "ATSRH/", "NRH/"]
# cuts = ["gaw/", "ATSRH/", "NRH/"]
#for dataset in cuts:
    # dataset = "ATSRH/"
    # # local
    # os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/degreeDist/'+dataset)
    # # os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
    # currentPath = inDegreeDistPath
    # dates = sorted(os.listdir(currentPath))
    # paths = [currentPath]*dates.__len__()
    # p.map(writeAlpha,dates)


dataset = "ATSRH/"
# local
#os.chdir('/home/parism/REGIO/resultData/MetaData/countDist/degreeDist/'+dataset)
os.chdir('/home/stud/mpa/REGIO/resultData/MetaData/countDist/degreeDist/' + dataset)
currentPath = inDegreeDistPath
dates = sorted(os.listdir(currentPath))
paths = [currentPath]*dates.__len__()
p.map(writeAlpha,dates)
