import os
from selenium import webdriver

def open_chrome():
    return webdriver.Chrome('{}\chromedriver.exe'.format(os.path.dirname(__file__)))

