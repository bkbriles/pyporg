#! /usr/bin/python3

import os

# Dummy vars for now
# TODO: Make file_path user defined!
file_path   = '/home/brian/test/'
folder_name = 'MKDIR_TEST'

file_path = os.chdir(file_path)

# Iterate through directory, splitting file name and file extension.
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    
    try:
        if file_ext == '.txt':
            os.makedirs(folder_name)
    except FileExistsError:
        print('Error: Filename ' + folder_name + ' exists!')

    if file_ext != '':
        print(file_ext)