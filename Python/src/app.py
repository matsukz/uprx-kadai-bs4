from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
from dotenv import load_dotenv
load_dotenv()

load_dotenv()

from login import login_uprx
from get_task import uprx_get_task

options = webdriver.ChromeOptions()
options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://sele_selenium:4444/wd/hub',
             options = options
            )

driver.implicitly_wait(10)

login_uprx(
    driver,
    os.getenv("uprx_link"),
    os.getenv("userid"),
    os.getenv("userpass")
)

time.sleep(3)

kadai_list = uprx_get_task(driver)
if kadai_list == {}:
    print("課題なし")
else:
    for kadai in kadai_list:
        print(kadai)

driver.quit()