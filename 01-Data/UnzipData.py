# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:02:15 2019

@author: Camille John
"""

#%% UNZIPPING THE MONTHLY DATA FOLDERS
#%% DOCUMENT SETUP
# General Setup
import os
cwd = os.getcwd() # cwd: current working directory

#%% CUSTOM FUNCTIONS
def UnzipArchive(archive):
    import zipfile
    destination = os.path.join(cwd,archive)
    archive = os.path.join(cwd,archive+'.zip')
    # Unzip archive folder
    zf = zipfile.ZipFile(archive)
    # Return a list of archive members by name
    check = zf.namelist()
    # Extract all archive members and save to a new location
    zf.extractall(destination)
    # close archive folder
    zf.close()
    return (check)

#%% MAIN BODY OF CODE - Start
#%% STEP 1: INPUTS
dArchive_list = ['2015-09', '2015-10', '2015-11', '2015-12', '2016-01', '2016-02', #0-5
                 '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', #6-11
                 '2016-09', '2016-10', '2016-11', '2016-12', '2017-01', '2017-02', #12-17
                 '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', #18-23
                 '2017-09', '2017-10', '2017-11', '2017-12', '2018-01', '2018-02', #24-29
                 '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08'] #30-35
dArchive_list = dArchive_list[0:36]
#dArchive_list = [dArchive_list[1]]

#%% STEP 2: UNZIP DATA FILE
idx1 = 1
for archive in dArchive_list:      
    print('Archive Iteration %d of %d started: %s' % (idx1,len(dArchive_list), archive))
    if os.path.exists(os.path.join(cwd,archive +'.zip')):
        # Unzip archive, extract files and save files to a new location
        UnzipArchive(archive)
    else:
        print (str(archive) + ': This archive could not be located in this location.')   
    idx1 += 1

#%% MAIN BODY OF CODE - End
#%% NOTES - Start

#%% NOTES - End
