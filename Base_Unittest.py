import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


# Se crea una clase del tipo Unittest, dentro de ella van todos los test
class base_test(unittest.TestCase):

    # Metodo que instancia el Driver del browser
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
        self.driver.maximize_window()

    # Metodo con un Test que abre una URL
    def test_1(self):
        self.driver.get("https://testingqarvn.com.es/")

    def test_2(self):
        self.driver.get("https://www.digitallearning.es/intro-programacion-js/alert.html")

    def test_3(self):
        self.driver.get("https://unipython.com/selenium-testing-test-suite-unittest/")

    # Metodo que cierra el o los tests
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
