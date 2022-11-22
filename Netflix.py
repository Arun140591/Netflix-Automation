from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.netflix.com/in/login")

#username
driver.find_element("name","userLoginId").send_keys("sgpbalaji@gmail.com")
#password
driver.find_element("name","password").send_keys("balaji123")
#login
driver.find_element("css selector","button[data-uia=login-submit-button]").click()
import time
time.sleep(3)
#profile
driver.find_element("link text","Mohan").click()
time.sleep(2)
#trailor
driver.find_element("link text","Slumberland").click()


#Cast
title = driver.find_element("xpath","/html/body/div[3]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]").text
print("title")
time.sleep(3)
#Description
title = driver.find_element("xpath","/html/body/div[3]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[1]/p/div").text
print("title")

