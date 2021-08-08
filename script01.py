#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:04:31 2019

@author: tharun
"""
#import nltk
import nltk
import re
#import corpus to import stopwords
from nltk.corpus import stopwords

file = open("BikeInjury.txt", "rt")
s=file.read()
print(s)
nltk.download('stopwords')
set(stopwords.words('english'))
print(s)
nltk.download('punkt')
a=re.sub(r'\W+','',s)
a=a.lower()
a=a.split()
print(a)
a=[word for word in a if word not in stopwords.words('english')]
print(a)

i_injuries = ['knee','fractured','lacerations','elbows','head','neck','lung','broken','scrapes','clavicle','ribs','traumatic','contusion','hip','hematoma','elbow','shoulders','forearm','limbs','brain','stomach','thigh','wrist','chin','abrasion']

injuries=[]
for i in i_injuries:
    for j in a:
        if i==j:
            i_injuries.append(i)
freq_dist=nltk.FreqDist(injuries)
print(freq_dist)            
print(freq_dist.most_common(25))  
freq_dist.plot(25)
