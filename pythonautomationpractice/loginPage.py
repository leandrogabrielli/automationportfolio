class LoginPage():

	def __init__(self, driver):
		self.driver = driver

	def enter_username(self, username):
		self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)

	def enter_password(self, password):
		self.driver.find_element_by_xpath("//*[@id='passwd']").send_keys(password)

	def click_login(self):
		self.driver.find_element_by_xpath("//*[@id='SubmitLogin']/span").click()