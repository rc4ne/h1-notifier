#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import pickle
import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send',"HackerOne", message])
    return

filename = 'h1_newprog.pk'
prev = ""


if os.path.isfile(filename):
    with open(filename, 'rb') as fi:
        prev = pickle.load(fi)
else:
    with open(filename, 'wb') as fi:
        pickle.dump("Just initiating the file..", fi)

# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
chrome_driver = "chromedriver.exe" # path to driver (make sure driver version is same as browser installed)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://hackerone.com/directory/programs?offers_bounties=true&order_direction=DESC&order_field=started_accepting_at")
driver.implicitly_wait(20)
current = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/div/div[2]/div[1]/div/span/strong/a').get_attribute("href")
driver.quit()
if current != prev:
	with open(filename, 'wb') as fi:
		pickle.dump(current, fi)
		sendmessage("New program introduced! "+current)
else:
	sendmessage("No new program introduced yet!")