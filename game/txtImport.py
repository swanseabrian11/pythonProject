
# 取出每一行的内容
def read_english_passage():
    passage_list = []
    with open('english.txt', 'r') as e_f:
        for index, line in enumerate(e_f.readlines()):
            print(index, line)
            passage_list.append(line.lower())


    return passage_list

# 从第一行取出每一句的内容
def get_english_sentence_list():
    passage_list = read_english_passage()
    sentence_list = []
    # 以.为分割符取句子放到数组中
    for section in passage_list:

        sentence_list = sentence_list + section.split('.')
        print(sentence_list[1])
        sentenec = sentence_list[1]
        print(len(sentenec))


    # 对数组中的的句子做处理
    # for index, sentence in enumerate(sentence_list):
    #     print(index, sentence)
    #     sentence_list[index] = sentence_list[index].strip()
    #     sentence_list[index] = sentence_list[index].replace('\n', '')
    #     if sentence_list[index] == '':
    #         sentence_list.remove(sentence_list[index])
    #         print(sentence + "XXXX", index)


if __name__ == '__main__':
    # read_english_passage()


    get_english_sentence_list()