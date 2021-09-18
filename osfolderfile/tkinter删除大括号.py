import re
import os
from tkinter import *
from math import trunc
import chardet
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

import tkinter.messagebox

# File: readline-example-3.py
def selectfile():

  # openfile1 = askopenfilename(title="目标文件",initialdir="c:",filetypes=[('TXT', 'txt')])
  dir1 = askdirectory()
  # directory = os.path.split(openfile1)[0]
  # tarpath = os.path.join(directory,"shoujihao.txt")
  pattern = re.compile(r'{.*?}')
  # txtlist = os.listdir(src)
  # step = trunc(100 / len(txtList))
  # file = open(r"C:\Users\Administrator\Desktop\vbs\删除{}及里面内容测验用文件\专用测验\43∑44.txt",'r',encoding='utf-8')
  # file = open( openfile1, 'r', encoding='utf-8')

  for file in os.listdir(dir1):
      if os.path.isfile(os.path.join(dir1, file)) == True:
          filepath = os.path.join(dir1, file)
          # with open(filepath, 'rb') as f:
          try:
            with open(filepath, errors= 'ignore') as f:

                neirong = f.read()
              # f_charInfo = chardet.detect(rb)
          # print(f_charInfo)  # 输出文本格式信息
          # print(f_charInfo['encoding'])  # 取得文本格式
          # print(rb.decode(f_charInfo['encoding']))  # 通过取得的文本格式读取txt
          #     neirong = rb.decode(f_charInfo['encoding'])
            m = pattern.sub('', neirong)


            with open(filepath, "w" ) as f:
                  # f1.truncate(0)
                  f.write(m)
          except:
             pass
             continue
  tkinter.messagebox.showinfo('提示', '操作完成')

root = Tk()
root.title('删除大括号')
root.resizable(0,0)
root.geometry('250x150')
Button(root, text = "路径选择", command = selectfile).pack()
# tkinter.messagebox.showinfo('提示','操作完成')
# print(file)
root.mainloop()
# pattern = re.compile(r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$')
# # file = open(r"C:\Users\Administrator\Desktop\/vbs\ivr_callee.txt",'r',encoding='utf-8')
# file = open(gfile,'r',encoding='utf-8')
#
# while 1:
#     lines = file.readlines(100000)
#     if not lines:
#         break
#     for line in lines:
#
#         m = pattern.findall(line)
#         # print(m)
#         if m:
#             # print(line)
#             with open(r"C:\Users\Administrator\Desktop\/vbs\1.txt", "a") as f1:
#                 f1.write(line)

