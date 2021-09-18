import re
import os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

# File: readline-example-3.py
def selectfile():

  openfile1 = askopenfilename(title="目标文件",initialdir="c:",filetypes=[('TXT', 'txt')])
  directory = os.path.split(openfile1)[0]
  tarpath = os.path.join(directory,"shoujihao.txt")
  pattern = re.compile(r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$')
  # file = open(r"C:\Users\Administrator\Desktop\/vbs\ivr_callee.txt",'r',encoding='utf-8')
  file = open( openfile1, 'r', encoding='utf-8')

  while 1:
      lines = file.readlines(100000)
      if not lines:
          break
      for line in lines:

          m = pattern.findall(line)
          # print(m)
          if m:
              # print(line)
              with open(tarpath, "a") as f1:
                  f1.write(line)
  # t.start()

root = Tk()
root.title('手机号整理')
root.resizable(0,0)
root.geometry('250x150')
Button(root, text = "路径选择", command = selectfile).pack()
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

