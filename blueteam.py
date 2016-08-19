#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
usageInMin = {'startAt':int(time.time())}

driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")

driver.get("http://goo.gl/545wov")
time.sleep(30)
mobile = driver.find_element_by_name("mobile")
mobile.send_keys(8750937767)
password = driver.find_element_by_name("password")
password.send_keys("redhat@11111p")
driver.find_element_by_name("submit").click()
#driver.find_element_by_link_text("MAID")
#driver.find_element_by_name("MAID").click()
#driver.close(1000)
time.sleep(90)

driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()
time.sleep(5)


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
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()


driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu > ion-content > div.scroll > ion-list > div > ion-item:nth-child(14)").click()
time.sleep(10)
driver.back()
time.sleep(10)
driver.find_element_by_css_selector("body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-bar > div:nth-child(4) > ion-header-bar > div.buttons.buttons-left.header-item > span > button").click()

driver.close()
    









    








