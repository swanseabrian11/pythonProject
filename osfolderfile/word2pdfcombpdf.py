from win32com.client import DispatchEx
from os import walk
import pythoncom
import os
import threading
import time

wdFormatPDF = 17


def doc2pdf(input_file):
    pythoncom.CoInitialize()
    with semaphore:
        lock.acquire()
    word = DispatchEx('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".doc", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
    lock.release()


if __name__ == "__main__":
    # 控制线程最大并发数为12
    start = time.time()
    semaphore = threading.BoundedSemaphore(50)
    # 线程锁
    lock = threading.Lock()
    directory = os.getcwd()
    doc_files = []
    # directory = r"I:\石堂村分户资料-打印 (1)\411722216208JC00770陈彦章"
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                path1 = str(root + "\\" + file)
                print(root)
                threading.Thread(target=doc2pdf, args=(path1,)).start()

    end = time.time()
    print(end - start, "秒")
                # doc2pdf(str(root + "\\" + file))