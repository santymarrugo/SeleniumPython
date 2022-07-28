import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

tiempo = 8
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")

driver.maximize_window()

time.sleep(tiempo)
nombre = driver.find_element(By.ID, "userName")
nombre.send_keys("Santiago Marrugo Monsalve")
nombre.send_keys(Keys.TAB)

driver.get("https://www.tutorialselenium.com/")
time.sleep(tiempo)

driver.get("https://testingqarvn.com.es/")
time.sleep(tiempo)

driver.back()
time.sleep(tiempo)

driver.back()
time.sleep(tiempo)

driver.forward()
time.sleep(tiempo)

driver.close()
