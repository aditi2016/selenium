#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
usageInMin = {'startAt':int(time.time())}
#path of chrome driver
driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")
# go to that url
driver.get("http://goo.gl/545wov")
#wait for 30second while page loading
time.sleep(30)
#find element by name
mobile = driver.find_element_by_name("mobile")
#then send key or can say password where moblile in css
mobile.send_keys(8750937767)
#send password at place of password
password = driver.find_element_by_name("password")
password.send_keys("redhat@11111p")
driver.find_element_by_name("submit").click()
#driver.find_element_by_link_text("MAID")
#driver.find_element_by_name("MAID").click()
#driver.close(1000)
time.sleep(90)
# to click on home
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
time.sleep(5)
# to click on slect serevices

driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(3) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(6) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(7) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()

driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(9) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(12) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(5) > a").click()
time.sleep(10)
driver.back()
time.sleep(10)

#to book maid
driver.find_element_by_xpath("//img[contains(@src,'maid.jpeg')]").click()
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-tabs > ion-nav-view:nth-child(4) > ion-view > ion-content > div.scroll > ion-list > div > ion-item:nth-child(1) > a").click()
time.sleep(10)
driver.back()
driver.back()
time.sleep(10)
#to logout
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
time.sleep(5)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(14)").click()




















driver.close()
    









    








