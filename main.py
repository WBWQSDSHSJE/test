'''
    HTMLTestRunner：运行器，可以运行和生成测试报告
'''
from HTMLTestRunner import HTMLTestRunner
import  unittest


# 1.加载4条用例
tests = unittest.defaultTestLoader.discover(r"E:\Python bcwj\day12",pattern="Test*.py")


# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算器测试报告",
    #description= "计算器的加法测试报告",
    verbosity=1,
    stream=open(file="计算器报告.html",mode="w+",encoding="utf-8")
)

# 3.让运行器运行4条用例
runner.run(tests)



# 任务1：代码邮箱发送
# 任务2：减法，除法，乘法用例写出来。
# 4.代码 163 发送邮件，将报告添加为附件，发送给我13552648187@163.com
# 密码不是登陆密码，邮箱对第三方软件的授权码















