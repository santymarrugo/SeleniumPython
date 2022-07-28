import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class PageSolicitarProducto:
    # Inicializamos la clase y le pasamos el webdriver en el constructor
    # ESTO SIEMPRE VA
    def __init__(self, driver):
        self.driver = driver
        self.btn_productos = (
            By.XPATH, "//a[@class='et_pb_button et_pb_button_13 et_pb_bg_layout_light'][contains(.,'Productos')]")
        self.btn_submit = (By.XPATH, "//button[contains(@id,'wsf-1-field-167')]")
        self.input_nombre = (By.XPATH, "//INPUT[@id='wsf-1-field-156']")
        self.input_apellido = (By.XPATH, "//INPUT[@id='wsf-1-field-157']")
        self.input_correo = (By.XPATH, "//INPUT[@id='wsf-1-field-158']")
        self.input_telefono = (By.XPATH, "//INPUT[@id='wsf-1-field-159']")
        self.rb_producto = (By.XPATH, "//LABEL[@id='wsf-1-label-160-row-2']")
        self.seleccionar_cantidad = (By.XPATH, "//input[contains(@id,'wsf-1-field-161')]")
        self.input_direccion_1 = (By.XPATH, "//INPUT[@id='wsf-1-field-162']")
        self.input_direccion_2 = (By.XPATH, "//INPUT[@id='wsf-1-field-163']")
        self.input_ciudad = (By.XPATH, "//INPUT[@id='wsf-1-field-164']")
        self.combo_estado = (By.XPATH, "//SELECT[@id='wsf-1-field-165']")
        self.input_cod_postal = (By.XPATH, "//INPUT[@id='wsf-1-field-166']")
        self.msjEnvioExitoso = (By.XPATH, "//p[contains(.,'Thank you for placing your order.')]")

    def accesoBotonProductos(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element(*self.btn_productos))
        self.driver.find_element(*self.btn_productos).click()

    def formularioProductos(self, nombre, apellido, correo, telefono, direccion_1, direccion_2, ciudad, estado,
                            cod_postal):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element(*self.btn_submit))
        self.driver.find_element(*self.input_nombre).send_keys(nombre)
        time.sleep(2)
        self.driver.find_element(*self.input_apellido).send_keys(apellido)
        self.driver.find_element(*self.input_correo).send_keys(correo)
        self.driver.find_element(*self.input_telefono).send_keys(telefono)
        self.driver.find_element(*self.rb_producto).click()
        self.driver.find_element(*self.seleccionar_cantidad).click()
        self.driver.find_element(*self.input_direccion_1).send_keys(direccion_1)
        self.driver.find_element(*self.input_direccion_2).send_keys(direccion_2)
        self.driver.find_element(*self.input_ciudad).send_keys(ciudad)
        Select(self.driver.find_element(*self.combo_estado)).select_by_value(estado)
        self.driver.find_element(*self.input_cod_postal).send_keys(cod_postal)

    def enviarDatos(self, mensaje):
        # Instanciamos un objeto de la clase TestCase para poder usar los assert de unittest y le pasamos como parametro el '__init__'
        tcAssert = unittest.TestCase('__init__')
        self.driver.find_element(*self.btn_submit).click()
        time.sleep(2)
        msj = self.driver.find_element(*self.msjEnvioExitoso).text
        tcAssert.assertEqual(msj, mensaje)
        time.sleep(2)
