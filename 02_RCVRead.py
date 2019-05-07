'''
    rcv上报数据的格式化，并将其存储到excel文件中
'''

import os
import xlwt

# 读取txt文件数据
a = str(input("请输入文件名称："))
txtFilePath = "C:\\Users\\Administrator\\Desktop\\"+a
txtFile = None
if os.path.exists(txtFilePath):
    txtFile = open(txtFilePath,"r")
    print("读取了已存在的txt文件")
else:
    txtFile = open(txtFilePath,"w+")
    print("文件不存在，现在已创建")

contentStr = txtFile.read()
txtFile.close()
print("测试数据",contentStr)

# 解析数据
contentArr = []
content = []
if contentStr != '':
    print(contentStr)
    contentArr = contentStr.split('&')
    print(contentArr)
    print(contentStr)
    txtFile.close()
else:
    print("文本文件内容为空")
    txtFile.close()

for myStr in contentArr:
    content.append(myStr.split('='))

print(content)

'''
    将数据写入excel文件的方法
    file_path：文件路径
    datas：二维数组数据
'''
def data_write(file_path, datas):
    # 创建一个excel文件
    workbook = xlwt.Workbook()
    # 添加一个sheet页
    sheet1 = workbook.add_sheet(a,cell_overwrite_ok=True)

    # 将数据写入表格
    row = 0
    for data in datas:
        col = 0
        for ss in data:
            sheet1.write(row,col,ss)
            col = col+1
        row = row + 1
    # 保存文件
    if(os.path.exists(file_path)==True):
        os.remove(file_path)
        print("删除了已存在的文件")
        workbook.save(file_path)
    else:
        workbook.save(file_path)

# 调用方法
xlf ="C:\\Users\\Administrator\\Desktop\\rcv.xls"
data_write(xlf,content)