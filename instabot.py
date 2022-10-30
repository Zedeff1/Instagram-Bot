import selenium
from selenium import webdriver
from time import sleep 
#import mysql.connector as sq

path = 'C:/Program Files (x86)/chromedriver.exe'

# setting up sql
#conn = sql.connect(host = 'localhost', user = 'root', password = 'Shreya', database = 'instabot')
#cursor = conn.cursor()



class instabot:
	def __init__(self, username, password): 
		

		self.driver = webdriver.Chrome(path)
		self.username = username
		self.driver.get("https://instagram.com")
		self.driver.maximize_window()
		sleep(2)
		

		self.username_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
						.send_keys(username)			#enters username
		sleep(2)

		self.password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
						.send_keys(password)			#enters password
		sleep(2)				

		self.submit = self.driver.find_element_by_xpath("//button[@type='submit']")\
				 .click()								#clicks on sibmit/login`
		sleep(5)		 								

		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
			     .click()
		sleep(2) 					#1st "Not Now"

		self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
			     .click()
		sleep(2)					#2nd "Not Now", goes to profile

			 

name = 'ABC'
passw = 'Xyz' 

bot = instabot(name, passw) 

