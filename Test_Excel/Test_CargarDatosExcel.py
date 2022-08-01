import time
import unittest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from ImportarDesdeExcel.PageExcel import CargarExcel
from selenium.webdriver.firefox.service import Service


class CargueExcel(unittest.TestCase):

    def setUp(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(firefox_profile, service=Service("../geckodriver.exe"))
        self.driver.get("https://testingqarvn.com.es/datos-personales/")
        self.driver.maximize_window()

        self.cargarDatosExcel = CargarExcel(self.driver)

    def test_llenarFormulario(self):
        self.cargarDatosExcel.llenarFormulario("Santiago", "Marrugo", "santi@yopmail.com", "3121212322", "Nazareno mz d lote 24")
        self.cargarDatosExcel.clickEnviarFormulario()
        time.sleep(5)

    def tearDown(self):
        pass
