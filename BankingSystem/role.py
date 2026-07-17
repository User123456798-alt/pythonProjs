from datetime import date
import os

import util as util

def createRole(name:str,salary:int,under:str):
    if util.isDuplicate(name,"data/role.txt",1):
        return{
            "status":False,
            "reason":"duplicate role"
        }
    underId = -1
    if under == "":
        underId = 0
    else:
        underId = util.getId("data/role.txt",under)
    Id = util.createId("data/role.txt")
    lines = ""
    if os.path.getsize("data/role.txt") != 0:
        with open ("data/role.txt","a") as f:
            f.seek(0,2)
            finLines = "\n"+str(Id) + "," + name + "," + str(salary) + "," + str(underId)
            f.write(finLines)
    else:
        with open ("data/role.txt","w") as f:
            f.write(str(Id) + "," + name + "," + str(salary) + "," + str(underId))
    return{
        "designation": name,
        "Superior": under,
        "salary": salary
    }

def updateRole(name:str,salary:str,under:str):
    prevRole = util.findRole(name)
    if prevRole == -1:
        return {
            "status":False,
            "reason":"role not found"
                }
    if salary == "":
        if under == "":
            return {
                    "status":False,
                    "reason":"no fields modified"
                }
        else:
            prevRole["under"] = str(util.getId("data/role.txt",under)) + "\n"
    else:
        prevRole["salary"] = salary
        if under != "":
            prevRole["under"] =  str(util.getId("data/role.txt",under))+ "\n"
    util.replaceRole(prevRole)

def deleteRole(name:str):
    finLines = ""
    prevRole = []
    with open("data/role.txt","r+") as f:
        f.seek(0)
        lines = f.readlines()
        notFound = True
        for line in lines:
            if notFound:
                lineS = line.split(",")
                if lineS[1] == name:
                    prevRole = lineS
                    notFound = False
                    continue
            finLines = finLines + line
    finlines = finLines[:-1]
    with open("data/role.txt","w") as f:
        f.writelines(finLines)
    with open("data/dump.txt","a") as f:
        f.seek(0,2)
        f.write("\n")
        f.write("role:")
        for i in prevRole:
            f.write(i + ",")
        f.write(str(date.today()))
    return{
        "Designation": prevRole[1],
        "salary": prevRole[2],
        "Superior": util.getRoleById(prevRole[3][:-1]),
        "deleted_on": str(date.today())
    }

def fetchRole(name:str):
    role = util.findRole(name)
    if role == -1:
        return{
            "status":False,
            "reason":"role not found"
        }
    return{
        "Id":role["Id"],
        "Designation":role["name"],
        "Salary":role["salary"],
        "Superior":role["under"],
    }