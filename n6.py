from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.justdial.com/Delhi-NCR/Placement-Services-For-Maids-(For-Employers)-in-Gurgaon/ct-522331?utm_source=adwords&utm_medium=codered&gclid=CjwKEAjwkJfABRDnhbPlx6WI4ncSJADMQqxdrBj-P_aO0O8Ix-KdQgxOeqY4C6G_Yha4eLIuGudIlBoCcLjw_wcB")

time.sleep(5)



driver.find_element_by_css_selector("#navhver > ul > li.login > ul > li:nth-child(3) > a > span").click()
time.sleep(7)
mobile_srch = driver.find_element_by_css_selector("#mobile_srch")
mobile_srch.send_keys("8750937767")
driver.find_element_by_css_selector("#btnSubmit3").click()
time.sleep(2)


time.sleep(2)
password = driver.find_element_by_css_selector("#cp")
password.send_keys("gurgaon")
time.sleep(2)

firstName = driver.find_element_by_css_selector("#fn")
firstName.send_keys("hitan")
lastName = driver.find_element_by_css_selector("#ln")
lastName.send_keys("maid ji")
time.sleep(5)
driver.find_element_by_css_selector("#signup_user > p:nth-child(10) > button").click()


  




  


    
driver.close()