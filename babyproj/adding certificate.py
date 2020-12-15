from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

chromedriver="/home/shibashree/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://pathfinder-qa.edgenetworks.ai/auth/login")
driver.maximize_window()
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shibashree.nanda@edgenetworks.in")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("EN1089")
driver.find_element_by_xpath("//*[text()='LOG IN']").click()

time.sleep(2)

#navigating to Certificate tab
driver.find_element_by_xpath("//*[text()='Certifications']").click()

#opening new certificate window
driver.find_element_by_xpath("//*[text()='Add Certificate']").click()

#adding certificate name
driver.find_element_by_xpath("//input[@placeholder='Enter Certificate Name']").send_keys("mic")
time.sleep(5)
driver.find_element_by_id("react-autowhatever-1--item-14").click()

#adding issued by field
driver.find_element_by_name("issued_by").send_keys("Microsoft")

#adding from date
driver.find_element_by_xpath("//input[@type='number']").click()
driver.find_element_by_xpath("//button[text()='‹']").click()
driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day'][7]").click()

#adding 'never expires' button
driver.find_element_by_name("expires").click()

#saving certificate
driver.find_element_by_xpath("//button[text()='Save']").click()


driver.close()