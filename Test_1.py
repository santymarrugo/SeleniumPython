import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")

driver.maximize_window()


nombre = driver.find_element(By.ID, value="userName")
nombre.send_keys("Santiago")
email = driver.find_element(By.ID, value="userEmail")
email.send_keys("santiago@gmail.com")
direccion = driver.find_element(By.ID, value="currentAddress")
direccion.send_keys("Barrio la carolina mz f lote 36, piso 2.")
direccion_permanente = driver.find_element(By.ID, value="permanentAddress")
direccion_permanente.send_keys("Mamonal KM 5")
btn_enviar = driver.find_element(By.CSS_SELECTOR, value="#submit")
btn_enviar.click()


driver.close()
