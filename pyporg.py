#! /usr/bin/python3

import os
import time

# Dummy vars for now
file_path       = '/home/brian/test/PYPORG_TEST/'
no_duplicates   = False
chk_jpg         = True
chk_jpeg        = False
chk_png         = True

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

    if chk_jpg == True:
        fileTransfer(no_duplicates)
    if chk_jpeg == True:
        fileTransfer(no_duplicates)
    if chk_png == True:
        fileTransfer(no_duplicates)


def fileTransfer(no_duplicates):
    if os.path.isdir(new_folder):
        print("Moving '" + f + "' to '" + new_folder + "'")
        os.rename(f, new_folder + "/" + f)
    else:
        print("Creating directory: \'" + new_folder +"'")
        os.makedirs(new_folder)
        print("Moving '" + f + "' to '" + new_folder + "'")
        os.rename(f, new_folder + "/" + f)

    #if no_duplicates == True:
        # Check for duplicate files and remove