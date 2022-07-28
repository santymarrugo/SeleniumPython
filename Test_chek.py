from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=("C:\Drivers\chromedriver.exe"))

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

elementoChek = driver.find_element(By.XPATH, "//span[contains(text(),'Check Box')]")
elementoChek.click()
chekHome = driver.find_element(By.XPATH, "//span[contains(text(),'Home')]")
chekHome.click()
