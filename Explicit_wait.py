import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=("C:\Drivers\chromedriver.exe"))
driver.get("https://www.vta.co/")
driver.maximize_window()

# Como trabajar con el Explicitly Wait
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'×')]")))
btn.click()
driver.close()
