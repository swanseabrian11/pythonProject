import os
import pandas as pd

excelname = 'C:\/Users\Administrator\Pictures\新建文件夹\/1.xls'     # 这个改成你要读取的excel名
df = pd.read_excel(excelname, header=None)      # 读取 excel 数据
df.columns = ['aa', 'bb']     # 因为你的excel没有列名，所以手动设置一下列名，方便操作
path ='C:\/Users\Administrator\Pictures\新建文件夹 '

# 开始修改名字
for i in range(len(df)):
    print(type(df.aa[i]))
    name1 = os.path.realpath(os.path.join(path, df.bb[i]+'.txt'))     # 修改前的文件名绝对路径
    name2 = os.path.realpath(os.path.join(path, df.aa[i].astype(str)+'.txt'))     # 修改后的文件名绝对路径
    os.rename(name2, name1)    # 修改文件名