from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
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

# Obtenemos el elemento del menu Practicas QA
menuPracticasQA = driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
# Pasamos el mouse por encima del Menu
accionMouseOver.move_to_element(menuPracticasQA).perform()
time.sleep(2)

subMenuDatosPersonales = driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/datos-personales/'][contains(.,'Datos Personales')])[1]")
subMenuDatosPersonales.click()
driver.execute_script("alert('Hola esto es una alerta')")
time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(3)

# driver.close()
