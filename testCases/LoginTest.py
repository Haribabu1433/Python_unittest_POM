import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("C:\\Users\\hpolicha\\PycharmProjects\\Python_unittest_POM")
from pageObjets.LoginPage import LoginPage
import time

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/admin/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
    def test_logn(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"webpage titles does not match")
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))