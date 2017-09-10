#! python3

# AutoMail.py - Automatically mail message to specific mail address from commend line
# Udage : AutoMail.py Email_address Message

import requests, sys, bs4
from selenium import webdriver

browser = webdriver.Chrome()
