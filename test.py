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
    
    try:
        mod_date = os.stat(f)
    except IOError:
        print('Error: Name or info of file doesn\'t exist')
    else:
        print("file modified: ", time.asctime(time.localtime(mod_date.st_mtime)) + ' ' + f)
        

    ''' try:
        if file_ext == '.txt':
            os.makedirs(folder_name)
    except FileExistsError:
        print('Error: Filename ' + folder_name + ' exists!')

    if file_ext != '':
        print(file_ext) '''