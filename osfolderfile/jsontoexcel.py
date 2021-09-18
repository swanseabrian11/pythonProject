import json

file = open(r"C:\Users\Administrator\Desktop\/vbs\python\jsonsavetoexcel\cowtransfer\/1-311_json\叽呤成都站1-311_json\/1.json",'r', encoding='utf-8')
json_data = json.load(file)
print(json_data)