import re

# File: readline-example-3.py
pattern = re.compile(r'(?<=数量为).*?(?=个)')
file = open("I:\/bat\wenbenchangdu\/a2.txt",encoding='utf-8')

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        m = pattern.findall(line)
        s = str(m).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择

        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        if int(s) < 30 and int(s) > 20:
            with open("I:\/bat\wenbenchangdu\/a1.txt", "a") as f1:
               f1.write(line)
        else:
            with open("I:\/bat\wenbenchangdu\/a3.txt", "a") as f2:
                f2.write(line)
        print(s)

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