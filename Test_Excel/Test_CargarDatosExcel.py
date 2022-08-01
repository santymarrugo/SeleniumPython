import time
import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from ImportarDesdeExcel.PageExcel import CargarExcel
from ImportarDesdeExcel.Funciones_Excel import AbrirExcel


class CargueExcel(unittest.TestCase):

    def setUp(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(firefox_profile, service=Service("../geckodriver.exe"))
        self.driver.get("https://testingqarvn.com.es/datos-personales/")
        self.driver.maximize_window()
        self.cargarDatosExcel = CargarExcel(self.driver)
        self.funcionesExcel = AbrirExcel(self.driver)

    def test_llenarFormulario(self):
        # Guardamos en una variable la ruta donde se encuentra el excel con los datos
        ruta = "C://Users//marr801550//PycharmProjects//Curso_selenium//ImportarDesdeExcel//Datos_Excel.xlsx"
        # En una variable guardamos el número de filas que tiene el Excel, mediante el metodo getRowCount()
        filas = self.funcionesExcel.obtenerNumeroFilas(ruta, "Hoja1")
        # Recorremos con un for todas las filas que tenga el Excel y por medio del metodo readData leemos los datos
        # y los guardamos en una variable, para eso la pasamos la ruta, el nombre de la hoja, fila y columna
        for row in range(2, filas + 1):
            nombre = self.funcionesExcel.leerDatosDeExcel(ruta, "Hoja1", row, 1)
            apellido = self.funcionesExcel.leerDatosDeExcel(ruta, "Hoja1", row, 2)
            email = self.funcionesExcel.leerDatosDeExcel(ruta, "Hoja1", row, 3)
            telefono = self.funcionesExcel.leerDatosDeExcel(ruta, "Hoja1", row, 4)
            direccion = self.funcionesExcel.leerDatosDeExcel(ruta, "Hoja1", row, 5)
            # Mediante el metodo llenarFormulario, le pasamos a los parámetros del metodo, los valores anteriormente
            # Guardados
            self.cargarDatosExcel.llenarFormulario(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion)
            self.cargarDatosExcel.clickEnviarFormulario()
            time.sleep(5)
            self.funcionesExcel.esribirDatosEnExcel(ruta, "Hoja1", row, 6, "INSERTADO")

    def test_crearLibroExcel(self):
        ruta = "C://Users//marr801550//PycharmProjects//Curso_selenium//ImportarDesdeExcel"
        self.funcionesExcel.crearNuevaLibro(ruta, "LibroPrueba.xlsx")

    def tearDown(self):
        pass
