import configparser
config = configparser.ConfigParser()

# the following parameters will modify the config.ini file located within the same directory
config['General'] = {'chrome' : 'C:\chromedriver\chromedriver.exe'}
config['Pages'] = {'page' : 'http://automationpractice.com'}
config['Users'] = {'user' : 'leandrogabrielli91@gmail.com'}
config['Passwords'] = {'password' : 'abcde12345'}

with open('config.ini', 'w') as fileconfig: # w = write
	config.write(fileconfig)