from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.homehelp4india.com/")

time.sleep(5)



txtname = driver.find_element_by_css_selector("#txtname")
txtname.send_keys("aditilahoria")
txtmobile = driver.find_element_by_css_selector("#txtmobile")
txtmobile.send_keys("8750937767")
time.sleep(2)

txtEmailId = driver.find_element_by_css_selector("#txtEmailId")
txtEmailId.send_keys("killbill12345@gmail.com")
time.sleep(2)
txtCity = driver.find_element_by_css_selector("#txtCity")
txtCity.send_keys("gurgaon")
time.sleep(2)
ddlservice = driver.find_element_by_css_selector("#ddlservice")
ddlservice.send_keys("h")
txtMessage = driver.find_element_by_css_selector("#txtMessage")
txtMessage.send_keys("maid ji")
driver.find_element_by_css_selector("#CheckBox1").click()
time.sleep(5)
driver.find_element_by_css_selector("#btnsend").click()


  




  


    
driver.close()