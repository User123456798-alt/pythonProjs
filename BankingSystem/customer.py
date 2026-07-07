from datetime import date
import os

import util as util

def createCustomer(name:str,mobile:str,email:str,dob:str):
    id = 00000000 + util.createId("data/customer.txt")
    doj = date.today()
    if os.path.getsize("data/customer.txt") != 0:
        with open ("data/customer.txt","a") as f:
            f.seek(0,2)
            finLines = "\n"+str(id) + "," + name + "," + mobile + "," + email + "," + dob + "," + doj
            f.write(finLines)
    else:
        with open ("data/customer.txt","w") as f:
            f.write("\n"+str(id) + "," + name + "," + mobile + "," + email + "," + dob + "," + doj)
    return {
        "name": name,
        "mobile": mobile,
        "email": email,
        "dob": doj
    }

def updateCustomer(name:str,mobile:str,email,str):
    customer = util.findItem("data/customer.txt",name)
    if customer == -1:
        return{
            "status":False,
            "reason":"customer not found"
        }
    if mobile == customer[2]:
        return{
            "status":False,
            "reason":"duplicate mobile"
        }
    if email == customer[3]:
        return{
            "status":False,
            "reason":"duplicate email"
        }
    if mobile == "":
        if email == "":
            return {
                    "status":False,
                    "reason":"no fields modified"
                }
        else:
            customer[3] == email
    else:
        customer[2] == mobile
        if email != "":
            customer[3] == email
    util.replaceItem("data/customer.txt",customer)

def removeCustomers(name:str):
    if not os.path.isdir("removed_customers"):
        os.makedirs("removed_customers");
    finLines = ""
    prevCustomer = []
    with open("data/customer.txt","r+") as f:
        f.seek(0)
        lines = f.readlines()
        notFound = True
        for line in lines:
            if notFound:
                lineS = line.split(",")
                if lineS[1] == name:
                    prevCustomer = lineS
                    notFound = False
                    continue
            finLines = finLines + line + "\n"
    finlines = finLines[:-1]
    with open("data/customer.txt","w") as f:
        f.writelines(finLines)
    with open("data/dump.txt","a") as f:
        f.seek(0,2)
        f.write("\n")
        f.write("customer:")
        for i in prevCustomer:
            f.write(i + ",")
        f.write(str(date.today()))
    return{
        "name": line[1],
        "mobile": line[2],
        "email": line[3],
        "dob": line[5],
        "doj": line[6],
        "deleted_on": date.today()
    }

def findCustomer(name:str):
    customer = util.findItem("data/customer.txt",name)
    if customer == -1:
        return{
            "status":False,
            "reason":"customer not found"
        }
    return{
        "name":customer[1],
        "mobile":customer[2],
        "email":customer[3],
        "dob":customer[4],
        "doj":customer[5]
    }