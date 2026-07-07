import os

def findStaff(name:str):
    staff = {"Id":"","name":"","mobile":0,"email":"","dob":"","doj":"","roleId":""}
    with open("data/staff.txt","r") as f:
        f.seek(0)
        for line in f.readlines():
            line = line.split(",")
            if line[1] == name:
                staff["Id"] = line[0]
                staff["name"] = line[1]
                staff["mobile"] = int(line[2])
                staff["email"] = line[3]
                staff["dob"] = line[4]
                staff["doj"] = line[5]
                staff["roleId"] = line[6]
                break
    if staff["name"] == "":
        return -1
    return staff

def replaceStaff(replace:dict):
        newLines = ""
        with open("data/staff.txt","r+") as f:
            f.seek(0)
            lines = f.readlines()
            for line in lines:
                lineS = line.split(",")
                if lineS[1] == replace["name"]:
                    newStaff = ""
                    for i,v in replace.items():
                        if i == "Id":
                            newStaff = "\n" + str(v)
                        else:
                            newStaff = newStaff + "," +str(v)
                line = newStaff
                newLines = newLines + line + "\n"
            newLines = newLines[:-1]
        with open("staff.txt","w") as f:
            f.writelines(newLines)

def getId(file:str,item:str):
    found = False
    print(os.getcwd())
    with open(file,"r") as f:
        for line in f.readlines():
            sLine = line.split(",")
            if sLine[1] == item:
                found = True
                return int(sLine[0])
    if not found:
        return -1
    
def getRoleById(Id:int):
    found = False
    print(os.getcwd())
    with open("data/role.txt","r") as f:
        for line in f.readlines():
            sLine = line.split(",")
            if int(sLine[0]) == Id:
                found = True
                return sLine[1]
    if not found:
        return -1
    
def isDuplicate(value:str,file:str,position:int):
    with open(file,"r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(',')
            if line[position] == value:
                return True
        return False
    
def createId(file:str):
    with open(file,"r+") as f:
        f.seek(0,0)
        lines = f.readlines()
        Ids = []
        for line in lines:
            line = line.split(",")
            cleaned = [s.lstrip("0") for s in line[0]]
            Ids.append(int(cleaned))
        newId = 1 + len(Ids)
        while newId in Ids:
            newId+=1
        return newId
    
def findRole(name:str):
    role = {"Id":"","name":"","salary":"","under":""}
    with open("data/role.txt","r") as f:
        f.seek(0)
        for line in f.readlines():
            line = line.split(",")
            if line[1] == name:
                role["Id"] = line[0]
                role["name"] = line[1]
                role["salary"] = line[2]
                role["under"] = line[3]
                break
    if role["name"] == "":
        return -1
    return role

def replaceRole(replace:dict):
        newLines = ""
        lines = ""
        with open("data/role.txt","r") as f:
            f.seek(0,0)
            lines = f.readlines()
        for line in lines:
            lineS = line.split(",")
            if lineS[0] == replace["Id"]:
                newRole = ""
                for i,v in replace.items():
                    if i == "Id":
                        newRole = v
                    else:
                        newRole = newRole + "," + v
                line = newRole
            newLines = newLines + line
        with open("data/role.txt","w") as f:
            f.writelines(newLines)

def findItem(file:str,name:str):
    item = []
    with open(file,"r") as f:
        f.seek(0)
        for line in f.readlines():
            line = line.split(",")
            if line[1] == name:
                for data in line:
                    item.append(data)
                break
    if item[0] == "":
        return -1
    return item

def replaceItem(file:str,item:list):
        newLines = ""
        lines = ""
        with open(file,"r") as f:
            f.seek(0,0)
            lines = f.readlines()
        for line in lines:
            lineS = line.split(",")
            if lineS[0] == item[0]:
                newRole = ""
                for i in len(item):
                    if i == 0:
                        newRole = item[i]
                    else:
                        newRole = newRole + "," + item[i]
                line = newRole
            newLines = newLines + line
        with open(file,"w") as f:
            f.writelines(newLines)