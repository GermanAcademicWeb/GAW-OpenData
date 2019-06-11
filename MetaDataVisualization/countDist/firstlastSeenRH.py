from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.colors as colors


#homepath
homepath = '/home/parism/PhD/REGIO/Comparability/GAW_visualization_python/ProjectComparabilityAndExploration/'

with open(homepath +"resultData/MetaData/countDist/RHFirstLastSeed/result2") as rs2:
    lines = rs2.readlines()

cleanlines = [line[1:-2] for line in lines]
dataArray = [line.split(",") for line in cleanlines]

firstSeen = [ar[-2] for ar in dataArray]
lastSeen = [ar[-1] for ar in dataArray]

firstSeenTime=[datetime.strptime(fs, '%Y%m%d%H%M%S') for fs in firstSeen]
lastSeenTime=[datetime.strptime(fs, '%Y%m%d%H%M%S') for fs in lastSeen ]

epoch = datetime.utcfromtimestamp(0)

xt = [(st-epoch).total_seconds()/(60*60*24*365.25)+1970 for st in firstSeenTime]
yt = [(st-epoch).total_seconds()/(60*60*24*365.25)+1970 for st in lastSeenTime]

fig2, ax2 = plt.subplots()
ax2.plot(xt,yt,'.',label="Retired host first-last time stamp")
ax2.set_ylabel(r'Last time stamp')

ax2.set_xlabel(r'First time stamp')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18),   ncol=3, fancybox=True, shadow=True)
# ax2.legend()
ax2.set_ylim(bottom=min(yt)-0.05,top=max(yt)+0.05)
ax2.set_xlim(left=min(xt)-0.05,right=max(xt)+0.05)
ax2.set_aspect(1.0)
# inDegreeimgPath = 'SDcom'
fig2.savefig(homepath+"resultDataVisualization/images/MetaData/countDist/RHFirstLastSeed/" +"firstlastseen"+ ".eps", dpi=300, transpartent=True,bbox_inches='tight')
plt.show()

