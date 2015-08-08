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
MainList=np.zeros(0)

for i in range(500):
	BootstrapList=np.zeros(0)
	for j in range(N):
		SEED=randint(N)
		b_data=AllData[SEED]
		BootstrapList=np.append(BootstrapList,b_data)
	MainList=np.append(MainList,np.average(BootstrapList))

print np.average(MainList),"\t",np.std(MainList)
