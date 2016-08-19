from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/collap/Downloads/chromedriver.exe")

driver.get("http://goo.gl/545wov")
time.sleep(20)
mobile = driver.find_element_by_name("mobile")
mobile.send_keys(8750937767)
password = driver.find_element_by_name("password")
password.send_keys("redhat@11111p")
driver.find_element_by_name("submit").click()
#driver.find_element_by_link_text("MAID")
#driver.find_element_by_name("MAID").click()
#driver.close(1000)
time.sleep(50)

#driver.find_element_by_xpath('//a[img/@src="http://blueteam.in/static/images/maid.jpeg"]').click()
driver.find_element_by_xpath("//img[contains(@src,'maid.jpeg')]").click()
time.sleep(20)
driver.get("http://blueteam.in/web-app/#/tab/service/maid/type/On-Demand")


#first get all the <a> elements
#List<WebElement> linkList=driver.findElements(By.tagName("a"));

#//now traverse over the list and check
#for(int i=0 ; i<linkList.size() ; i++)
#{
 #   if(linkList.get(i).getAttribute("href").contains("long"))
  #  {
  #      linkList.get(i).click();
 
 #       break;
  #  }
#}



    





