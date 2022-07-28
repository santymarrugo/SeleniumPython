import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageIndex:
    # Inicializamos la clase y le pasamos el webdriver en el constructor
    # ESTO SIEMPRE VA
    def __init__(self, driver):
        self.driver = driver

        self.menu_practicasQA = (By.XPATH, "(//a[@href='https://testingqarvn.com.es/practicas-qa/'][contains(.,'Prácticas QA')])[1]")
        self.btn_combox = (By.XPATH, "//A[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light'][text()='ComboBox']")
        self.btn_submit = (By.XPATH, "//button[contains(@id,'wsf-1-field-52')]")
        self.input_nombre = (By.XPATH, "//input[contains(@id,'wsf-1-field-45')]")
        self.input_apellido = (By.XPATH, "//input[contains(@id,'wsf-1-field-46')]")
        self.input_correo = (By.XPATH, "//input[contains(@id,'wsf-1-field-47')]")
        self.input_telefono = (By.XPATH, "//input[contains(@id,'wsf-1-field-48')]")
        self.input_direccion = (By.XPATH, "//textarea[contains(@id,'wsf-1-field-49')]")
        self.lenguajeCB = (By.XPATH, "//label[contains(@id,'wsf-1-label-50-row-3')]")
        self.languageRB = (By.XPATH, "//label[contains(@id,'wsf-1-label-51-row-3')]")
        self.op = (By.XPATH, "//select[contains(@id,'wsf-1-field-53')]")
        self.btn_submit = (By.XPATH, "//button[contains(@id,'wsf-1-field-52')]")
        self.mSuccess = (By.XPATH, "//p[contains(text(),'Gracias por tu encuesta.')]")

    def accesoMenuPracticasQA(self):
        self.driver.find_element(*self.menu_practicasQA).click()

    def accesoBotonComboBox(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element(*self.btn_combox))
        self.driver.find_element(*self.btn_combox).click()

    def datosPersonales(self, nombre, apellido, correo, telefono, direccion):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element(*self.btn_submit))
        name = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.input_nombre))
        self.driver.find_element(*self.input_nombre).send_keys(nombre)
        time.sleep(2.2)
        self.driver.find_element(*self.input_apellido).send_keys(apellido)
        self.driver.find_element(*self.input_correo).send_keys(correo)
        self.driver.find_element(*self.input_telefono).send_keys(telefono)
        self.driver.find_element(*self.input_direccion).send_keys(direccion)

    def elegirLenguajeChkBox(self):
        self.driver.find_element(*self.lenguajeCB).click()

    def elegirLenguajeRdButton(self):
        self.driver.find_element(*self.languageRB).click()

    def seleccionarSO(self, sistemaElegido):
        Select(self.driver.find_element(*self.op)).select_by_value(sistemaElegido)

    def enviarDatos(self):
        self.driver.find_element(*self.btn_submit).click()
        time.sleep(3)

    def verificarEnvioDatos(self, mensaje):
        msAssert = unittest.TestCase('__init__')
        ms = self.driver.find_element(*self.mSuccess).text
        msAssert.assertEqual(mensaje, ms)
