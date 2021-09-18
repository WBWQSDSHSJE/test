import xlrd

#打开工作簿
wb=xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")



sheets=wb.sheet_names()

#选择操作选项卡
for i in sheets:
    sheet=wb.sheet_by_name(i)
    rows=sheet.nrows
    clos = sheet.ncols
    dict1 = {}
    list2 = sheet.col_values(1)
    list3 = sheet.col_values(4)
    sets = set()
    sum=0

    #将每个月的衣服名清空冗余数据放在sets中
    for k in range(1, len(list2)):
       sets.add(list2[k])
    #求每个月的销售总量
    for h in range(1,len(list3)):
        sum = sum + list3[h]
    #将衣服名称和销售量做成字典
    for t in sets:
        dict1[t]=0
    for j in range(1,rows):
        list1=sheet.row_values(j)
        if list1[1] in dict1.keys():
            dict1[list1[1]]=list1[4]+list1[4]
    print('\n',i, ':')

    for p in dict1.items():
        b = format(round(p[1] / sum, 4), '.2%')

        print(p[0], '占比为', b, sep='',end='  ')












