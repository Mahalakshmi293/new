from utils import*


def register(name,age,course,address):
    data=read_json()
    stud_json= {
        "name":name,
        "age":age,
        "course":course,
        "address":address
    }

    if len(data)==0:
        sno=1
    else:
        sno=str(int(list(data.keys())[-1])+1)
    data[sno]=stud_json
    write_json(data)
   
   
def update(id,name,age,course,address):
    data=read_json()
    data[id]["name"]=name
    data[id]["age"]=age
    data[id]["course"]=course
    data[id]["address"]=address
    write_json(data)

def delete(id):
    data=read_json()
    del data[id]
    write_json(data)



