import util as util
from datetime import date
import os

def createStaff(name:str,mobile:int,email:str,role:str,dob:str):
    if util.isDuplicate(email,"data/staff.txt",3):
        return{
            "status":False,
            "reason":"duplicate email"
        }
    if util.isDuplicate(mobile,"data/staff.txt",2):
        return{
            "status":False,
            "reason":"duplicate mobile"
        }
    roleId = util.getId("data/role.txt",role)
    if roleId == -1:
        return {
            "status":False,
            "reason":"role not found: " + role
        }
    doj = date.today()
    with open("data/staff.txt","r+") as f:
        lines = f.readlines()
        Ids = []
        for line in lines:
            line = line.split(",")
            Ids.append(int(line[0]))
        staffId = 1 + len(Ids)
        while staffId in Ids:
            staffId+=1
        staffId = util.createId("data/staff.txt")
        staff = "\n" + str(staffId) + "," + name + "," + str(mobile) + "," + email  + "," + dob  + "," + str(doj)  + "," + str(roleId)
        f.write(staff)
    return{
        "name": name,
        "mobile": mobile,
        "email": email,
        "role": role,
        "dob": dob
    }

def updateStaff(name:str,mobile:int,email:str,role:str):
    if util.isDuplicate(email,"data/staff.txt",3):
        return{
            "status":False,
            "reason":"duplicate email"
        }
    if util.isDuplicate(mobile,"data/staff.txt",2):
        return{
            "status":False,
            "reason":"duplicate mobile"
        }
    prevStaff = util.findStaff(name)
    if prevStaff == -1:
        return {
            "status":False,
            "reason":"staff member not found"
        }
    if mobile == 0:
        if email == "":
            if role == "":
                return {
                    "status":False,
                    "reason":"no fields modified"
                }
            else:
                prevStaff["role"] = role
        else:
            prevStaff["email"] = email
            if role != "":
                prevStaff["role"] = role
    else:
        if email == "":
            if role == "":
                prevStaff["mobile"] = mobile
            else:
                prevStaff["role"] = role
        else:
            prevStaff["email"] = email
            if role != "":
                prevStaff["role"] = role
    util.replaceStaff(prevStaff)    

def deleteStaff(name:str):
    finLines = ""
    prevStaff = []
    with open("data/staff.txt","r+") as f:
        f.seek(0)
        lines = f.readlines()
        notFound = True
        for line in lines:
            if notFound:
                lineS = line.split(",")
                if lineS[1] == name:
                    prevStaff = lineS
                    notFound = False
                    continue
            finLines = finLines + line + "\n"
    finlines = finLines[:-1]
    with open("data/staff.txt","w") as f:
        f.writelines(finLines)
    with open("data/dump.txt","a") as f:
        f.seek(0,2)
        f.write("\n")
        f.write("staff:")
        for i in prevStaff:
            f.write(i + ",")
        f.write(str(date.today()))
    return{
        "name": line[1],
        "mobile": line[2],
        "email": line[3],
        "doj": line[5],
        "role": line[6],
        "deleted_on": date.today()
    }

def fetchStaff(name:str):
    staff = util.findStaff(name)
    if staff == -1:
        return{
            "status":False,
            "reason":"staff member not found"
        }
    return{
        "Id":staff["Id"],
        "Name":staff["name"],
        "Number":staff["mobile"],
        "Email":staff["email"],
        "dob":staff["dob"],
        "doj":staff["doj"],
        "RoleId":staff["roleId"]
    }