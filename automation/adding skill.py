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

#opening new skill window
driver.find_element_by_xpath("//*[text()=' Add Skill']").click()

#adding skill name
driver.find_element_by_name("name").send_keys("selen")
time.sleep(5)
listElement = driver.find_elements_by_xpath("//li[@role='option']")
print("items are ",len(listElement))
time.sleep(5)
for ele in listElement:
    #print(ele.get_attribute())
    print(ele.text)
    if ele.text == 'Selenium':
        ele.click()
        break

#adding skill type
driver.find_element_by_xpath("//span[text()='primary']").click()

#adding skill proficiency
driver.find_element_by_xpath("//span[text()='foundation']").click()

#adding last used period
driver.find_element_by_id("last_used_year").click()
driver.find_element_by_xpath("//option[@value='currentlyUsing']").click()

#adding exp in years
driver.find_element_by_id("experience_in_years").click()
driver.find_element_by_xpath("//select[@id='experience_in_years']//option[@value='1']").click()

#adding exp in months
driver.find_element_by_id("experience_in_months").click()
driver.find_element_by_xpath("//select[@id='experience_in_months']//option[@value='6']").click()

#saving skill
driver.find_element_by_xpath("//button[text()='Save']").click()


driver.close()


