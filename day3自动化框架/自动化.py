'''
    1.准备用户名和密码
    2.输入用户名，输入密码，点击登陆
    3.校验，断言

    框架：
        1.数据类：专门封装登录的所有，参数化的数据在这地方
        2.操作类：专门用于对模块进行操作的。
        3.用例类：整合数据类和操作类完成登陆的操作。
        4.入口程序：专门生成测试报告
'''
from unittest import TestCase
from selenium import  webdriver
class Demo(TestCase):
    def testLogin1(self):
        # 1.准备数据
        username = "jason"
        password = "1234567"
        expect = "Student Login1"  # 期望结果

        # 2.启动浏览器，输入数据
        driver = webdriver.Chrome()
        driver.get(r"http://localhost:8081/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        driver.find_element_by_xpath("//*[@id='submit']").click()

        # 3.断言
        #  获取浏览器的标题
        data = driver.title

        if expect !=  data:
            driver.save_screenshot("登陆失败！.jpg")
        else:
            print("登陆成功，用例通过！")


















