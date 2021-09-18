from tkinter.filedialog import askdirectory
import tkinter.messagebox
from tkinter import *
import os
import chardet


def selectfile():
    dir1 = askdirectory()
    pattern = re.compile(r'{.*?}')
    for file in os.listdir(dir1):
        if os.path.isfile(os.path.join(dir1, file)):
            filepath = os.path.join(dir1, file)
            with open(filepath, 'rb') as f:
                rb = f.read()
            # code = chardet.detect(rb)['encoding']
            with open(filepath, errors= 'ignore') as f:
                m = pattern.sub('', f.read())
            with open(filepath, "w") as f:
                f.write(m)
    tkinter.messagebox.showinfo('提示', '操作完成')


root = Tk()
root.title('删除大括号')
root.resizable(0, 0)
root.geometry('250x150')
Button(root, text="路径选择", command=selectfile).pack()

root.mainloop()