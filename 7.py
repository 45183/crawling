from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

URL = "https://papago.naver.com/"
driver.get(URL)
time.sleep(3)

question = input("번역할 내용을 입력하세요. : ")

form = driver.find_element_by_css_selector("textarea#txtSource")
form.send_keys(question)

button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
time.sleep(2)

result = driver.find_element_by_css_selector("div#txtTarget")
print(question, "->", result.text)

driver.close()