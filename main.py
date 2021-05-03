from selenium import webdriver
import chromedriver_autoinstaller
import time
import sys

chromedriver_autoinstaller.install()  # Checks if chromedriver exists or not. If doesn't then then downloads and adds to path 

driver = webdriver.Chrome()

# creates a output.txt file in the project folder and mode 'w' writes output.
sys.stdout = open("output.txt", "w")

#Task-1
driver.get("https://stage-www.keyflow.com/en/profile/login")
driver.find_element_by_name("phone").send_keys("+46761177777")
driver.find_element_by_name("password").send_keys("testerQA123")
driver.find_element_by_xpath("//button/span[contains(text(),'Login')]").click()

#used to add delay in the execution.
time.sleep(1)

#Task-2
driver.get("https://stage-www.keyflow.com/en/profile/me")

#Task3

age=driver.find_element_by_xpath("//h1[contains(@class,'userName')]").text
print(age[-2:])
sys.stdout.close()
driver.close()
