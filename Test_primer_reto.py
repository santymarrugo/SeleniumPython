import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.maximize_window()

driver.get("https://testingqarvn.com.es/")

time.sleep(2)

# Hacemos clic en el menu de practicas QA
menuPracticasQA = driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
menuPracticasQA.click()

# Buscamos nos vamos hasta donde es te elmento de contacto para hacer clic sobre el
btnContacto = driver.find_element(By.XPATH, "//a[contains(.,'Formulario de Contacto')]")
driver.execute_script("arguments[0].scrollIntoView()", btnContacto)

# Hacemos clic en el boton de contacto para llenar el formulario
btnContacto.click()

# Hacemos scroll hasta el boton submit
btnSubmit = driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-116')]")
driver.execute_script("arguments[0].scrollIntoView()",btnSubmit)

# LLenamos los campos del formulario
firstName = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-110')]")
firstName.send_keys("Manuel")
time.sleep(4)
lastName = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-111')]")
lastName.send_keys("Torrente")
email = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-112')]")
email.send_keys("mtorrente@miemail.com")
phone = driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-113')]")
phone.send_keys("3162424521")
inquiry = driver.find_element(By.XPATH, "//textarea[contains(@id,'wsf-1-field-114')]")
inquiry.send_keys("Tengo problemas con mi internet porque no me esta dando la velocidad contratada")
chkConsent = driver.find_element(By.XPATH, "//label[contains(@id,'wsf-1-label-115-row-1')]")
chkConsent.click()
time.sleep(3)
btnSubmit.click()
time.sleep(2)
driver.close()