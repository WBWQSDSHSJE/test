import random
start=100
print("初始资金为100，猜一次使用10金币，猜一个0~10的数字，开始游戏吧！")
num=random.randint(0,10)
guess=int(input("请输入一个数字："))
while guess!=num:
    start-=10
    if start==0:
        print("金币使用完毕！")
        break
    else :
        if guess>num:
            print("数字太大了！请重新猜！")
            print("当前金币数为",start)
            guess = int(input("请输入一个数字："))
        elif guess <num:
            print("太小了，请重新猜！")
            print("当前金币数为", start)
            guess = int(input("请输入一个数字："))
if guess==num:
    print("猜对了！就是",num)
    start=start-10
    print("当前金币数为", start)