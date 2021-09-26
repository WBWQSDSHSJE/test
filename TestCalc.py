'''
    unittest：单元测试框架。
    1.子类继承TestCase
    2.写测试用例,testXxx
    3.运行

'''
from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testAdd1(self):
        num1 = 10
        num2 = 10
        sum = 20

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)


    def testAdd2(self):
        num1 = -10
        num2 = -10
        sum = -20

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testAdd3(self):
        num1 = -10
        num2 = 10
        sum = 0

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testAdd4(self):

        num1 = 100000000000000000000000000000000000000000000000000000
        num2 = 10
        sum = 100000000000000000000000000000000000000000000000000010

        calc = Calc()
        s = calc.add(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMinus1(self):
        num1=10
        num2=5
        sum=5
        calc=Calc()
        s=calc.minus(num1,num2)

        self.assertEqual(sum,s)
    def testMminus2(self):
        num1=-10
        num2=-5
        sum=-5
        calc=Calc()
        s=calc.minus(num1,num2)
        self.assertEqual(sum,s)
    def testMinus3(self):
        num1=10
        num2=-5
        sum=15
        calc=Calc()
        s=calc.minus(num1,num2)
        self.assertEqual(sum,s)
    def testMnus4(self):
        num1=-10
        num2=5
        sum=-15
        calc=Calc()
        s=calc.minus(num1,num2)
        self.assertEqual(sum,s)

    def testmulti1(self):
        num1 = 10
        num2 = 5
        sum = 50
        calc = Calc()
        s = calc.multi(num1, num2)

        self.assertEqual(sum, s)

    def testmulti2(self):
        num1 = -10
        num2 = -5
        sum = 50
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(sum, s)

    def testmulti3(self):
        num1 = 10
        num2 = -5
        sum = -50
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(sum, s)

    def testmulti4(self):
        num1 = -10
        num2 = 5
        sum = -50
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(sum, s)

    def testdevision1(self):
        num1 = 10
        num2 = 5
        sum = 2
        calc = Calc()
        s = calc.devision(num1, num2)

        self.assertEqual(sum, s)

    def testdevision2(self):
        num1 = -10
        num2 = -5
        sum = 2
        calc = Calc()
        s = calc.devision(num1, num2)
        self.assertEqual(sum, s)

    def testdevision3(self):
        num1 = 10
        num2 = -5
        sum = -2
        calc = Calc()
        s = calc.devision(num1, num2)
        self.assertEqual(sum, s)

    def testdevision4(self):
        num1 = -10
        num2 = 5
        sum = -2
        calc = Calc()
        s = calc.devision(num1, num2)
        self.assertEqual(sum, s)










