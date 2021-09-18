import xlrd

#1.打开
wb = xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")

# 2.操作选项卡

def yue(n):
    sheet = wb.sheet_by_index(n)

    sheet.row_values(0)
    sheet.col_values(0)

    cols = sheet.ncols  # 获取有多少列
    rows = sheet.nrows # 获取有多少行
    sets=set()
    dict1={}
    # 1月份销售额
    for i in range(1,rows):
        data = sheet.row_values(i)#哪行
        sets.add(data[1])
        k=0
        for j in sets:
            dict1[j]=0
        for i in range(1,rows):
            data1 = sheet.row_values(i)#哪行
            if data1[1] in dict1.keys():
                k=k+data1[4]
                dict1[data1[1]]=k
    return  dict1

def he(m,p,q):
    dict1=yue(m)
    dict2=yue(p)
    dict3=yue(q)

    sum=0
    num=0

    for i in dict1.keys():
        for j in dict2.items():
            if j[0] in i:
                sum=j[1]+sum
                dict1[j[0]]=sum
    for i in dict1.keys():
        for j in dict3.items():
            if j[0] in i:
                sum=j[1]+sum
                dict1[j[0]]=sum

    for i in dict1.items():
        if num<=i[1]:
            num=i[1]
            b=i[0]
    if m==2and p==3 and q==4:
        print('第一季度最畅销的衣服是',b,'，销售了',num,'件！',sep='')
    elif m==5and p==6 and q==7:
        print('第二季度最畅销的衣服是',b,'，销售了',num,'件！',sep='')
    elif m==8 and p==9 and q==10:
        print('第三季度最畅销的衣服是',b,'，销售了',num,'件！',sep='')
    if m==11 and p==0 and q==1:
        print('第四季度最畅销的衣服是',b,'，销售了',num,'件！',sep='')
he(0,1,2)


for i in range(4,11):
    he((i-2),(i-1),i)

he(11,0,1)




