from selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get(r'https://www.suning.com/?utm_source=360&utm_medium=brand&utm_campaign=title&utm_term=brand')

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys('冰箱')
time.sleep(5)
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(5)

driver.get('https://product.suning.com/0070135396/12194058264.html?safp=d488778a.13701.productWrap.10&safc=prd.0.0&safpn=10007.244005')
#driver.find_element_by_xpath("//*[@class='res-img']").click()
time.sleep(5)

data=driver.window_handles
driver.switch_to_window(data[-1])

driver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(5)

data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@class='go-cart']").click()
time.sleep(5)

data=driver.window_handles
driver.switch_to_window(data[-1])
driver.find_element_by_xpath("//*[@class='checkout cart-btn']").click()
time.sleep(10)

driver.quit()
#https://product.suning.com/0070135396/12194058264.html?safp=d488778a.13701.productWrap.10&safc=prd.0.0&safpn=10007.244005