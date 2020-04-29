class HomePage():

	def __init__(self, driver):
		self.driver = driver

	def click_sign_in(self):
		self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()

	def click_log_out(self):
		self.driver.find_element_by_xpath("//*[@id='header']/div[2]/div/div/nav/div[2]/a").click()