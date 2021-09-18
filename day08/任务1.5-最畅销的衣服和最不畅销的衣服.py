import xlrd
import pymysql
# #1.连接数据库
# con=pymysql.connect(host="localhost",user="root",password="root",database="sell")
#
# #2.创建控制台
# cursor=con.cursor()






#一、打开工作簿
wb=xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")


sheets=wb.sheet_names()
sum=0
sets=set()
dict1={}
#二、操作选项卡  三、找数据
for i in sheets:
    sheet=wb.sheet_by_name(i)
    clos=sheet.ncols

    list1=sheet.col_values(4)
    list2=sheet.col_values(1)
    for j in range(1,len(list1)):
        sum=sum+list1[j]
    for k in range(1,len(list2)):

        sets.add(list2[k])
print(sets)
#sets集合中的数据存在字典中
for h in sets:
    dict1[h]=0




#3.准备sql语句
#4.执行sql语句
#求表中每一月的名字和相应销售量
for i in sheets:
    sheet = wb.sheet_by_name(i)
    rows=sheet.nrows
    for j in range(1,rows):
        list3=sheet.row_values(j)
        if list3[1] in dict1.keys():

            dict1[list3[1]]=dict1[list3[1]]+list3[4]


a=0
for o in dict1.items():
    if o[1]>=a:
        a=o[1]
        b=o[0]
c=a
for u in dict1.items():
    if c>=u[1]:
        c=u[1]
        d=u[0]
print('最畅销的衣服是：',b,',卖出了',a,'件！',sep='')
print('最不畅销的衣服是：',d,',卖出了',c,'件！',sep='')












