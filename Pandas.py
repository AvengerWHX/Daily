
import pandas as pd
import numpy as np

# 导入CSV或者xlsx文件
# df = pd.DataFrame(pd.read_csv('name.csv',header=1))
df = pd.DataFrame(pd.read_excel('C:\\Users\\Administrator\\Desktop\\name.xlsx'))

# 用pandas创建数据表
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
                   "date":pd.date_range('20130102', periods=6),
                   "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age":[23,44,54,32,34,32],
                   "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
                   "price":[1200,np.nan,2133,5433,np.nan,4432]},
                  columns =['date','city','category','age','price','id'])
print(df)

# 数据表信息查看
# 1.维度查看
df.shape
print(df.shape)
# 2.数据表基本信息（维度、列名称、数据格式、所占空间等）
df.info()
print("-----------",df.info())

# 3.每一列数据的格式
df.dtypes
# 4.某一列格式
df['price'].dtype
# 5.空值
df.isnull()
# 6.查看某一列空值
df.isnull()

df.to_excel('C:\\Users\\Administrator\\Desktop\\name.xlsx', sheet_name='bluewhale_cc')