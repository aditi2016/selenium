from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.indeed.co.in/cook-jobs-in-Gurgaon,-Haryana")

time.sleep(5)
driver.find_element_by_css_selector("#userOptionsLabel").click()
time.sleep(5)

driver.find_element_by_css_selector("#container > div > div > div > a.linkItem.linkItem-chevron.registrationLink > div").click()
time.sleep(5)
register_email = driver.find_element_by_css_selector("#register_email")
register_email.send_keys("aditilahoria@gmail.com")
register_retype_email = driver.find_element_by_css_selector("#register_retype_email")
register_retype_email.send_keys("aditilahoria@gmail.com")
time.sleep(2)

password = driver.find_element_by_css_selector("#register_password")
password.send_keys("killbill12345")
driver.find_element_by_css_selector("#loginform > div.form-group > button").click()

  




  


    
driver.close()