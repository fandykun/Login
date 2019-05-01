from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

NRP = ''
password = ''

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://integra.its.ac.id/index.php?n=internet')

input_nrp = driver.find_element_by_id('userid')
input_pwd = driver.find_element_by_id('password')

input_nrp.send_keys(NRP)
input_pwd.send_keys(password)
driver.find_element_by_tag_name('button').click()

time.sleep(3)
driver.quit()