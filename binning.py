#!/usr/bin/python2.7

import numpy as np
import sys
from numpy.random import *

AllData=np.zeros(0)
bnum=int(sys.argv[1])

for filename in sys.argv[2:]:
	data=np.loadtxt(filename)
	AllData=np.append(AllData,data)

N=len(AllData)

btime=N/bnum
barray=np.zeros(0)

for i in range(btime):
	barray=np.append(barray,np.average(AllData[i*bnum:i*bnum+bnum]))

print np.average(barray),"\t",np.std(barray)/(len(barray)**0.5)
