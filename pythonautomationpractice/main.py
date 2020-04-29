import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginPage import LoginPage 
from homePage import HomePage
import time

class automationpractice(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

	def test_login(self):
		driver = self.driver
		driver.get("http://automationpractice.com")
		homepage = HomePage(driver)
		homepage.click_sign_in()
		time.sleep(2)
		login = LoginPage(driver)
		login.enter_username("leandrogabrielli91@gmail.com")
		login.enter_password("zxnm123")
		login.click_login()
		time.sleep(2)
		homepage.click_log_out()
		time.sleep(2)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
