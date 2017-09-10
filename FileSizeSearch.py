#! python3
# Search specific folder with file size larger than 10Mb

import os, re, shutil

# Walk the entire folder tree and print the file name on screen

def filesize(folder,size):
    folder = os.path.abspath(folder)
    print(folder)
    size = size *1024*1024

    for foldername, subfolder, filenames in os.walk(folder):
        for filename in filenames:
            targetfile = os.path.join(foldername, filename)
            # print(targetfile + ' '+ str(os.path.getsize(targetfile)))
            if os.path.getsize(targetfile) > size:
                print(targetfile, os.path.getsize(targetfile))



filesize('/Users/paperboy/',5)
