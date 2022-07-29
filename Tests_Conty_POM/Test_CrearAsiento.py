import time
import unittest

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from PagesConty.PageLogin import PageLogin
from PagesConty.PageAsientos import PageAsientos


class CrearAsiento(unittest.TestCase):

    def setUp(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(firefox_profile, service=Service("../geckodriver.exe"))
        self.driver.get("https://memorycontywebtesting.azurewebsites.net")
        self.driver.maximize_window()

        self.page_login = PageLogin(self.driver)
        self.page_crear_asiento = PageAsientos(self.driver)

    def test_CrearAsiento(self):
        self.page_login.userycontrasena("tester0003@memory.com.uy", "Test1ng147852369")
        self.page_login.clickIngresar()
        self.page_login.seleccionarEmpresa("8585")
        self.page_login.seleccionarSucursal("17266")
        self.page_login.seleccionarPuntoEmision("9503")
        self.page_login.clickIngresoEmpresa()
        self.page_login.inicioExitoso("Inicio")
        self.page_crear_asiento.accederAsientos()
        self.page_crear_asiento.verificarTituloVentanaModalAsiento("Asientos")
        self.page_crear_asiento.clickCrearMes()
        self.page_crear_asiento.escribirMesAnioAsiento("12/2022")
        self.page_crear_asiento.clickBtnAceptarAsientos()
        self.page_crear_asiento.verificarTituloVentana("Asientos 12/2022")
        self.page_crear_asiento.escribirLineaAsiento()

    def tearDown(self):
        pass
        # self.driver.quit()
