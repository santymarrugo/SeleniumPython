from selenium import webdriver
from Pages.PageIndex import *
from Pages.PageSolicitarProducto import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


# Aqui la clase QARVN está heredando de la clase TestCase que está en el Package de unittest
class QARVN(unittest.TestCase):
    # Metodo setUp, aqui podemos levantar el browser, ir a algun sitio en particular , cosas que se van a repetir en
    # todos nuestros casos
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service("../geckodriver.exe"))
        self.driver.get("https://testingqarvn.com.es/")
        self.driver.maximize_window()
        # Instanciamos un Objeto de la Clase PageIndex, para tener acceso a sus metodos
        self.page_index = PageIndex(self.driver)
        # Instanciamos un Objeto de la Clase PageIndex, para tener acceso a sus metodos
        self.page_producto = PageSolicitarProducto(self.driver)

    def test_EnviarFormulario(self):
        self.page_index.accesoMenuPracticasQA()
        self.page_index.accesoBotonComboBox()
        self.page_index.datosPersonales("Santiago jose", "Marrugo Monsalve", "santi@gmail.com", "3003030303",
                                        "La carolina mz f lote 36")
        self.page_index.elegirLenguajeChkBox()
        self.page_index.elegirLenguajeRdButton()
        self.page_index.seleccionarSO("Mac")
        self.page_index.enviarDatos()
        self.page_index.verificarEnvioDatos("Gracias por tu encuesta.")

    def test_pedirProducto(self):
        self.page_index.accesoMenuPracticasQA()
        self.page_producto.accesoBotonProductos()
        self.page_producto.formularioProductos("Juan Jose", "Palacios Chamorro", "juanpixx@gmail.com", "3000303000",
                                               "El libertador", "Donde rosa", "Cartagena", "GA", "30313")
        self.page_producto.enviarDatos("Thank you for placing your order.")

    # Nos indica que hacer una vez termine cada caso de prueba, esto sucedera en todos los casos existentes
    def tearDown(self):
        self.driver.quit()
