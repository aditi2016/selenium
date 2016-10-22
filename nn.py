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
    driver.get("http://www.allindiayellowpage.com/UserModule/PublicSearchListforJobs.aspx?CategoryId=1463&sctid=37946&SearchTerm=Domestic%20Help%20Jobs&CityName=Gurgaon&ic=0")

    time.sleep(10)
    driver.find_element_by_css_selector("#frm1 > div:nth-child(5) > div:nth-child(1) > div:nth-child(4) > div > a").click()

    # mobile = driver.find_element_by_name("mobile")

    time.sleep(20)

    # password = driver.find_element_by_name("password")
    # password.send_keys("redhat@11111p")
    name = driver.find_element_by_css_selector("#txName").click()
  
    name.send_keys("aditi")


    time.sleep(10)
# to click on home
    txtEmail =  driver.find_element_by_css_selector("#txtEmail").click()
    txtEmail.send_keys("aditilahoria@gmail.com") 
    print("mailenter")
# to click on slect serevices

    txtstate = driver.find_element_by_css_selector("#txtstate").click()
    txtstate.send_keys("haryana") 
    print("stateenter")
  

    txtmob = driver.find_element_by_css_selector("#txtmob").click()
    txtmob.send_keys("8750937767")
    print("txtmob")
     
    txtadress = driver.find_element_by_css_selector("#txtadress").click()
    txtadress.send_keys("delhi")
    print("doneaddress")
    time.sleep(10)
 
    txtdescription = driver.find_element_by_css_selector("#txtdescription").click()
    txtmob.send_keys("done")

    print("txtdescription")

    
    driver.find_element_by_css_selector("#btnBook").click()
    print("done")
    
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
	    smtpObj.login("aditilahoria@gmail.com", "aditikill12345")

	    print("sending mail...")

	    smtpObj.sendmail(sender, receivers, message)

	    print("Succesfully sent email")

	except smtplib.SMTPException:
	    print("Error: unable to send email")
	    import traceback
	    traceback.print_exc()







    








