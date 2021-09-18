import os
from openpyxl import Workbook


def main():
    # path = r"C:\Users\Administrator\Desktop\两天总文件夹\总文件夹"
    path = os.getcwd()
    wb = Workbook()
    ws = wb.active
    for a, b, c in os.walk(path):  # walk自动遍历文件夹，a是当前遍历的子文件夹，c是子文件夹下的文件列表
        # print(a, b, c)
        c.insert(0, a)  # 把path也加入到列表中
        ws.append(c)  # 写入到excel
    wb.save('test.xlsx')  # 最后保存


if __name__ == '__main__':
    main()