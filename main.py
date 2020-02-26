import sys
from time import localtime
from time import sleep
from time import strftime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from check_internet import is_connected

"""
Set options:
"""

options = Options()
options.headless = True
profile = FirefoxProfile()
profile.set_preference('browser.cache.disk.enable', False)
profile.set_preference('browser.cache.memory.enable', False)
profile.set_preference('browser.cache.offline.enable', False)
profile.set_preference('network.cookie.cookieBehavior', 1)
profile.set_preference('network.http.phishy-userpass-length', 255)

GECKO_PATH = 'C:/Users\John\PycharmProjects\Plex_Invoice_Auto_Email\GrabPDF\geckodriver2.exe'
REMOTE_SERVER = "www.google.com"
RUN_TIME = strftime("%Y-%m-%d %I:%M:%S %p", localtime())

"""
Main Logic:
"""
internet = is_connected(REMOTE_SERVER)

if not internet:
    driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=GECKO_PATH)
    driver.set_page_load_timeout(60)
    try:
        driver.get('http://admin:6i9fTvEwG0@192.168.0.1/RouterStatus.asp')
    except:
        print("Can't get to the router!!!")
        sys.exit(2)

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,('//*[@id="reboot"]'))))
    driver.find_element_by_xpath('//*[@id="reboot"]').click()
    #driver.find_element_by_xpath('//*[@id="status"]').click()
    sleep(300)
    if is_connected(REMOTE_SERVER):
        print(RUN_TIME, "Rebooted the router!!")
    else:
        print(RUN_TIME, "Router did not reboot in 5 minutes!!")
elif internet:
    print(RUN_TIME, "Internet is accessible!!")
else:
    print(RUN_TIME, "Unknown error - please check logs!!")

