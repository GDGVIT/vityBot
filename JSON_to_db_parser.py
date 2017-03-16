import json
import os

listOfDicts = []

directoryList = os.listdir("./testjsonfolder")

for file in directoryList:
    with open("./testjsonfolder/"+file) as json_data:
        loader = json.load(json_data)
    listOfDicts.append(loader)

for each in listOfDicts:
    print(each)
