import unittest
import configparser
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from loginPage import LoginPage 
from homePage import HomePage
from checkoutPage import CheckoutPage
from payPage import PayPage
from selenium.webdriver import ActionChains
import HtmlTestRunner
import re
import time

class automationpractice(unittest.TestCase):

	def setUp(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		config.sections()
		getbrowser = config['General']['chrome']
		self.page = config['Pages']['page']
		self.driver = webdriver.Chrome(executable_path=getbrowser)
		self.user = config['Users']['user']
		self.password = config['Passwords']['password']

	def test_automation(self):
		driver = self.driver
		driver.maximize_window()
		driver.get(self.page)
		homepage = HomePage(driver)
		homepage.click_sign_in()
		time.sleep(3)
		login = LoginPage(driver)
		login.enter_username(self.user)
		login.enter_password(self.password)
		login.click_login()
		time.sleep(3) 
		home = driver.find_element_by_xpath("//*[@id='header_logo']/a/img")
		home.click()
		homepage.buy_cheapest()
		checkout = CheckoutPage(driver)
		checkout.perform_checkout()
		payment = PayPage(driver)
		payment.pay_by_bank()


	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results of my test plan'))			