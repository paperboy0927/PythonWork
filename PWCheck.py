#! /usr/bin/env python3

import re

PWRegex_r1 = re.compile(r'\w{8,}')
PWRegex_r2 = re.compile(r'[A-Z]+')
PWRegex_r3 = re.compile(r'[a-z]+')

while True:
    password = input("please input password for check:")
    match1 = PWRegex_r1.search(password)
    match2 = PWRegex_r2.search(password)
    match3 = PWRegex_r3.search(password)
    if(match1 == None or match2 == None or match3 == None):
        print(password + " not match to rule, please try again")

    else:
        print(password + ' match to password rule')
        break



