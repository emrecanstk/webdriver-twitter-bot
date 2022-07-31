from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

tarayici = webdriver.Chrome()

tarayici.get('https://twitter.com/i/flow/login')
time.sleep(7)



