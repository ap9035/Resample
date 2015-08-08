#!/usr/bin/python2.7

import numpy as np
import sys
from numpy.random import *

AllData=np.zeros(0)

for filename in sys.argv[1:]:
	data=np.loadtxt(filename)
	AllData=np.append(AllData,data)

N=len(AllData)

BootstrapList=np.zeros(0)

for i in range(N):
	SEED=randint(N)
	b_data=AllData[SEED]
	BootstrapList=np.append(BootstrapList,b_data)

print np.average(BootstrapList),"\t",np.std(BootstrapList)/(N**0.5)
