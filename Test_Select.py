import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://testingqarvn.com.es/")
driver.maximize_window()
#Accedemos al menu donde estan las practicas de QA
menuPracticasQA = driver.find_element(By.XPATH, "(//A[@href='https://testingqarvn.com.es/practicas-qa/'][text()='Prácticas QA'])[1]")
menuPracticasQA.click()
#Hacemos scroll hasta el final de la pagina
driver.execute_script("window.scrollTo(0,1500)")

#Entramos a la parte del curso donde estan los combobox
btnComboBox = driver.find_element(By.XPATH, "//A[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light'][text()='ComboBox']")
btnComboBox.click()

#Hacemos scroll hasta el final de la pagina
driver.execute_script("window.scrollTo(0,1500)")

# Nombre
nombre = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-45')]")
nombre.send_keys("Santiago Jose")
# Apellidos
apellidos = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-46')]")
apellidos.send_keys("Marrugo Monsalve")
# Email
email = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-47')]")
email.send_keys("santiago@marrugo.com")
# Phone
phone = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-48')]")
phone.send_keys("3162525612")
# Direccion
direccion = driver.find_element(By.XPATH, "//textarea[contains(@id,'wsf-1-field-49')]")
direccion.send_keys("Cartagena Colombia")
# Lenguaje CheckBox
lenguajePython = driver.find_element(By.XPATH, "//label[contains(@id,'wsf-1-label-50-row-2')]")
lenguajePython.click()
# Lenguaje Radio Button
lenguajeSelenium = driver.find_element(By.XPATH, "//label[contains(@id,'wsf-1-label-51-row-3')]")
lenguajeSelenium.click()

#Seleccionamos el valor del combobox
DD_sistOper = Select(driver.find_element(By.XPATH, "//select[contains(@id,'wsf-1-field-53')]")).select_by_value("Linux")

time.sleep(3)
#Hacemos clic en el boton Submit
btnEnviar = driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-52')]")
btnEnviar.click()

time.sleep(3)
driver.close()

