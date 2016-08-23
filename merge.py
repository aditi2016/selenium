from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
driver.get("http://www.gmail.com")
time.sleep(10)
Email = driver.find_element_by_id("Email").click()
Email.send_Keys("aditilahoria@gmail.com")
driver.findElement_by_id("next").click()
time.sleep(10)
Passwd = driver.find_element_by.id("Passwd")
Passwd.sendKeys("killbill12345")
element.submit()
time.sleep(10)
driver.find_element_by_selector("#\3a ho > div > div").click()
time.sleep(5)
driver.find_element_by_name("to").click()
to.send_Keys("aditilahoria@gmail.com")
driver.find_element_by_name("Subjectbox").click()
Subjectbox.send_Keys("found error")
driver.findElement_by_id("lq").click()

    

