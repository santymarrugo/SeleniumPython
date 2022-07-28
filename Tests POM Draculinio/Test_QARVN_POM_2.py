from selenium import webdriver

from Pages.PageDatosPersonales import *
from Pages.PageIndex import *
from selenium.webdriver.chrome.service import Service


class DatosPersonales(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("../chromedriver.exe"))
        #self.driver = webdriver.Firefox(executable_path="../geckodriver.exe")
        self.driver.get("https://testingqarvn.com.es/")
        self.driver.maximize_window()

        # Instanciamos el objeto de la clase PageIndex
        self.page_index = PageIndex(self.driver)
        # Instanciamos el objeto de la clase PageDatosPeronsales
        self.page_datos_personales = PageDatosPersonales(self.driver)

    def test_llenarDatos(self):
        self.page_index.accesoMenuPracticasQA()
        self.page_datos_personales.btn_datos_personales()
        self.page_datos_personales.llenarDatos("Samuel Jose", "Perez Cantillo", "sam@gmail.com", "3003434124", "Castillogrande Av 4ta")
        self.page_datos_personales.clickEnviarDatos("Gracias por tu encuesta.")

    def tearDown(self):
        self.driver.quit()
