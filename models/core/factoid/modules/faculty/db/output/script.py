import os
import json

files = os.listdir(os.curdir)[:-2]

json_list = list()

for file in files:
	with open(file) as f:
		print(file)
		d = json.load(f)
		json_list.append(d)

with open('data.json', 'w') as f:
	json.dump(json_list, f, indent=4)