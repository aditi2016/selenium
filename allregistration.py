#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.allindiayellowpage.com/UserModule/PublicSearchListforJobs.aspx?CategoryId=1463&sctid=37946&SearchTerm=Domestic%20Help%20Jobs&CityName=Gurgaon&ic=0")

time.sleep(10)
driver.find_element_by_css_selector("#frm1 > div:nth-child(5) > div:nth-child(1) > div:nth-child(4) > div > a").click()
time.sleep(10)

txName = driver.find_element_by_name("txName")
  
txName.send_keys("aditilahoria")


time.sleep(10)
# to click on home
txtEmail =  driver.find_element_by_css_selector("#txtEmail")
txtEmail.send_keys("aditilahoria@gmail.com") 
print("mailenter")
# to click on slect serevices

txtstate = driver.find_element_by_css_selector("#txtstate")
txtstate.send_keys("haryana") 
print("stateenter")
  

txtmob = driver.find_element_by_css_selector("#txtmob")
txtmob.send_keys("8750937767")
print("txtmob")
     
txtadress = driver.find_element_by_css_selector("#txtadress")
txtadress.send_keys("delhi")
print("doneaddress")
time.sleep(10)
 
txtdescription = driver.find_element_by_css_selector("#txtdescription")
txtmob.send_keys("done")

print("txtdescription")

    
driver.find_element_by_css_selector("#btnBook").click()
print("done")
    
driver.close()

