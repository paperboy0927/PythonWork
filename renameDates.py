#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# create a regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?)     # all test before the data
    ((0|1)?\d)-                          # one or two digits for the month
    ((0|1|2|3)?\d)-                      # one or two digits for the date
    ((19|20)\d\d)                         # four digits forthe year
    (.*?)$
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    print(amerFilename)
    mo = datePattern.search(amerFilename)
    print(type(mo))
    # Skip files without at date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    #Form the European style filename
    euroFilename = beforePart + dayPart + '-' +monthPart + '-' + yearPart + afterPart

    #get the full, absolute file paths

    absworkingDir = os.path.abspath('.')
    print(absworkingDir)
    amerFilename = os.path.join(absworkingDir, amerFilename)
    euroFilename = os.path.join(absworkingDir, euroFilename)

    #Rename the files

    print('Renaming "%s" to "%s" ...' %(amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # uncomment after testing

