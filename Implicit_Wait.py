import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


tiempo = 1
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://demoqa.com/text-box")

nombre = driver.find_element(By.ID, value="userName")
nombre.send_keys("Santiago")

driver.maximize_window()

driver.close()