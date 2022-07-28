import time
import unittest

from selenium.webdriver.common.by import By


class PageDatosPersonales:

    def __init__(self, driver):
        self.driver = driver
        '''
        Declaramos todos lo elementos de la clase en el constructor de la misma en forma de tupla, para tener acceso a
        ellos en todos los metodos que tenga la clase, y de esta forma solo escribirlos una vez, si desarrollo cambia 
        algo solo se debe cambiar aqui y se replica en los metodos donde usemos estos elementos.
        ***NOTA: aqui le pasamos una referencia del elemento para que lo busque por XPATH, este se guarda en una 
        variable
        '''
        self.input_nombre = (By.XPATH, "//INPUT[@id='wsf-1-field-21']")
        self.input_apellido = (By.XPATH, "//INPUT[@id='wsf-1-field-22']")
        self.input_correo = (By.XPATH, "//INPUT[@id='wsf-1-field-23']")
        self.input_telefono = (By.XPATH, "//INPUT[@id='wsf-1-field-24']")
        self.input_direccion = (By.XPATH, "//TEXTAREA[@id='wsf-1-field-28']")
        self.btn_enviar = (By.XPATH, "//BUTTON[@id='wsf-1-field-27']")
        self.btn_datos = (By.XPATH, "//A[@class='et_pb_button et_pb_button_1 et_pb_bg_layout_light'][text()='Datos Personales']")
        self.msj_exito = (By.XPATH, "//p[contains(.,'Gracias por tu encuesta.')]")

    def btn_datos_personales(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.driver.find_element(*self.btn_datos))
        self.driver.find_element(*self.btn_datos).click()

    def llenarDatos(self, nombre, apellido, correo, telefono, direccion):
        # Con esta forma le dejamos la responsabilidad de buscar el elemento al metodo, y arriba solo se le digo
        # como lo tiene que buscar, en este caso por medio del XPATH, es solo una referencia porque es muy probable que
        # cuando vaya a buscar el elemento en la parte del __init__ este aun no exista
        self.driver.find_element(*self.input_nombre).send_keys(nombre)
        time.sleep(2)
        self.driver.find_element(*self.input_apellido).send_keys(apellido)
        self.driver.find_element(*self.input_correo).send_keys(correo)
        self.driver.find_element(*self.input_telefono).send_keys(telefono)
        self.driver.find_element(*self.input_direccion).send_keys(direccion)

    def clickEnviarDatos(self, mensaje):
        # Instanciamos un objeto de la case TestCase para utilizar los assert
        tcAssert = unittest.TestCase('__init__')
        self.driver.find_element(*self.btn_enviar).click()
        time.sleep(2)
        msj = self.driver.find_element(*self.msj_exito).text
        tcAssert.assertEqual(msj, mensaje)

