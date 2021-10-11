from selenium import webdriver
import  time

driver=webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
time.sleep(1)

#进入注册页面
driver.get("http://localhost:8080/HKR/register.jsp;jsessionid=C25B392BECFCCF3E5E5ABBF6BAF02D48")
time.sleep(3)

#开始注册，第一步

driver.find_element_by_xpath("//*[@id='loginname']").send_keys('aaas')
driver.find_element_by_xpath("//*[@name='username']").send_keys('aaa')
driver.find_element_by_xpath("//*[@id='pwd']").send_keys('123456')
driver.find_element_by_xpath("//*[@name='reloginpass']").send_keys('123456')
time.sleep(3)
driver.find_element_by_xpath("//*[@type='button' and @name='next']").click()
time.sleep(3)
#第二步
# data=driver.window_handles
# driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@id='valid_age']").send_keys('20')
time.sleep(3)
#下拉框也可以当做输入框来做，直接发送文字
#pass
data=driver.window_handles
driver.switch_to_window(data[-1])



#最好使用复制xpath
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
#driver.find_element_by_xpath("//*[@class='next action-button']").click()
time.sleep(3)

#第三步
data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys('12584569845@qq.com')
driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys('13422556210')
driver.find_element_by_xpath("//*[@name='address']").send_keys('kfh')
driver.find_element_by_xpath("//*[@id='btn_reg']").click()
time.sleep(5)
driver.quit()





