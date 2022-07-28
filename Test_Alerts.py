from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.maximize_window()

# Creamos un objeto de la clase ActionChains
accionMouseOver = ActionChains(driver)

driver.get("https://testingqarvn.com.es/")

# Obtenemos el elmento del menu Cursos
menuCursos = driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/cursos/'][contains(.,'Cursos')])[1]")
# Pasamos el mouse por encima del menu
accionMouseOver.move_to_element(menuCursos).perform()
time.sleep(2)

# Creamos una alerta
driver.execute_script("alert('Hola esto es una alerta')")
time.sleep(2)
# Cerramos la alerta
driver.switch_to.alert.accept()
time.sleep(3)

driver.close()