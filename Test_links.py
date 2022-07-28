from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.maximize_window()

a = ActionChains(driver)

driver.get("https://testingqarvn.com.es/")

# Creamos una variable para guardar todos los links de la pagina
links = driver.find_elements(By.TAG_NAME, "a")
print("El numero de links que hay en la pagina es: ", len(links))

for numLinks in links:
    print(numLinks.text)

menuBarraSuperior = driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
a.move_to_element(menuBarraSuperior).perform()
time.sleep(2)

#
# driver.close()
