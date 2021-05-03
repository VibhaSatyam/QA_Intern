from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()

#Task-1
driver.get("https://stage-www.keyflow.com/en/profile/login")
driver.find_element_by_name("phone").send_keys("+46761177777")
driver.find_element_by_name("password").send_keys("testerQA123")
driver.find_element_by_xpath("//button/span[contains(text(),'Login')]").click()
time.sleep(1)

#Task-2
driver.get("https://stage-www.keyflow.com/en/profile/me")

#Task3

age=driver.find_element_by_xpath("//h1[contains(@class,'userName')]").text
print(age[-2:])