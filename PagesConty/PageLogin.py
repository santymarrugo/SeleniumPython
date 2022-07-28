import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class PageLogin:

    def __init__(self, driver):
        self.driver = driver

        self.input_usuario = (By.XPATH, "//input[contains(@id,'Email')]")
        self.input_password = (By.XPATH, "//input[contains(@id,'Password')]")
        self.link_olvide_contrasena = (By.XPATH, "//a[contains(.,'¿Olvidaste la contraseña?')]")
        self.btn_ingresar = (By.XPATH, "//input[contains(@id,'btnLogin')]")
        self.comboEmpresa = (By.XPATH, "//select[contains(@id,'EmpresaId')]")
        self.comboSucursal = (By.XPATH, "//select[contains(@id,'SucursalId')]")
        self.comboPuntoEmision = (By.XPATH, "//select[contains(@id,'PuntoEmisionId')]")
        self.btn_empresa_ingresar = (By.XPATH, "//input[contains(@id,'btnSeleccionEmpresa')]")
        self.labelInicio = (By.XPATH, "//label[contains(@id,'inicio')]")
        self.mensajeUserPassErrado = (By.XPATH, "//span[contains(@id,'mensaje')]")

    def userycontrasena(self, usuario, contrasena):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.btn_ingresar))
        self.driver.find_element(*self.input_usuario).send_keys(usuario)
        self.driver.find_element(*self.input_password).send_keys(contrasena)

    def clickIngresar(self):
        self.driver.find_element(*self.btn_ingresar).click()

    def seleccionarEmpresa(self, id_empresa):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.comboEmpresa))
        Select(self.driver.find_element(*self.comboEmpresa)).select_by_value(id_empresa)

    def seleccionarSucursal(self, id_sucursal):
        Select(self.driver.find_element(*self.comboSucursal)).select_by_value(id_sucursal)

    def seleccionarPuntoEmision(self, id_puntoemision):
        Select(self.driver.find_element(*self.comboPuntoEmision)).select_by_value(id_puntoemision)

    def clickIngresoEmpresa(self):
        self.driver.find_element(*self.btn_empresa_ingresar).click()

    def inicioExitoso(self, mensaje):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.labelInicio))
        tcAssert = unittest.TestCase("__init__")
        msjLabelInicio = self.driver.find_element(*self.labelInicio).text
        tcAssert.assertEqual(msjLabelInicio, mensaje)

    def inicioFallido(self, mensaje):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.mensajeUserPassErrado))
        tcAssert = unittest.TestCase("__init__")
        msjError = self.driver.find_element(*self.mensajeUserPassErrado).text
        tcAssert.assertEqual(msjError, mensaje)



