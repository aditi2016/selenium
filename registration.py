from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException
usageInMin = {'startAt':int(time.time())}
#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url
if true:(driver.get("http://goo.gl/545wov")
#wait for 30second while page loading
time.sleep(30)
#find element by name
mobile = driver.find_element_by_name("mobile")
#then send key or can say password where moblile in css
mobile.send_keys(9911033477)
#send password at place of password
password = driver.find_element_by_name("password")
password.send_keys("redhat@11111p")
time.sleep(10)
conf_password = driver.find_element_by_name("conf_password")
conf_password.send_keys("redhat@11111p")
name = driver.find_element_by_name("name")
name.send_keys("redhat@11111p")
email = driver.find_element_by_name("email")
email.send_keys("lahoria.singh.aditi@gmail.com")
driver.find_element_by_name("submit").click()
driver.close())

else: false
	print ('not working') 



