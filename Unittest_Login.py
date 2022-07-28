import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

tiempo = 0.5


class base_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def test_LoginExitoso(self):
        user = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        user.send_keys("standard_user")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        btn_login.click()
        # Validamos que hayamos entrado exitosamente
        label_products = self.driver.find_element(By.XPATH, "//span[@class='title'][contains(.,'Products')]")
        self.assertEqual(label_products.text, "PRODUCTS")
        print(label_products.text)
        time.sleep(tiempo)

    def test_LoginUserLocked(self):
        user = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        user.send_keys("locked_out_user")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        btn_login.click()
        # Validamos que el usuario este bloqueado
        label_user_locked = self.driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        self.assertEqual(label_user_locked.text, "Epic sadface: Sorry, this user has been locked out.")
        print(label_user_locked.text)
        time.sleep(tiempo)

    def test_LoginUserWhithProblem(self):
        user = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        user.send_keys("problem_user")
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        btn_login.click()
        # Validamos la imagen de los productos
        img_products = self.driver.find_element(By.XPATH, "(//img[@src='/static/media/sl-404.168b1cce.jpg'])[2]")
        print(img_products.is_displayed())
        self.assertEqual(img_products.is_displayed(), True)
        time.sleep(tiempo)

    def test_UserEmpty(self):
        password = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        password.send_keys("secret_sauce")
        btn_login = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        btn_login.click()
        msg_user_empty = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual(msg_user_empty.text, "Epic sadface: Username is required")
        print(msg_user_empty.text)
        time.sleep(tiempo)

    def test_PasswordEmpty(self):
        user = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        user.send_keys("problem_user")
        btn_login = self.driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        btn_login.click()
        msg_password_empty = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual(msg_password_empty.text, "Epic sadface: Password is required")
        print(msg_password_empty.text)
        time.sleep(tiempo)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
