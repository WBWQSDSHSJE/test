import xlrd

#打开工作簿
wb=xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")



sheets=wb.sheet_names()

#选择操作选项卡
sum=0
#全年总销售额
for i in sheets:
    sheet = wb.sheet_by_name(i)
    rows = sheet.nrows  # 获取取的是行数目
    for j in range(1, rows):
        data = sheet.row_values(j)  # 获取一行值
        sum = sum + data[2] * data[4]

for i in sheets:
    sheet=wb.sheet_by_name(i)
    rows1=sheet.nrows
    cols=sheet.ncols
    sets = set()
    dict1={}
    list2=sheet.col_values(1)
    sums=0

    #将每个衣服放在sets中
    for k in range(1,len(list2)):
        sets.add(list2[k])
    #将每个衣服放在字典里，将销售金额赋值为0
    for q in sets:
        dict1[q]=0

    print('\n',i,':')


    for j in range(1,rows1):
        list1=sheet.row_values(j)
        if list1[1] in dict1.keys():
            sums  =sums+list1[2]*list1[4]
            dict1[list1[1]]=sums
    for p in dict1.items():

        b=format(round(p[1] / sum, 4), '.2%')
        print(p[0],'占比为：',b,sep='',end='  ')







