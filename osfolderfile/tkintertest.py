import re
import os
from tkinter import *
import chardet
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

# File: readline-example-3.py


  # openfile1 = askopenfilename(title="目标文件",initialdir="c:",filetypes=[('TXT', 'txt')])
  # directory = os.path.split(openfile1)[0]
  # tarpath = os.path.join(directory,"shoujihao.txt")
pattern = re.compile(r'{.*?}')
# file = open(r"C:\Users\Administrator\Desktop\vbs\删除{}及里面内容测验用文件\专用测验\43∑44.txt",'r',encoding='UTF-8')
# try:
file = open(r"C:\Users\Administrator\Desktop\bat\0917批量删括号及里面内容7个文件\批量删括号及里面内容\11.txt",'rb')
# with open(r"C:\Users\Administrator\Desktop\vbs\删除{}及里面内容测验用文件\专用测验\43∑44.txt",'rb') as file:
  # file = open( openfile1, 'r', encoding='utf-8')

# for file in os.listdir(src):
# #     if os.path.isfile(os.path.join(src, file)) == True:
# #         filepath = os.path.isfile(os.path.join(src, file))
# with open(file, 'rb') as f:

neirong = file.read().decode('gbk','ignore')
# except:
#     file = open(r"C:\Users\Administrator\Desktop\bat\0917批量删括号及里面内容7个文件\批量删括号及里面内容\11.txt",'r',encoding='utf-8-sig')
#     neirong = file.read()
# f_charInfo = chardet.detect(rb)
# print(f_charInfo)  # 输出文本格式信息
# print(f_charInfo['encoding'])  # 取得文本格式
# print(rb.decode(f_charInfo['encoding']))  # 通过取得的文本格式读取txt
# neirong = rb.decode(f_charInfo['encoding'],errors = 'ignore')
m = pattern.sub('', neirong)
print(m)
# # print(txt)
#   # if not lines:
#   #     break
#   # for line in lines:
#   #     ls = []
#   #    m = pattern.sub('',txt)
#   # # print(m)
#   #     # file.truncate(0)
#   #
#   #
#   #     # if m:
#   #     #     # print(line)
with open(r"C:\Users\Administrator\Desktop\bat\0917批量删括号及里面内容7个文件\批量删括号及里面内容\11.txt",'w') as f1:
#
    f1.write(m)
