import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PageAsientos:

    def __init__(self, driver):
        # self.lineaNueva = None
        self.driver = driver

        self.btnMenuPrincipal = (By.XPATH, "//span[contains(@id,'iconMenu_topToggle')]")
        self.opCarpetas = (By.XPATH, "//a[contains(@id,'v-pills-carpetas-tab')]")
        self.opAsiento = (By.XPATH, "(//a[@class='nav-link menuTopToggleSubOption menuTopToggleText'][contains(.,'Asientos')])[3]")
        self.labelAsientoModal = (By.XPATH, "//LABEL[@id='exampleModalLongTitleAsientos']")
        self.rbCrearMes = (By.XPATH, "//input[contains(@id,'inputAsiento1')]")
        self.inputMesAnio = (By.XPATH, "//input[contains(@id,'FechaNuevoAsiento')]")
        self.btnAceptarAsientos = (By.XPATH, "//button[contains(@class,'btn btn-danger popupBotonAceptar btnCargarAsientos')]")
        self.rbEditarMesAsiento = (By.XPATH, "//input[contains(@id,'inputAsiento2')]")
        self.rbPrimerMes = (By.XPATH, "//input[contains(@value,'1/2022')]")
        self.lblVerificarMesAsiento = (By.XPATH, "//LABEL[@id='inicio']")
        self.btnNuevaLinea = (By.XPATH, "//i[@class='material-icons'][contains(.,'note_add')]")


    '''
    Metodo para acceder a la opcion Asientos y que se muestre el PopUp para escoger la fecha del asiento
    '''
    def accederAsientos(self):
        self.driver.find_element(*self.btnMenuPrincipal).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.opCarpetas))
        self.driver.find_element(*self.opCarpetas).click()
        self.driver.find_element(*self.opAsiento).click()

    '''
    Metodo para verificar que texto al momento de hacer click en la opcion asientos, y asegurar que se haya ingresado
    exitosamente a esa opcion.
    '''
    # Metodo para verificar que se esté mostrando el modal para elegir el mes del asiento
    def verificarTituloVentanaModalAsiento(self, txtmensajeModal):
        tcAssert = unittest.TestCase("__init__")
        txtAModal = self.driver.find_element(*self.labelAsientoModal).text
        tcAssert.assertEqual(txtAModal, txtmensajeModal)

    # Metodo para seleccionar el primer mes de la lista de asientos y entrar a editarlo
    def editarMesAsiento(self):
        self.driver.find_element(*self.rbEditarMesAsiento).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.rbPrimerMes))
        self.driver.find_element(*self.rbPrimerMes).click()

    # Metodo para hacer click en el boton Aceptar del Modal de Asientos
    def clickBtnAceptarAsientos(self):
        self.driver.find_element(*self.btnAceptarAsientos).click()

    # Metodo para verificar el texto de la parte superior izquierda y que nos indica en que parte de la plataforma estamos
    def verificarTituloVentana(self, mensaje):
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element(self.lblVerificarMesAsiento, mensaje))
        tcAssert = unittest.TestCase("__init__")
        lblMesAsiento = self.driver.find_element(*self.lblVerificarMesAsiento).text
        tcAssert.assertEqual(lblMesAsiento, mensaje)

    # Metodo para hacer click en el boton que agrega una nueva línea en el asiento
    def clickAgregarLineaAsiento(self):
        self.driver.find_element(*self.btnNuevaLinea).click()

    # Metodo que nos permite escribir texto en la línea del asiento después de haber agregado una línea nueva
    def escribirLineaAsiento(self):
        self.driver.execute_script('hot.selectCell(0,5)')
        self.driver.execute_script('hot.setDataAtCell(0,5,"12")')
        
        # self.driver.execute_script('hot.setDataAtCell(0,6,"11111")')
        # self.driver.execute_script('hot.setDataAtCell(0,7,"41113")')
        # self.driver.execute_script('hot.setDataAtCell(0,9,"1")')
        # self.driver.execute_script('hot.setDataAtCell(0,10,"Prueba Selenium con Python")')
        # self.driver.execute_script('hot.setDataAtCell(0,11,"1")')
        # self.driver.execute_script('hot.setDataAtCell(0,12,"12500")')
        # self.driver.execute_script('hot.setDataAtCell(0,19,"I")')
        # PageAsientos(self.driver).clickAgregarLineaAsiento()
        # self.driver.execute_script('hot.selectCell(1,5)')
        # self.driver.execute_script('hot.setDataAtCell(1,5,"12")')
        # self.driver.execute_script('hot.setDataAtCell(1,6,"11111")')
        # self.driver.execute_script('hot.setDataAtCell(1,7,"41113")')
        # self.driver.execute_script('hot.setDataAtCell(1,9,"1")')
        # self.driver.execute_script('hot.setDataAtCell(1,10,"Prueba Selenium con Python_linea2")')
        # self.driver.execute_script('hot.setDataAtCell(1,11,"1")')
        # self.driver.execute_script('hot.setDataAtCell(1,12,"50000")')
        # self.driver.execute_script('hot.setDataAtCell(1,19,"I")')

    # Metodo para hacer click en el radiobutton para crear un mes nuevo de asientos
    def clickCrearMes(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.rbPrimerMes))
        self.driver.find_element(*self.rbCrearMes).click()

    # Metodo para escribir el mes nuevo a crear
    def escribirMesAnioAsiento(self, fecha):
        self.driver.find_element(*self.inputMesAnio).click()
        self.driver.find_element(*self.inputMesAnio).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.inputMesAnio).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.inputMesAnio).send_keys(fecha)




