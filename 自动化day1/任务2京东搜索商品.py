from  selenium import webdriver
import time

driver=webdriver.Chrome()

driver.get(r"https://www.jd.com/?cu=true&utm_source=haosou-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_haosoupinzhuan&utm_term=0a875d61c5fe47d8bc48679132932d23_0_d97fae3b844e4408bbcd85715d201072")

time.sleep(3)
driver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/seckillcms/s280x280_jfs/t1/137855/37/23235/76403/6153dabeEa08680c3/76079048766d6b95.jpg.webp' ]").click()

time.sleep(5)
driver.quit()