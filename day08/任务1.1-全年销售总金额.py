import xlrd

#打开工作簿
wb=xlrd.open_workbook(filename=r"E:\python自动化测试\Python作业\python11\day07[xlrd excel表格读写]\任务\2020年每个月的销售情况.xlsx")

#获取全部的sheet表格名
sheet=wb.sheet_names()
sum=0
for i in sheet:
    sheets=wb.sheet_by_name(i)
    rows=sheets.nrows #获取取的是行数目
    for j in range(1,rows):
        data=sheets.row_values(j) #获取一行值
        sum=sum+data[2]*data[4]


print(sum)














