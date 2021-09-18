from win32com.client import Dispatch
from os import walk
import os
from PyPDF4 import PdfFileMerger
from PyPDF4 import PdfFileReader, PdfFileWriter
import PyPDF4
import time


# def getFileName(filedir):
#     for root, dirs, filenames in walk(filedir):
#         for d in dirs:
#             file_list = [f for f in os.listdir(os.path.join(root, d)) if f.endswith('.pdf')]
#             file_list = [os.path.join(root, d, filename) for filename in file_list]
#     # file_list = [os.path.join(root, filespath) \
#     #              for root, dirs, files in os.walk(filedir) \
#     #              for filespath in files \
#     #              if str(filespath).endswith('pdf')
#     #              ]
#     return file_list if file_list else []

# 合并同一目录下的所有PDF文件
# def MergePDF(filepath, outfile):
#
#     output = PdfFileWriter()
#     outputPages = 0
#     pdf_fileName = getFileName(filepath)
#
#     if pdf_fileName:
#         for pdf_file in pdf_fileName:
#             print("路径：%s"%pdf_file)
#
#             # 读取源PDF文件
#             input = PdfFileReader(open(pdf_file, "rb"))
#
#             # 获得源PDF文件中页面总数
#             pageCount = input.getNumPages()
#             outputPages += pageCount
#             print("页数：%d"%pageCount)
#
#             # 分别将page添加到输出output中
#             for iPage in range(pageCount):
#                 output.addPage(input.getPage(iPage))
#
#         print("合并后的总页数:%d."%outputPages)
        # 写入到目标PDF文件
        # outputStream = open(os.path.join(filepath,outfile), "wb")
        # output.write(outputStream)
        # outputStream.close()
        # print("PDF文件合并完成！")
    #
    # else:
    #     print("没有可以合并的PDF文件！")



if __name__ == "__main__":
    output = PdfFileWriter()
    outputPages = 0

    # file_dir = os.getcwd()
    time1 = time.time()
    doc_files = []
    outfile = "combo4.pdf"
    time2 = time.time()
    # dirs = os.listdir(path)
    path = r"I:\临时文件3.0\411722216204JC00492司二广"


    # filelist =os.listdir(path)
    #
    # for file in filelist:
    #     path1 = os.path.join(path,file)
    #
    #
    #     if os.path.isdir(path1):
    #        filelist1 = os.listdir(path1)
    #        # print(filelist1)
    #        # for file in filelist1:
    #        #    path2 = os.path.join(path1, file)
    #        #
    #        #    print('-----')
    #
    #
    #        # if os.path.isfile(path2):
    pdf_lst = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.pdf')]
    pdf_lst.sort()
    # pdf_lst = [os.path.join(path, filename) for filename in pdf_lst]
    print(pdf_lst)
    file_merger = PdfFileMerger()
    for pdf in pdf_lst:
                            # print(pdf)
        file_merger.append(PyPDF4.PdfFileReader(pdf))  # 合并pdf文件
        # #
        file_merger.write(os.path.join(path, outfile))

    # filelist1 = os.listdir(path)
    #
    # bianlifolder()
    #      for d in dirs:
    #          file_list = [f for f in os.listdir(os.path.join(root,d)) if f.endswith('.pdf')]
    #          file_list = [os.path.join(root,d, filename) for filename in file_list]
    #
    #          MergePDF(file_dir, outfile)
    #          outputStream = open(os.path.join(root,d, outfile), "wb")
    #          output.write(outputStream)
    #          outputStream.close()
    #          print("PDF文件合并完成！")
    #         file_merger = PdfFileMerger()
    #         for pdf in pdf_lst:
    #             # print(pdf)
    #             file_merger.append(pdf)  # 合并pdf文件
    #
    #             file_merger.write(os.path.join(root, d, out))
    #         # if file.endswith(".doc") or file.endswith(".docx"):
          # print(d)
        #     doc2pdf(str(root + "\\" + file))
