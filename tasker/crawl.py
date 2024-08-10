from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


search_url = "https://www.bing.com/"

print('Please wait while we update!', flush=True)
time.sleep(5)

session = requests.Session()
login_page = session.get(search_url)
soup = BeautifulSoup(login_page.content, 'html.parser')

search_engine = []

for item in search_engine:
    time.sleep(1)
    search_field = search_url.find_element