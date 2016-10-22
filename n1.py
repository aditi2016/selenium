from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.babajob.com/")

time.sleep(5)
driver.find_element_by_css_selector("#findJobs").click()
time.sleep(5)

name = driver.find_element_by_css_selector("#jobseekerName")
name.send_keys("aditi")
mobile = driver.find_element_by_css_selector("#jobseekerMobileOrEmail")
mobile.send_keys("9871768388")
job = driver.find_element_by_css_selector("#field-desiredcategory")
job.send_keys("sales")
time.sleep(2)

password = driver.find_element_by_css_selector("#jobseekerPassword")
password.send_keys("killbill12345")
driver.find_element_by_css_selector("#jobSeekerRegister").click()

  




  


    
driver.close()

