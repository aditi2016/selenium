from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
driver.get("http://www.gmail.com")
time.sleep(10)
element = driver.find_element_by_id('Email')
element.send_keys('aditilahoria')
driver.find_element_by_id("next").click()
time.sleep(5)
Passwd = driver.find_element_by_id('Passwd')
Passwd.send_keys("killbill12345")
time.sleep(5)
driver.find_element_by_id("signIn").click()

time.sleep(50)
driver.find_element_by_xpath("//*[@id=':ho']/div/div").click() 
time.sleep(15)
to = driver.find_element_by_name('to')
to.send_keys('aditi@blueteam.in')
time.sleep(5)
subjectbox = driver.find_element_by_name('subjectbox')
subjectbox.send_keys('found error')
time.sleep(3)
driver.find_element_by_class_name("T-I J-J5-Ji aoO T-I-atl L3").click()

    

