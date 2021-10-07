# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 14:53:47 2018

@author: Camille John
"""

#%% FINDING COMMON IDS FROM MULTIPLE MONTHLY DATA FOLDERS
#%% DOCUMENT SETUP
# Operating system libraries
import os
cwd = os.getcwd()
import csv
# Time access and conversion library
import time as tm

#%% MAIN BODY OF CODE - Start
#%% STEP 1: INPUTS
# Create list of months to analyze 
yyyy_mm_list =  ['2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', #0-5
                 '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', #6-11
                 '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', #12-17
                 '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', #18-23
                 '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', #24-29
                 '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08'] #30-35
yyyy_mm_list = yyyy_mm_list[24:36] # Partial selection initiated (2017-09 to 2018-08)
#yyyy_mm_list = yyyy_mm_list[12:36] # Partial selection initiated (2016-09 to 2018-08)
#yyyy_mm_list = [yyyy_mm_list[14]] # Single selection initiated

#%% STEP 2: FIND COMMON IDS
#For each month analyzed, create a list of all the files found
listFiles = []
idx1 = 1
for yyyy_mm in yyyy_mm_list:
    if os.path.exists(os.path.join(cwd,yyyy_mm)):
        print ('\n')
        print('Year_Month Iteration %d of %d started: %s' %(idx1, len(yyyy_mm_list), yyyy_mm))
        starting = tm.time()
        print ('\n')  
        listFiles.append(os.listdir(os.path.join(cwd,yyyy_mm)))
        
    else:
        print (yyyy_mm + ': This month was not found in data set.')
        print ('\n')
    print(tm.time() - starting)
    idx1 += 1
    
# Do these month have duplicate data files?
import pandas as pd
for i in range(0,len(listFiles)):
    S = pd.Series(listFiles[i])
    if len(S.unique()) == len(S.index):
        print('Year_Month %d has no duplicates.' %(i))
    
#Create a list of all the files common to every month analyzed
common = listFiles[0]
for month in listFiles:
    common = list(set(common).intersection(month))

#Create csv file and write common ids to file
with open('CommonIds.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['filename'])
    for file in common:
        wr.writerow([file])
        
#%% MAIN BODY OF CODE - End
#%% NOTES - Start

#%% NOTES - End

    

       
        
