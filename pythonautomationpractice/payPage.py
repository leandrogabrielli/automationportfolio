import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re
import time

class PayPage(unittest.TestCase):

	def __init__(self, driver):
		self.driver = driver

	def pay_by_bank(self):
		driver = self.driver
		pay_by_bank_button = driver.find_element_by_xpath("//*[@id='HOOK_PAYMENT']/div[1]/div/p/a")
		pay_by_bank_button.click()
		confirm_order_button = driver.find_element_by_xpath("//*[@id='cart_navigation']/button")
		confirm_order_button.click()
		src = driver.page_source
		text_complete = re.search(r'Your order on My Store is complete', src)
		self.assertNotEqual(text_complete, None)
		time.sleep(3)