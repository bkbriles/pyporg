#! /usr/bin/python3

import os
import time

# Dummy vars for now
# TODO: Make file_path user defined!
file_path   = '/home/brian/test/PYPORG_TEST/'
folder_name = 'MKDIR_TEST'

file_path = os.chdir(file_path)

# Iterate through directory, splitting file name and file extension.
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    # Grab the month the file was last modified    
    try:
        #mod_stat = os.stat(f)
        file_stats = time.ctime(os.stat(f).st_mtime)
        f_day, f_month, f_date, f_time, f_year = file_stats.split()
    except IOError:
        print('Error: Name or info of file doesn\'t exist')
    else:
        #print("file modified: "), time.asctime(time.localtime(mod_stat.st_ctime_ns))
        #print("file modified: " + str(mod_stat.st_ctime_ns)) #Works
        print(f_month)

        # Get rid of the nonsense and only keep the month. ex. 'Jul'

    #print('DEBUG: mod_stat: ' + str(mod_stat.st_ctime_ns))

    try:
        if file_ext == '.txt':
            os.makedirs(folder_name)
    except FileExistsError:
        print('Error: Filename ' + folder_name + ' exists!')