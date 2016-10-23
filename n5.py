from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url

driver.get("http://www.homeadvisor.com/")

time.sleep(5)



driver.find_element_by_css_selector("#truncated-header > div > ul > li.ha-links.mobile-hidden.header-nav-item.has-sub-menu.my-account").click()
driver.find_element_by_css_selector("#truncated-header > div > ul > li.ha-links.mobile-hidden.header-nav-item.has-sub-menu.my-account > div > ul > li:nth-child(1) > a").click()

time.sleep(2)

email = driver.find_element_by_css_selector("#email")
email.send_keys("killbill12345@gmail.com")
time.sleep(2)
password = driver.find_element_by_css_selector("#password")
password.send_keys("gurgaon")
time.sleep(2)
retypePassword = driver.find_element_by_css_selector("#retypePassword")
retypePassword.send_keys("gurgaon")
firstName = driver.find_element_by_css_selector("#firstName")
firstName.send_keys("hitan")
lastName = driver.find_element_by_css_selector("#lastName")
lastName.send_keys("maid ji")
zipp = driver.find_element_by_css_selector("#zip")
zipp.send_keys("110052")
driver.find_element_by_css_selector("#marketingOptIn").click()
time.sleep(5)
driver.find_element_by_css_selector("#signupFormVO > div:nth-child(10) > div.col2 > input").click()


  




  


    
driver.close()