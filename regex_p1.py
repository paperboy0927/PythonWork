#! /usr/bin/env python3

import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242.')

print('Phone number found:'+ mo.group())

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = phoneNumberRegex.findall('Cell : 415-555-0000 Work: 415-666-0000')

print(mo2)


