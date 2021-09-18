import pymysql
import xlrd




def create():
    # 1.连接数据库

    con = pymysql.connect(host="localhost", user="root", password="root", database="sell")

    # 2.创建控制台
    cursor = con.cursor()

    # 3.准备一条sql语句
    #4.执行sql

    wb = xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")

    sheets = wb.sheet_names()
    print(sheets)

    param1=[]
    # 操作选项卡

    for i in sheets:
        list1 = []
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows
        sql="create table `%s` (日期 varchar(10),服装名称 varchar(10),`价格/件` varchar (10),本月库存数量 varchar(20) ,销售量 varchar (10));"
        param=[i]
        cursor.execute(sql,param)
        con.commit()

        for j in range(1, rows):
            list1 = sheet.row_values(j)
            list1.insert(0,i)
            sql1="insert into `%s` values(%s,%s,%s,%s,%s);"
            # 4.执行sql
            cursor.execute(sql1,list1)
            con.commit()
            del list1
    # 5.提交数据,真正提交到数据库
    # con.commit()
    # 6.关闭资源
    cursor.close()
    con.close()


#调用函数
create()






















