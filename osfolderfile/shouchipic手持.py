import re
import linecache
import os
import shutil
from itertools import chain

def search_file(file_name, search_path, pathsep = os.pathsep):
  for path in search_path.split(pathsep):
    candidate = os.path.join(path, file_name)
    if os.path.isfile(candidate):
      return os.path.abspath(candidate)
  return None
def getFilePath(path):
    path_list = []
    filelist =os.listdir(path)
#
    for file in filelist:
     # 当前目录所包含文件或者文件夹的路径
      path1 = os.path.join(path,file)
#
#    判断这个路径下是不是目录
      if os.path.isdir(path1):
         path_list.append(path1)
         print(path_list)
         return path_list

# 合并同一目录下的所有PDF文件
def newname(pathlist,tarpath):
    pattern1 = re.compile(r'(?<=姓名=).{1,200}')
    pattern2 = re.compile(r'(?<=身份证号=).{1,200}')
    pattern3 = re.compile(r'[0-9\u4e00-\u9fa5]')
    for subpath in pathlist:
      # os.path.isdir(path1)
      find_file = search_file('识别结果.txt', subpath)
      find_file1 = search_file('手持.jpg', subpath)
      if find_file:
            # print("File 'babyos.img' found at %s" % find_file)
       sbjgtxt = os.path.join(subpath, find_file)
       scpic   = os.path.join(subpath,  find_file1)
       scpic1 = os.path.splitext(scpic)[0]
       file = open(sbjgtxt, encoding='utf-8')
       while 1:
         lines = file.readlines()

         if not lines:
            break
         for line in lines:
              line = line.strip()
              m = pattern1.findall(line)
              if m:
                s = str(m).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
                s = s.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
                m1 = pattern2.findall(line)
              if m1:
                s1 = str(m1).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
                s1 = s1.replace("'", '').replace(',', '')  # 去除单引号，逗号，每行末尾追加换行符
                print(s1)
                newname = s + s1
                print(newname)
                shutil.copy(scpic1,os.path.join(tarpath, newname.jpg.xlsx))
              # os.rename(scpic1, os.path.join(tarpath, newname.jpg))
#
    #     print("没有可以合并的PDF文件！")
if __name__ == "__main__":

    path = r"C:\Users\Administrator\Desktop\测试命名保存\测试命名保存"
    tarpath = r"C:\Users\Administrator\Desktop\测试命名保存\测试命名保存\tar"
    # path = os.getcwd()
    pathlist = getFilePath(path)
    # newname(pathlist, tarpath)