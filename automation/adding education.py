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

#navigating to Education tab
driver.find_element_by_xpath("//*[text()='Education']").click()

#opening new Education window
driver.find_element_by_xpath("//*[text()='Add Education']").click()

#adding Institute name
driver.find_element_by_xpath("//input[@placeholder='Enter Certificate Name']").send_keys("mic")
time.sleep(5)
driver.find_element_by_id("react-autowhatever-1--item-14").click()

#adding degree/course
driver.find_element_by_name("institute").send_keys("iit")
driver.find_element_by_xpath("//span[text()='IITT Institutions, Chandigarh']")

#adding from date
driver.find_element_by_xpath("//input[@type='number']").click()
driver.find_element_by_xpath("//button[text()='‹']").click()
driver.find_element_by_xpath("//button[@class='react-calendar__tile react-calendar__month-view__days__day'][7]").click()

#adding 'never expires' button
driver.find_element_by_id("certificate").click()

#saving Education detail
driver.find_element_by_xpath("//button[text()='Save']").click()

#closing window
driver.close()