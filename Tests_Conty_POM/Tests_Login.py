from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from PagesConty.PageLogin import *
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class LoginConty(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options, service=Service("../chromedriver.exe"))
        self.driver.get("https://memorycontywebtesting.azurewebsites.net")
        self.driver.maximize_window()

        self.page_Login = PageLogin(self.driver)

    def test_LoginExitoso(self):
        self.page_Login.userycontrasena("tester0003@memory.com.uy", "Test1ng147852369")
        self.page_Login.clickIngresar()
        self.page_Login.seleccionarEmpresa("8585")
        self.page_Login.seleccionarSucursal("17266")
        self.page_Login.seleccionarPuntoEmision("9503")
        self.page_Login.clickIngresoEmpresa()
        self.page_Login.inicioExitoso("Inicio")

    def test_LoginFallidoPassErrado(self):
        self.page_Login.userycontrasena("tester0003@memory.com.uy", "134345454545")
        self.page_Login.clickIngresar()
        self.page_Login.inicioFallido("Usuario o contraseña incorrecto.")

    def test_LoginFallidoUserErrado(self):
        self.page_Login.userycontrasena("santymarrugo@yopmail.com", "Test1ng147852369")
        self.page_Login.clickIngresar()
        self.page_Login.inicioFallido("Usuario o contraseña incorrecto.")

    def test_LoginUserVacio(self):
        self.page_Login.userycontrasena("", "Test1ng147852369")
        self.page_Login.clickIngresar()
        self.page_Login.inicioFallido("Usuario o contraseña incorrecto.")

    def test_LoginPassVacio(self):
        self.page_Login.userycontrasena("tester0003@memory.com.uy", "")
        self.page_Login.clickIngresar()
        self.page_Login.inicioFallido("Usuario o contraseña incorrecto.")

    def tearDown(self):
        self.driver.quit()
