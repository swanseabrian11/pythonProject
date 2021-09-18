import re
import os

# File: readline-example-3.py
pattern = re.compile(r'^\d+')
file = open("I:\/bat\wenbenchangdu\/a2.txt", encoding='utf-8')

src = 'I:\/001\/001\/23408-FP·2014-Y-%y%y%y0001-23408-FP·2014-Y-%y%y%y0001-23408-FP·2014-Y-0001'
target = 'I:\/001\/002'
for file in os.listdir(src):
    if os.path.isfile(os.path.join(src, file)) == True:
        # file_name = os.path.basename(__file__)
        # print(__file__)
        # # 输出为 test.py
        # file_name = file_name.split('.')[0]
        # print(file)
        #     m = pattern.findall(file)
        #     strm = str(m)
        #     s = str(m).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        #     #
        # s = s.replace("'", '').replace(',', '')   # 去除单引号，逗号，每行末尾追加换行符
        # # 输出为 test
        filename = os.path.splitext(file)[0]
        matchname = re.fullmatch(pattern, filename)
        print(matchname)
        if matchname != None:
            path = os.path.join(src, file)
            with open(path, 'rb') as rstream:
                container = rstream.read()
            path1 = os.path.join(target, file)
            with open(path1, 'wb') as wstream:
                wstream.write(container)

    # newname = file.replace(filename, s)
    # print(newname)
    # # m = pattern.findall(file_name)
    # os.rename(os.path.join(path,file),os.path.join(path,newname))
    # print(file)


# while 1:
#     lines = file.readlines(100000)
#     if not lines:
#         break
#     for line in lines:
#         m = pattern.findall(line)
#         s = str(m).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
#
#         s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
#         if int(s) < 30 and int(s) > 20:
#             with open("I:\/bat\wenbenchangdu\/a1.txt", "a") as f1:
#                f1.write(line)
#         else:
#             with open("I:\/bat\wenbenchangdu\/a3.txt", "a") as f2:
#                 f2.write(line)
#         print(s)

# if  m[line] <30 and m[line]>20:
#     with open("I:\bat\wenbenchangdu\a1.txt", "w") as f1:
#         # for i in range(len(m)):
#         #     for i in range(len(m)):
#         #         # s = str(m[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
#         #         s = str(m[i])
#         #         s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
#
#                 f1.write(line)
# pass  # do something
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)

        for file in filelist:
            path = os.path.join(src, file)
            with open(path, 'rb') as rstream:
                container = rstream.read()
            path1 = os.path.join(target, file)
            with open(path1, 'wb') as wstream:
                wstream.write(container)
        else:
            print('复制完毕')
