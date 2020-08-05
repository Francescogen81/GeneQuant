# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:05:49 2020

@author: fran8
"""

import csv

with open("profiles.csv", "r") as infile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers
   exampleData = list(reader)


with open("results.csv", "r") as infile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers
   exampleResultsData = list(reader)
   
   
profileDict = {}
j = 0

for i in exampleData:
    for j in range (0, len(exampleData)):
        profileDict.update({i[0]: i[1:]})   
        j += 1    #create a dictionary of profiles
   
resultDict =   {}
j = 0

for i in exampleResultsData:
    for j in range (0, len(exampleResultsData)):
        resultDict.update({i[0]: i[1:]})   
        j += 1            #create a dictionary of results
    