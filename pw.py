#! /usr/bin/env python3

# pw.py - An insecure password locker program

PASSWORDS = {'email': 'F7min1BDuvMJuxESSKHF3qfe4qTdsaf',
             'blog': 'VMdasfifhasdkj;lskhg93021urjds;v',
             'luggage': '12345'}


import sys, pyperclip

if len(sys.argv) < 2:
    print('usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first commend line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')

else:
    print('There is no account named ' + account)

