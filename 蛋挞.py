from threading import Thread
import threading
import time

basket=0

lock=threading.Lock()

class Cook(Thread):
    chefname=''
    count=0

    def run(self) -> None:
        global  basket

        while 1:


            if basket>=500:
                time.sleep(10)




                    #break
            else:
                with lock:
                    basket = basket + 1
                    self.count = self.count + 1
                    print(self.chefname, '共做了', self.count, '个', sep='')



class Customer(Thread):
    name=''
    num=3000
    def run(self) -> None:
        global num
        global basket


        while 1 :
            if basket>0:
                with lock:
                    basket=basket-1
                    self.num=self.num-2
                    print(self.name,'买了一个！')
                    time.sleep(2)
            if self.num==0:
                    print(self.name,'买完了！',sep='')
                    break
            else:
                time.sleep(2)


cook1=Cook()
cook1.chefname='张三'
cook2=Cook()
cook2.chefname='李四'
cook3=Cook()
cook3.chefname='王五'
customer1=Customer()
customer1.name='1'
customer2=Customer()
customer2.name='2'

customer3=Customer()
customer3.name='3'
customer4=Customer()
customer4.name='4'
customer5=Customer()
customer5.name=5
customer6=Customer()
customer6.name='6'
cook1.start()
cook2.start()
cook3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()
