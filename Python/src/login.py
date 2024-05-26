from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

def login_uprx(driver, url:str ,userid:str, userpasswd:str):

    driver.get(url)

    time.sleep(2)

    id = driver.find_element(By.ID, "loginForm:userId")
    passwd = driver.find_element(By.ID, "loginForm:password")

    id.clear()
    passwd.clear()

    id.send_keys(userid)
    passwd.send_keys(userpasswd)

    driver.find_element(By.ID, "loginForm:loginButton").click()

    time.sleep(5)