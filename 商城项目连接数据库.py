import  pymysql
import string
import random
import  datetime as dt
import time
#连接数据库
con=pymysql.connect(host="localhost",user="root",password="root",database="bank")


#创建控制台
cursor=con.cursor()

#工商银行
bname="中国工商银行" #界面
bsystem="账户管理系统"
bbanben="版本是V3.0"

while 1:
    print('\033[34m*\033[0m' * 30)
    print('\033[34m*\033[0m', bname.center(22), '\033[34m*\033[0m')
    print('\033[34m*\033[0m', bsystem.center(22), '\033[34m*\033[0m')
    print('\033[34m*\033[0m', bbanben.center(24), '\033[34m*\033[0m')
    print('\033[34m*\033[0m' * 30)
    print('\033[34m*1.开户\033[0m', " " * 20, '\033[34m*\033[0m')
    print('\033[34m*2.存钱\033[0m', " " * 20, '\033[34m*\033[0m')
    print('\033[34m*3.取钱\033[0m', " " * 20, '\033[34m*\033[0m')
    print('\033[34m*4.转账\033[0m', " " * 20, '\033[34m*\033[0m')
    print('\033[34m*5.查询\033[0m', " " * 20, '\033[34m*\033[0m')
    print('\033[34m*6.bye\033[0m', " " * 20, '\033[34m*\033[0m')
    print("请选择业务")
    a = input()
# 开户
    if a=="1":

        print("确定开户？（输入yes开始开户，no退出）")
        cursor.execute("select count(*) from info")
        num = cursor.fetchone()
        if num[0]>100:
            print("存储已满，无法再开户！")
            continue

        print("请输入：")
        b = input()
        if b=="yes" :
            seeds = string.digits

            random_str = []
            for i in range(8):
                random_str.append(random.choice(seeds))

            number = "".join(random_str)
            print("这是您的账号：",number)
            print("请输入您的姓名")
            name=input()
            print("请输入6位数密码：")
            passwords=input()#要判断一下是否为6位数字
            t=len(passwords)
            if passwords.isdigit()==False and t!=6:
                print("请输入6位数字！")
                continue

            account=0
            print("请输入您的地址：")
            print("国家：")
            address1= input()
            print("省份：")
            address2 = input()
            print("街道")
            address3 = input()
            print("门牌号")
            address4 = input()


            time=dt.datetime.now().strftime('%F %T')

            sql="insert into info value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            param = [number,name,passwords,address1,address2,address3,address4,0,time,bname]
            cursor.execute(sql, param)
            con.commit()



            continue

        elif b=="no":

            continue
        else :
            print("输入错误，请重新输入!")
            continue
#存钱
    elif a=="2":
        print("请输入账号：")
        number1=input()
        print("请输入密码：")
        pass1=input()

        cursor.execute("select account,`password` ,money from info;")
        data1 = cursor.fetchall()
        con.commit()
        for j in data1:
            if number1  in j:

                if pass1==j[1]:
                    a = 1
                    break
            else :
                a=0

        if a==0:
            print('账号或密码输入错误！')
            continue
        else:

            for i in data1:


                if i[0]==number1 and i[1]==pass1:

                    print("请输入存款金额：")
                    m = float(input())+float(i[2])
                    money=str(m)
                    t=[money,i[0]]
                    sql = "update info set money=%s where account=%s;"
                    cursor.execute(sql,t)
                    con.commit()
                    print('存钱成功！',m,'5秒后跳转。')
                    time.sleep(5)
                    break


#取钱

    elif a=="3":
        print("请输入账号：")
        number1 = input()
        print("请输入密码：")
        pass1 = input()

        cursor.execute("select account,`password` ,money from info;")
        data1 = cursor.fetchall()
        con.commit()
        for j in data1:
            if number1 in j:

                if pass1 == j[1]:
                    a = 1
                    break
            else:
                a = 0

        if a == 0:
            print('账号或密码输入错误！5秒后跳转。。。')
            time.sleep(5)
            continue
        else:

            for i in data1:

                if i[0] == number1 and i[1] == pass1:
                    print("请输入取款金额：")
                    m = -float(input()) + float(i[2])
                    if m<0:
                        print('余额不足！5秒后跳转。。。')
                        time.sleep(5)
                        break
                    money = str(m)
                    t = [money, i[0]]
                    sql = "update info set money=%s where account=%s;"
                    cursor.execute(sql, t)
                    con.commit()
                    print('取钱成功！账户余额为：',m, '5秒后跳转。')
                    time.sleep(5)
                    break
#转账
    elif a=="4":

        print("请输入付款账号：")
        number1 = input()
        account2 = input('请输入收款账号：')
        moneys=float(input('请输入转账钱数：'))
        print("请输入密码：")
        pass1 = input()


        cursor.execute("select account,`password` ,money from info;")
        data1 = cursor.fetchall()
        con.commit()
        for j in data1:
            if number1 in j:

                if pass1 == j[1]:
                    a = 1
                    break
            else:
                a = 0
        for i in data1:
            if account2 in i:
                b=3
                list1=i

                break
            else:
                b=4
        if b==4:
            print('转账账号输入错误！5秒后跳转。。。')
            time.sleep(5)
            continue

        elif a == 0:
            print('账号或密码输入错误！')
            continue
        else:

            for i in data1:

                if i[0] == number1 and i[1] == pass1:

                    m = -moneys + float(i[2])
                    if m < 0:
                        print('余额不足！5秒后跳转。。。')
                        time.sleep(5)
                        break
                    money2=str(float(list1[2])+moneys)
                    n=[money2,account2]


                    money = str(m)
                    t = [money, i[0]]
                    sql = "update info set money=%s where account=%s;"
                    cursor.execute(sql, t)
                    cursor.execute(sql, n)
                    con.commit()
                    print('转账成功！账户余额为：',m, '5秒后跳转。')
                    time.sleep(5)
                    break

#查询

    elif a=="5":
        print("请输入账号：")
        number1 = input()
        print("请输入密码：")
        pass1 = input()

        cursor.execute("select account,`password` ,money from info;")
        data1 = cursor.fetchall()
        con.commit()
        for j in data1:
            if number1 in j:

                if pass1 == j[1]:
                    a = 1
                    break
            else:
                a = 0

        if a == 0:
            print('账号或密码输入错误！5秒后跳转。。。')
            time.sleep(5)
            continue
        else:
            sql = "select * from info where account = %s"
            param = [number1]
            cursor.execute(sql, param)
            data = cursor.fetchall()
            for i in data:
                print('账号：',i[0],'  姓名：',i[1],' 密码：',i[2],' 国家：',i[3],' 城市：',i[4],' 街道',i[5],' 门牌号',i[6],' 余额',i[7],' 修改时间：',i[8],' 开户行',i[9],sep='')
                time.sleep(5)



    elif a=="6":
        print("确认退出？（输入yes退出，no不退出。）")
        q=input()
        if q=="yes":
            exit(0)
        elif q=="no":

            continue
        else:
            print("输入错误！")
            continue
    else :
        print("输入有误，请重新输入！")


# 3.准备一条sql语句
# sql = "insert into  t_dept value(%s,%s,%s)"
# param = ['103','后勤部','南京']

# 4.执行sql
# cursor.execute(sql,param)


# 5.提交数据,真正提交到数据库
# con.commit()


# 6.关闭资源
cursor.close()
con.close()
