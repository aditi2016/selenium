from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.myunnati.com/")

time.sleep(5)
driver.find_element_by_css_selector("#menu-item-70 > a").click()
time.sleep(5)

driver.find_element_by_css_selector("#pageC > div.bodyCont.cl > div.grid-13.omega.fr.hidden-phone > div.dropWrap.hlight > form > button").click()
time.sleep(30)



name = driver.find_element_by_css_selector("#name").click()
name.send_keys("aditi")
eml = driver.find_element_by_css_selector("#eml")
eml.send_keys("aditilahoria@gmail.com")
time.sleep(2)

mobNo = driver.find_element_by_css_selector("#mobNo")
mobNo.send_keys("9871768387")
Sug_city = driver.find_element_by_css_selector("#Sug_city")
Sug_city.send_keys("gurgaon")
cstmExpY = driver.find_element_by_css_selector("#cstmExpY").click()
driver.find_element_by_css_selector("#\23 99").click()
driver.find_element_by_css_selector("#agreechkbox").click()
driver.find_element_by_css_selector("#customSubmit").click()



  




  


    
driver.close()