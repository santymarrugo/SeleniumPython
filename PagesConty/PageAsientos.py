import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

t = 0.4


class PageAsientos:

    def __init__(self, driver):
        # self.lineaNueva = None
        self.driver = driver

        self.btnMenuPrincipal = (By.XPATH, "//span[contains(@id,'iconMenu_topToggle')]")
        self.opCarpetas = (By.XPATH, "//a[contains(@id,'v-pills-carpetas-tab')]")
        self.opAsiento = (
        By.XPATH, "(//a[@class='nav-link menuTopToggleSubOption menuTopToggleText'][contains(.,'Asientos')])[3]")
        self.labelAsientoModal = (By.XPATH, "//LABEL[@id='exampleModalLongTitleAsientos']")
        self.rbCrearMes = (By.XPATH, "//input[contains(@id,'inputAsiento1')]")
        self.inputMesAnio = (By.XPATH, "//input[contains(@id,'FechaNuevoAsiento')]")
        self.btnAceptarAsientos = (
        By.XPATH, "//button[contains(@class,'btn btn-danger popupBotonAceptar btnCargarAsientos')]")
        self.rbEditarMesAsiento = (By.XPATH, "//input[contains(@id,'inputAsiento2')]")
        self.rbPrimerMes = (By.XPATH, "//input[contains(@value,'1/2022')]")
        self.lblVerificarMesAsiento = (By.XPATH, "//LABEL[@id='inicio']")
        self.btnNuevaLinea = (By.XPATH, "//i[@class='material-icons'][contains(.,'note_add')]")
        self.btnTerminar = (By.XPATH, "//i[contains(text(),'check')]")
        self.rbMesDic = (By.XPATH, "//input[contains(@value,'12/2022')]")

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
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(self.lblVerificarMesAsiento, mensaje))
        tcAssert = unittest.TestCase("__init__")
        lblMesAsiento = self.driver.find_element(*self.lblVerificarMesAsiento).text
        tcAssert.assertEqual(lblMesAsiento, mensaje)

    # Metodo para hacer click en el boton que agrega una nueva línea en el asiento
    def clickAgregarLineaAsiento(self):
        self.driver.find_element(*self.btnNuevaLinea).click()

    # Metodo que nos permite escribir texto en la línea del asiento después de haber agregado una línea nueva
    def escribirLineaAsiento(self, fila, colDia, colDeb, colHab, colRut, colS, colConcep, colMone, colTot, colImp,
                                colCoti, colLib, colTipo,  dia, debe, haber, rut, s, concepto, moneda, total, impuesto,
                                IVA, libro, tipo):
        action = ActionChains(self.driver)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colDia + ',"' + dia + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colDeb + ',"' + debe + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colHab + ',"' + haber + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colS + ',"' + s + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell('+fila+', '+colConcep+', "'+concepto+'")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colMone + ',"' + moneda + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell(' + fila + ',' + colTot + ',"' + total + '")')
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(t)
        self.driver.execute_script('hot.setDataAtCell('+fila+','+colLib+',"'+libro+'")')

    # Metodo para eliminar lineas de asientos
    def eliminarLineasAsientos(self):
        pass
    
    # Metodo para hacer click en el radiobutton para crear un mes nuevo de asientos
    def clickCrearMes(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.rbPrimerMes))
        self.driver.find_element(*self.rbCrearMes).click()

    # Metodo para hacer click en el radiobutton para crear un mes nuevo de asientos
    def clickMesDiciembre(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.rbMesDic))
        self.driver.find_element(*self.rbMesDic).click()

    # Metodo para hacer click en el boton Terminar
    def clickBotonTerminar(self):
        self.driver.find_element(*self.btnTerminar).click()

    # Metodo para escribir el mes nuevo a crear
    def escribirMesAnioAsiento(self, fecha):
        self.driver.find_element(*self.inputMesAnio).click()
        self.driver.find_element(*self.inputMesAnio).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*self.inputMesAnio).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.inputMesAnio).send_keys(fecha)
