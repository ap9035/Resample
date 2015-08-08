#!/usr/bin/python2.7
import numpy as np
import sys

AllData=np.zeros(0)

for filename in sys.argv[1:]:
	data=np.loadtxt(filename)
	AllData=np.append(AllData,data)

print np.average(AllData),"\t",np.std(AllData)/(len(AllData)**0.5)
