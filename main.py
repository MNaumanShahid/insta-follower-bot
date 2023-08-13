from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
import os

driver_path = os.environ.get("CHROMIUM_PATH")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

URL = "https://www.instagram.com/login"
USERNAME = os.environ.get("INSTA_USR")
PWD = os.environ.get("INSTA_PWD")

driver = webdriver.Chrome(service=Service(executable_path=f"r{driver_path}"), options=chrome_option)
driver.get(URL)
time.sleep(2)
username_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username_field.send_keys(USERNAME)
pwd_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
pwd_field.send_keys(PWD)
pwd_field.send_keys(Keys.ENTER)

time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a').click()
time.sleep(2)
search_field = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
search_field.send_keys("bugatti")
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(2)

buttons = driver.find_elements(By.CSS_SELECTOR, "div._aano button")
for button in buttons:
    try:
        button.click()
        time.sleep(1)
    except ElementClickInterceptedException:
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]').click()
        print("Following limit reached.")
        break
