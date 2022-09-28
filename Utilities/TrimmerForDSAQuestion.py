import json

file = open("C:\ParthProgrammes\DSA.txt", "r", encoding="utf-8")
obj = json.load(file)
file.close()

arraylist = []
for item in obj:
    if(item['Topic:'] == 'Bit Manipulation'):
        arraylist.append(item['URL'])
for i in arraylist:
    print(i)
