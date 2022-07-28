import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageAsientos:

    def __init__(self, driver):
        self.driver = driver

        self.btnMenuPrincipal = (By.XPATH, "//span[contains(@id,'iconMenu_topToggle')]")
        self.opCarpetas = (By.XPATH, "//a[contains(@id,'v-pills-carpetas-tab')]")
        self.opAsiento = (By.XPATH, "(//a[@class='nav-link menuTopToggleSubOption menuTopToggleText'][contains(.,'Asientos')])[3]")
        self.labelAsientoSeleccion = (By.XPATH, "//label[contains(@id,'inicio')]")
        self.labelAsientoModal = (By.XPATH, "//label[@class='modal-title'][contains(.,'Asientos')]")
        self.rbCrearMes = (By.XPATH, "//input[contains(@id,'inputAsiento1')]")
        self.inputMesAnio = (By.XPATH, "//input[contains(@id,'FechaNuevoAsiento')]")
        self.btnAceptarAsientos = (By.XPATH, "//button[contains(@class,'btn btn-danger popupBotonAceptar btnCargarAsientos')]")

    '''
    Metodo para acceder a la opcion Asientos y que se muestre el PopUp para escoger la fecha del asiento
    '''
    def accederAsientos(self):
        self.driver.find_element(*self.btnMenuPrincipal).click()
        time.sleep(1)
        self.driver.find_element(*self.opCarpetas).click()
        self.driver.find_element(*self.opAsiento).click()

    '''
    Metodo para verificar que texto al momento de hacer click en la opcion asientos, y asegurar que se haya ingresado
    exitosamente a esa opcion.
    '''
    def ventanaAsiento(self, txtmensaje, txtmensajeModal):
        tcAssert = unittest.TestCase("__init__")
        txtSeleccion = self.driver.find_element(*self.labelAsientoSeleccion).text
        txtAModal = self.driver.find_element(*self.labelAsientoModal).text
        tcAssert.assertEqual(txtSeleccion, txtmensaje)
        tcAssert.assertEquals(txtAModal, txtmensajeModal)
        print(txtSeleccion)
        print(txtAModal)
