'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''

import xlrd
import pymysql
class  InitPage:

    login_success_data = [
        # id : msg_uname
        {"username": "jason", "password": "1234567", "expect": "Student Login"},
        {"username": "不再爱了", "password": "1234567", "expect": "Student Login"}
    ]

    login_error_data = [
        # id : msg_uname
        {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄"}
    ]

    login_success_data = []
    login_error_data = []
    #excel表获取数据
    wb=xlrd.open_workbook(filename=r'HKR.xlsx')
    sheet1=wb.sheet_by_name('sucess')
    sheet2=wb.sheet_by_name('error')

    row1=sheet1.nrows
    row2=sheet2.nrows

    for i in range(1,row1):
        data1=sheet1.row_values(i)
        if isinstance(data1[1],float)==True:
            data1[1]=int(data1[1])

        dict1={"username":data1[0],"password":str(data1[1]),"expect":data1[2]}

        login_success_data.append(dict1)
        #print(dict1)

    for j in range(1,row2):
        data2=sheet2.row_values(j)
        if isinstance(data2[1], float) == True:
            data2[1] = int(data2[1])
        dict2 = {"username": data2[0], "password": str(data2[1]), "expect": data2[2]}
        login_error_data.append(dict2)
        #print(dict2)


    #数据库
    success = []
    error = []
    con=pymysql.connect(host='localhost',user='root',password='root',database='zdhtest')
    cursor=con.cursor()

    sql1="select * from sucess"
    cursor.execute(sql1)

    data3=cursor.fetchall()
    for i in data3:
        if isinstance(i[1], float) == True:
            i[1] = int(i[1])
        dict3=dict2 = {"username": i[0], "password": i[1], "expect": i[2]}
        success.append(dict3)


    sql2 = "select * from error"
    cursor.execute(sql2)
    data4=cursor.fetchall()
    for i in data4:
        if isinstance(i[1], float) == True:
            i[1] = int(i[1])
        dict3=dict2 = {"username": i[0], "password": i[1], "expect": i[2]}
        error.append(dict3)


    cursor.close()
    con.close()























