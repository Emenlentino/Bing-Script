import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Browser():
    # Function to login to Bing Rewards

    def wait_for(sec=2):
        print(f'waiting {sec} seconds...', flush=True)
        time.sleep(sec)
        print('done')

    chromedriverpath = os.getcwd() + '.C:/Program Files/Google/Chrome/Application/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.binary_location = chromedriverpath
    service = webdriver.ChromeService(executable_path=chromedriverpath)
    driver = webdriver.Chrome(service=service,options=options)

    path_to_json = "./form_data/accounts.json"

    with open(path_to_json , "r") as datafile:
        credential = json.load(datafile)

    user_data = credential["username"]
    pass_data = credential["password"]

    try:
        driver.get("https://login.live.com/")
        wait_for(10)
        elem = driver.find_element("name",'loginfmt')
        elem.clear()
        elem.send_keys(user_data) # add your login email id
        elem.send_keys(Keys.RETURN)
        wait_for(5)
        elem1 = driver.find_element("name",'passwd')
        elem1.clear()
        elem1.send_keys(pass_data) # add your password
        elem1.send_keys(Keys.ENTER)
        wait_for(7)

    except Exception as e:
        print(e)
        wait_for(4)

    # Invoked login_session to detect page url !            
    if "login" not in driver.current_url.lower():
        url_base = 'http://www.bing.com/search?q='
        print(url_base)
    else:
        print("Login failed.")
        return None

Browser()