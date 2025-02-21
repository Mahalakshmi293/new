import json

FILE="stud.json"

def read_json():
    with open(FILE) as f:
        return json.load(f)

def write_json(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=3)


# data=read_json()
# print(data["1"]["age"])