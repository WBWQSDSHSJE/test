import time
from selenium import webdriver

driver=webdriver.Chrome()

driver.get(r'https://www.baidu.com/')

driver.find_element_by_xpath("//*[@id='kw' and @name='wd']").send_keys('李白')

driver.find_element_by_xpath("//*[@id='su' and @type='submit']").click()

#https://www.baidu.com/
#缓冲
time.sleep(5)
#点击第一个链接
driver.find_element_by_id("1").find_element_by_tag_name("a").click()
#跳转新窗口定位句柄
# a=driver.window_handles
# driver.switch_to_window(a[1])