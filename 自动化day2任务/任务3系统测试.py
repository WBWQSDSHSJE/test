from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
time.sleep(5)

driver.get("http://localhost:8080/HKR/admin_jsps/login.jsp;jsessionid=F87AFF8F6F026B3F24D9648515EC3321")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys('jason')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='password']").send_keys('admin')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(3)

#1.评价
#进入评价，可以先创建评价，或者找日期
data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@id='_easyui_tree_15']").click()
time.sleep(3)

#导出评价
driver.find_element_by_xpath("//*[@class='l-btn-icon icon-redo']").click()
time.sleep(5)


#评价报表
driver.find_element_by_xpath("//*[@id='_easyui_tree_16']").click()
time.sleep(2)

#关闭下方下载条
#pass

#2.报表下载，考虑截图
driver.get_screenshot_as_file('b.png')


#3.日志
data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']").click()
time.sleep(3)

#下载日志
data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='l-btn-icon pagination-next']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
time.sleep(5)
#i.分页显示数据量，第xx页模块
#pass


#driver.quit()





