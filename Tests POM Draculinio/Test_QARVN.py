import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Pages.PageIndex import *


class QARVN(unittest.TestCase):
    # Metodo setUp, aqui podemos levantar el browser, ir a algun sitio en particular , cosas que se van a repetir en
    # todos nuestros casos
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="../geckodriver.exe")
        self.driver.get("https://testingqarvn.com.es/")
        self.driver.maximize_window()
        time.sleep(2)

    def test_ComboBox(self):
        menu_practicasQA = self.driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
        menu_practicasQA.click()
        btn_combox = self.driver.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light'][contains(.,'ComboBox')]")
        self.driver.execute_script("arguments[0].scrollIntoView()", btn_combox)
        time.sleep(3)
        btn_combox.click()
        time.sleep(2)
        btn_submit = self.driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-52')]")
        self.driver.execute_script("arguments[0].scrollIntoView()", btn_submit)

        # Name
        name = self.driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-45')]")
        name.send_keys("Santiago Jose")
        time.sleep(3)
        # LastName
        lastname = self.driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-46')]")
        lastname.send_keys("Marrugo Monsalve")
        # Email
        email = self.driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-47')]")
        email.send_keys("santiago@gmail.com")
        # Phone
        phone = self.driver.find_element(By.XPATH, "//input[contains(@id,'wsf-1-field-48')]")
        phone.send_keys("3009898765")
        # Address
        address = self.driver.find_element(By.XPATH, "//textarea[contains(@id,'wsf-1-field-49')]")
        address.send_keys("Caracoles mz 34 lote 18")
        # Languages CheckBox
        languageCB = self.driver.find_element(By.XPATH, "//label[contains(@id,'wsf-1-label-50-row-3')]")
        languageCB.click()
        # Languages RadioButton
        languageRB = self.driver.find_element(By.XPATH, "//label[contains(@id,'wsf-1-label-51-row-3')]")
        languageRB.click()
        # Operative System ComboBox
        op = Select(self.driver.find_element(By.XPATH, "//select[contains(@id,'wsf-1-field-53')]"))
        op.select_by_value("Mac")
        time.sleep(3)
        # Clic Submit
        btn_submit.click()
        time.sleep(3)
        # Message send success
        mSuccess = self.driver.find_element(By.XPATH, "//p[contains(text(),'Gracias por tu encuesta.')]").text
        # assert verification to success execution of test
        self.assertEqual(mSuccess, "Gracias por tu encuesta.")

    def test_requestProduct(self):
        menu_practicasQA = self.driver.find_element(By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
        menu_practicasQA.click()
        btn_productos = self.driver.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_13 et_pb_bg_layout_light'][contains(.,'Productos')]")
        self.driver.execute_script("arguments[0].scrollIntoView()", btn_productos)
        time.sleep(3)
        btn_productos.click()
        btn_submit = self.driver.find_element(By.XPATH, "//button[contains(@id,'wsf-1-field-167')]")
        self.driver.execute_script("arguments[0].scrollIntoView()", btn_submit)
        time.sleep(3)

    # Nos indica que hacer una vez termine cada caso de prueba, esto sucedera en todos los casos existentes
    def tearDown(self):
        # self.driver.execute_script("alert('Fin del test')")
        # time.sleep(2)
        # self.driver.switch_to.alert.accept()
        self.driver.quit()
