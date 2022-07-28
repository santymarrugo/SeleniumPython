import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageLogin:

    def __init__(self, driver):
        self.driver = driver

        self.inputUsuario = (By.XPATH, "//input[contains(@id,'Email')]")
        self.inputPass = (By.XPATH, "//input[contains(@id,'Password')]")
        self.btnIngresar = (By.XPATH, "//input[contains(@id,'btnLogin')]")
        self.cmbEmpresa = (By.XPATH, "//select[contains(@id,'EmpresaId')]")
        self.cmbSucursal = (By.XPATH, "//select[contains(@id,'SucursalId')]")
        self.cmbPuntoEmision = (By.XPATH, "//select[contains(@id,'PuntoEmisionId')]")
        self.btnIngresaEmpresa = (By.XPATH, "//input[contains(@id,'btnSeleccionEmpresa')]")
        self.lblPanelControl = (By.XPATH, "//span[@class='menu_title'][contains(.,'Panel de control')]")
        self.msjFalloLogin = (By.XPATH, "//span[contains(@id,'mensaje')]")

    def Login(self, usuario, contrasena):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.btnIngresar))
        self.driver.find_element(*self.inputUsuario).send_keys(usuario)
        self.driver.find_element(*self.inputPass).send_keys(contrasena)

    def clickBtnIngresar(self):
        self.driver.find_element(*self.btnIngresar).click()

    def seleccionEmpresa(self, idEmpresa):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.btnIngresaEmpresa))
        Select(self.driver.find_element(*self.cmbEmpresa)).select_by_value(idEmpresa)

    def seleccionSucursal(self, idSucursal):
        Select(self.driver.find_element(*self.cmbSucursal)).select_by_value(idSucursal)

    def seleccionPuntoEmision(self, idPuntoEmision):
        Select(self.driver.find_element(*self.cmbPuntoEmision)).select_by_value(idPuntoEmision)

    def clickIngresarEmpresa(self):
        self.driver.find_element(*self.btnIngresaEmpresa).click()

    def verificarLoginExitoso(self, mensaje):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.lblPanelControl))
        tcAssert = unittest.TestCase("__init__")
        msjPanelControl = self.driver.find_element(*self.lblPanelControl).text
        tcAssert.assertEqual(msjPanelControl, mensaje)

    def verificarLoginFallido(self, mensaje):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.msjFalloLogin))
        tcAssert = unittest.TestCase("__init__")
        msjLoginFallido = self.driver.find_element(*self.msjFalloLogin).text
        tcAssert.assertEqual(msjLoginFallido, mensaje)

