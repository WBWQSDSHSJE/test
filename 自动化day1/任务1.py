from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get(r'file:///E:/python%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/Python%E4%BD%9C%E4%B8%9A/%E8%87%AA%E5%8A%A8%E5%8C%96/day1/%E7%BB%83%E4%B9%A0%E7%9A%84html/frame.html')

driver.maximize_window()

driver.find_element_by_id("input1").send_keys('ll')
# driver.find_element_by_xpath("//*[@id='input1']").send_keys("ll")

time.sleep(5)

driver.close()