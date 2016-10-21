#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from smtplib import SMTPException

#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url
try:
    driver.get("http://goo.gl/545wov")
	#wait for 30second while page loading
    time.sleep(40)
	#find element by name
    mobile = driver.find_element_by_name("mobile")
#then send key or can say password where moblile in css
    mobile.send_keys(8750937767)
#send password at place of password
    password = driver.find_element_by_name("password")
    password.send_keys("redhat@11111p")
    driver.find_element_by_name("submit").click()
    print("login done")

#driver.find_element_by_link_text("MAID")
#driver.find_element_by_name("MAID").click()
#driver.close(1000)
    time.sleep(90)
# to click on home
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
    time.sleep(10) 
    print("home click")
# to click on slect serevices

    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(3) > a").click()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    print("slect serevices")
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()

    print("home1")
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(6) > a").click()
    
    print("check verified")
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


    print("home2")
    time.sleep(5)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(7) > a").click()
    print("check calc")
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
     
    print("home3")
    time.sleep(5)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(9) > a").click()
    time.sleep(5)
    print("check contact")
    time.sleep(10)
    driver.back()
    driver.back()
    time.sleep(10)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
     
    print("home4")
    time.sleep(5)

    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(12) > a").click()
    time.sleep(10)
    print("check about")
    driver.back()
    time.sleep(10)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()

     
    
     
    print("home6")
    time.sleep(5)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(11) > a").click()
    print("check f&Q")
    time.sleep(10)
    driver.back()
    time.sleep(10)

    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()

     
    print("home7")
    time.sleep(5)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(13) > a").click()
    print("check T&C")
    time.sleep(10)
    driver.back()
    time.sleep(10)

#to book maid
    driver.find_element_by_xpath("//img[contains(@src,'maid.jpeg')]").click()
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-tabs > ion-nav-view:nth-child(4) > ion-view > ion-content > div.scroll > ion-list > div > ion-item:nth-child(1) > a").click()
    
    print("maid book")
    time.sleep(10)
    driver.back()
    driver.back()
    time.sleep(10)
#to logout
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
    time.sleep(5)
    driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(14)").click()

    driver.close()



except:
	sender = 'aditilahoria@gmail.com'
	receivers = ['aditilahoria@gmail.com']

	message = """From: From Person <den.callanan@gmail.com>
	To: To Person <callanden@gmail.com>
	Subject: SMTP e-mail test

	code error code error.
	"""

	try:
	    print("trying host and port...")

	    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    smtpObj.login("aditilahoria@gmail.com", "killbill12345")

	    print("sending mail...")

	    smtpObj.sendmail(sender, receivers, message)

	    print("Succesfully sent email")

	except smtplib.SMTPException:
	    print("Error: unable to send email")
	    import traceback
	    traceback.print_exc()







    








