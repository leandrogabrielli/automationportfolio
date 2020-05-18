import re
from selenium.webdriver import ActionChains
import time

class HomePage():

	def __init__(self, driver):
		self.driver = driver

	def click_sign_in(self):
		self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()

	def buy_cheapest(self):
		driver = self.driver
		prices = driver.find_elements_by_xpath("//*[@id='homefeatured']/li/div")
		price = driver.find_element_by_class_name("content_price")
		price_array = [int("".join(filter(str.isdigit, price.text))) for price in prices]
		cheapest = str(min(price_array))
		cheapest = re.sub(r'(?<!^)(?=(\d{2})+$)', r'.', cheapest) 
		cheapest = '$' + cheapest
		elemento = driver.find_element_by_xpath("//div[1]/span[contains(text(),'" + cheapest + "')]")
		hover = ActionChains(driver).move_to_element(elemento)
		hover.perform()
		add_to_cart = driver.find_element_by_xpath("//div[1]/span[contains(text(),'" + cheapest + "')]/../..//span[contains(text(),'Add to cart')]")
		time.sleep(2)
		add_to_cart.click()
		time.sleep(2)

	def click_log_out(self):
		self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]/a").click()


