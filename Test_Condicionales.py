from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()

# Creamos un objeto de la clase ActionChains
accionMouseOver = ActionChains(driver)

driver.get("https://testingqarvn.com.es/")

imagenLogoPagina = driver.find_element(By.XPATH, "//img[@src='http://testingqarvn.com.es/wp-content/uploads/2022/01/logo3.png']")

visible = imagenLogoPagina.is_displayed()

if visible == True:
    driver.execute_script("alert('Elemento VISIBLE')")
else:
    driver.execute_script("alert('Elemento NO VISIBLE')")


# driver.close()