from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

URL = "https://www.gmarket.co.kr/"
driver.get(URL)

time.sleep(3)

driver.close()