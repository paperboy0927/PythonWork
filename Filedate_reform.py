#! python3
# renameDates.py - Renames flienames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# create a regex that matches files with the American date format.

datepattern = re.compile(r"""^(.*?) # all text before the data
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one ore two digits for the day
    ((19|20)\d\d)                   # for digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datepattern.search(amerFilename)

    #skip files withou a date.
    if mo ==None:
        continue

    # get th different parts of the filename.

    beforePart = mo.group(1)
    monthpater = mo.group(2)
    daypart    = mo.group(4)
    yearpart   = mo.group(6)
    afterpart  = mo.group(8)

