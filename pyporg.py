#! /usr/bin/python3

import os
import time

# Dummy vars for now
file_path   = '/home/brian/test/PYPORG_TEST/'

file_path = os.chdir(file_path)

# Iterate through directory.
for f in os.listdir():
    try:
        # Split file name and file extension
        file_name, file_ext = os.path.splitext(f)
    except IOError:
        print('Error: file doesn\'t exist')
    else:
        # Store file mod time info
        file_stats = time.ctime(os.stat(f).st_mtime)
        f_day, f_month, f_date, f_time, f_year = file_stats.split()

    # Set a new folder name for f
    new_folder = f_year + " " + f_month

    if os.path.isdir(new_folder):
        os.rename(f, new_folder + "/" + f)
    else:
        os.makedirs(new_folder)
        os.rename(f, new_folder + "/" + f)     