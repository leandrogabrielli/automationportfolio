import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re
import time

class CheckoutPage(unittest.TestCase):

	def __init__(self, driver):
		self.driver = driver

	def perform_checkout(self):
		driver = self.driver
		src = driver.page_source
		text_succ_added = re.search(r'Product successfully added to your shopping cart', src)
		self.assertNotEqual(text_succ_added, None)		
		checkout1 = driver.find_element_by_xpath("//span[contains(text(),'Proceed to checkout')]")
		checkout1.click()
		time.sleep(2)
		checkout2 = driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']")
		checkout2.click()
		time.sleep(2)
		comment_textbox = driver.find_element_by_xpath("//*[@id='ordermsg']/textarea").send_keys("Thanks for going through this test")
		time.sleep(3)
		checkout3 = driver.find_element_by_xpath("//*[@id='center_column']/form/p/button")
		checkout3.click()
		time.sleep(2)
		checkbox_agree = driver.find_element_by_xpath("//*[@id='cgv']")
		checkbox_agree.click()
		checkout4 = driver.find_element_by_xpath("//*[@id='form']/p/button")
		checkout4.click()
		time.sleep(3)	