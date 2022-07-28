from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tiempo = 3
# Instanciamos el objeto del WebDriver
driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()

buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
time.sleep(tiempo)

buscar.send_keys('C:\\Users\marr801550\\PycharmProjects\\Curso_selenium\\Imagenes\\demoFoca.jpg')
time.sleep(tiempo)

rbtnImage = driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]")
rbtnImage.click()
time.sleep(tiempo)

btnUpload = driver.find_element(By.XPATH, "//input[contains(@type,'submit')]")
btnUpload.click()
time.sleep(tiempo)


driver.close()
