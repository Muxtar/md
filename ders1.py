from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_experimental_option('debuggerAddress', 'localhost:8989')

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, executable_path="geckodriver", options = option)
driver.maximize_window()

option.add_experimental_option('debuggerAddress', 'localhost:8989')
path = "/home/mb/Desktop/geckodriver"

vars = {}

driver.get("https://www.e-gov.az/az/services/read/3766/0")
driver.switch_to.frame(0)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) > .col-md-4:nth-child(1) img").click()

driver.find_element(By.CSS_SELECTOR, ".col-md-5  .choice:nth-child(1)").click()

driver.find_element(By.CSS_SELECTOR, ".col-md-5 .choice:last-child").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-6 .choice:nth-child(2)").click()

driver.find_element(By.CSS_SELECTOR, ".col-md-4 > .form-control > option:nth-child(5)").click()

driver.find_element(By.NAME, "Captcha").click()
time.sleep(10)
# driver.find_element(By.ID, "next").click()
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(3)").click()

driver.find_element(By.NAME, "Captcha").click()
# driver.find_element(By.CSS_SELECTOR, ".btn-next").click()
# driver.find_element(By.CSS_SELECTOR, ".appartment-row:nth-child(9) > td:nth-child(4)").click()