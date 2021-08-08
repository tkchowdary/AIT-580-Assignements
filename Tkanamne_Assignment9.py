#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 20:41:52 2019

@author: tharun
"""
#importing the nltk
import nltk

#import regular expression
import re

#getrid of "stopwords", from corpus
from nltk.corpus import stopwords

#opening the file from source
file = open('BikeInjury.txt', 'r')

#command to read and inout the file
s = file.read()

#displaying contents
print(s)

nltk.download('punkt')

tokens = re.sub(r'\W+', ' ', s)

#Converting it to lower case
tokens = tokens.lower()

tokens = tokens.split()

tokens = [word for word in tokens if word not in stopwords.words('english')]
#print all the invidual words
print(tokens)



i_injuries = ['knee','fractured','lacerations','elbows','head','neck','lung','broken','scrapes',

            'clavicle','ribs','traumatic','contusion','hip','hematoma','elbow','shoulders',

            'forearm','limbs','brain','stomach','thigh','wrist','chin','abrasion']



cmn_i_injuries = []



for i in i_injuries:

    for j in tokens:

        if i == j:

            cmn_i_injuries.append(i)    


#plot 25 most common injuries
freq_dist = nltk.FreqDist(cmn_i_injuries)

print(freq_dist)

print(freq_dist.most_common(25))

freq_dist.plot(25)






#to print few sentences
sentences = nltk.sentences_tokenize(s)

print(sentences[0])

print(sentences[1])

print(sentences[2])

print(sentences[3])

print(sentences[4])

print(sentences[5])

print(sentences[6])

print(sentences[7])

print(sentences[9])

print(sentences[10])
