from selenium import webdriver
import time

chromedriver="/home/shibashree/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://pathfinder-qa.edgenetworks.ai/auth/login")
driver.maximize_window()
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("shibashree.nanda@edgenetworks.in")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("EN1089")
driver.find_element_by_xpath("//*[text()='LOG IN']").click()
#driver.find_element_by_xpath("//span[@class='avatar avatar-sm rounded-circle']").click()

driver.find_element_by_xpath("//div[@class='align-items-center media']").click()
driver.find_element_by_xpath("//*[text()='Log Out']").click()
