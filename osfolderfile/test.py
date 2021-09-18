import re
import linecache
import os
import shutil
pattern1 = re.compile(r'(?<=姓名=).{1,200}')
pattern2 = re.compile(r'(?<=身份证号=).{1,200}')
pattern3 = re.compile(r'[0-9\u4e00-\u9fa5]')
# path = os.getcwd()
path = r"D:\重命名"
tarpath = r"D:\重命名\tar"
# print(list(path))
def whichEncode(text):
  text0 = text[0]
  try:
    text0.decode('utf8')
  except Exception as e:
    if "unexpected end of data" in str(e):
      file = open(text, encoding='utf-8')
    elif "invalid start byte" in str(e):
        file = open(text, encoding='gb2312')
    elif "ascii" in str(e):
       file = open(text, encoding='Unicode')
  return file
def search_file(file_name, search_path, pathsep = os.pathsep):
  for path in search_path.split(pathsep):
    candidate = os.path.join(path, file_name)
    if os.path.isfile(candidate):
      return os.path.abspath(candidate)
  return None
filelist =os.listdir(path)
path_list = []
for file in filelist:
     if file == 'tar':
         print(file)
     # 当前目录所包含文件或者文件夹的路径
     path1 = os.path.join(path,file)
     # find_file2 = search_file('tar', file)
     # tarpath = os.path.join(file, find_file2)
#    判断这个路径下是不是目录
     if os.path.isdir(path1):

         # find_file2 = search_file('tar', subpath1)
         # tarpath = os.path.join(path1, find_file2)
         path_list.append(path1)
         print(path1)
         # return path1


         for subpath in path_list:
             os.path.isdir(path1)
             find_file = search_file('识别结果.txt', subpath)
             find_file1 = search_file('手持.jpg', subpath)
             if find_file:
                 # print("File 'babyos.img' found at %s" % find_file)
                 sbjgtxt = os.path.join(subpath, find_file)
             if find_file1:
                 scpic = os.path.join(subpath, find_file1)

                 try:
                     file = open(sbjgtxt, encoding='gbk')
                 except Exception as e:
                     shutil.copy(sbjgtxt, os.path.join(tarpath, find_file))

                 else:

                 # file = open(sbjgtxt, encoding='gb2312')
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
                               scpic1 = os.path.splitext(scpic)[0]
                               newname1 = scpic.replace(scpic1, newname)
                               print(newname)
                               try:
                               ##'有可能出现异常的代码放在这里'
                                   shutil.copy(scpic, os.path.join(tarpath, newname1))
                               except:
                                   pass
                                   continue