#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:00:06 2019

@author: tharun
"""


#c)
 #Explain how you accounted for any missing data, and how that may have affected your results
#to find missing data in a column


import pandas as pd
f=pd.read_csv("/Users/tharun/Atlantic.csv",sep=',') #read dataset
f['central_pressure'].isnull()
f['central_pressure'].fillna(0)

f['central_pressure'].plot(kind='hist',bins=50)

