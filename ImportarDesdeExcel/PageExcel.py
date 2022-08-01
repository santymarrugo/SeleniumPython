import unittest
from selenium.webdriver.common.by import By


class CargarExcel:

    def __init__(self, driver):
        self.driver = driver

        # Localizadores
        self.inputNombre = (By.XPATH, "//input[contains(@id,'wsf-1-field-21')]")
        self.inputApellido = (By.XPATH, "//input[contains(@id,'wsf-1-field-22')]")
        self.inputEmail = (By.XPATH, "//input[contains(@id,'wsf-1-field-23')]")
        self.inputTelefono = (By.XPATH, "//input[contains(@id,'wsf-1-field-24')]")
        self.inputDireccion = (By.XPATH, "//textarea[contains(@id,'wsf-1-field-28')]")
        self.btnEnviar = (By.XPATH, "//button[contains(@id,'wsf-1-field-27')]")

    # Metodos / Funciones
    def llenarFormulario(self, nombre, apellido, email, telefono, direccion):
        self.driver.find_element(*self.inputNombre).send_keys(nombre)
        self.driver.find_element(*self.inputApellido).send_keys(apellido)
        self.driver.find_element(*self.inputEmail).send_keys(email)
        self.driver.find_element(*self.inputTelefono).send_keys(telefono)
        self.driver.find_element(*self.inputDireccion).send_keys(direccion)

    def clickEnviarFormulario(self):
        self.driver.find_element(*self.btnEnviar).click()


