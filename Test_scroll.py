from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

tiempo = 3
driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.maximize_window()

driver.get("https://pixabay.com/es/")
time.sleep(tiempo)

# Seleccionamos el elemento
buscar = driver.find_element(By.XPATH, "//label[contains(.,'Descubre más')]")
# Se hace el scroll mediante una funcion JavaScript, y se va hasta donde se encuentre dicho elemento
ir = driver.execute_script("arguments[0].scrollIntoView()", buscar)

time.sleep(tiempo)

driver.close()
