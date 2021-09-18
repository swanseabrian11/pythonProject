import re

pattern = re.compile(r'[A-Z]{4,}/+')

with open("I:\html5定制学生作业\data.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    m = pattern.findall(data)

    with open("I:\html5定制学生作业\data2.txt", "w") as f1:
        for i in range(len(m)):
            for i in range(len(m)):

             # s = str(m[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
             s = str(m[i])
             s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符

             f1.write(s)
        #         print(m[1])

        # f1.write(s)
