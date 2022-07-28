import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from PagesGestion.PageLogin import PageLogin


class LoginGestion(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options, service=Service("../chromedriver.exe"))
        self.driver.get("https://gestiontesting.memory.com.uy")
        self.driver.maximize_window()

        self.page_login = PageLogin(self.driver)

    def test_LoginExitoso(self):
        self.page_login.Login("tester0001@memory.com.uy", "Test1ng147852369")
        self.page_login.clickBtnIngresar()
        self.page_login.seleccionEmpresa("3216")
        self.page_login.seleccionSucursal("6499")
        self.page_login.seleccionPuntoEmision("3248")
        self.page_login.clickIngresarEmpresa()
        self.page_login.verificarLoginExitoso("Panel de control")

    def test_LoginFallidoUserErrado(self):
        self.page_login.Login("santy@yopmail.com", "Test1ng147852369")
        self.page_login.clickBtnIngresar()
        self.page_login.verificarLoginFallido("Usuario o contraseña incorrecto.")

    def test_LoginFallidoPassErrado(self):
        self.page_login.Login("tester0001@memory.com.uy", "loquesea12345")
        self.page_login.clickBtnIngresar()
        self.page_login.verificarLoginFallido("Usuario o contraseña incorrecto.")

    def test_LoginFallidoUserVacio(self):
        self.page_login.Login("", "Test1ng147852369")
        self.page_login.clickBtnIngresar()
        self.page_login.verificarLoginFallido("Usuario o contraseña incorrecto.")

    def test_LoginFallidoPassVacio(self):
        self.page_login.Login("tester0001@memory.com.uy", "")
        self.page_login.clickBtnIngresar()
        self.page_login.verificarLoginFallido("Usuario o contraseña incorrecto.")

    def tearDown(self):
        self.driver.quit()
