from appium import  webdriver
import time



url = "127.0.0.1:4723/wd/hub"#在软件Appium的Custom Server里面

param = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "splash.SplashActivity"
}

driver = webdriver.Remote(url,param)

# time.sleep(20)
# driver.find_element_by_xpath("//*[@id='com.ss.android.ugc.aweme:id/bk+']").click()
# el1 =  driver.findElementById("com.ss.android.ugc.aweme:id/bk+")
# el1.click()
#
# time.sleep(10)
# driver.tap(x=448, y=980).perform()#又被识别了？？？？？


time.sleep(20)
driver.tap(x=84,y=927).perform()
time.sleep(10)
driver.swipe(390,1214,390,351)#滑动















