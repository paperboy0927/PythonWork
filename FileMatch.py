#! python3
# Open .txt in specific folder & print lines with keyword "New York"

import os, re

FilePath = os.getcwd()
print(FilePath)

CapitalRegex = re.compile(r'New York')

for filename in os.listdir(FilePath):
    if filename[-4:] == '.txt':
        txtfile = open(FilePath+'/'+filename, 'r')
        for line in txtfile.readlines():
            match = CapitalRegex.search(line)
            if match != None:
                print(filename)
                print(line)




