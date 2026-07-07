import util as util
from datetime import date
import os

def hasAccOfType(custId:str,type:str):
    with open("data/account.txt","r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(',')
        if line[3] == custId:
            if line[1] == type:
                return line
    return False

def createAccount(name:str,type:str,start:int):
    accNo = str(000000000000 + util.createId("data/account.txt"))
    custId = str(util.getId("data/customer.txt",name))
    if os.path.getsize("data/account.txt") != 0:
        acc = hasAccOfType(custId,type)
        if(acc == False):
            file = open("data/statements/statement_{accNo}.txt","w")
            file.write("created on: "+str(date.today()))
            file.close()
            with open ("data/account.txt","a") as f:
                f.seek(0,2)
                finLines = "\n"+accNo + "," + type + "," + int(start) + "," + custId
                f.write(finLines)
        else:
            prevBalance = acc[2]
            acc[2] = str(int(acc[2])+start)
            util.replaceItem("data/account.txt",acc)
            with open("data/statements/statement_{accNo}.txt","a"):
                f.seek(0,2)
                finLines = "\n"+str(date.today()) + "," + prevBalance + "," + str(start) + "," + 0 + "," + acc[2]
                f.write(finLines)
    else:
        with open ("data/account.txt","w") as f:
            f.write("\n"+accNo + "," + type + "," + int(start) + "," + custId)
    return{
    "name": name,
    "acc_type": type,
    "initial_deposit": start
    }