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
        if not os.path.isdir("statements"):
            os.makedirs("statements");
        with open ("data/account.txt","w") as f:
            f.write("\n"+accNo + "," + type + "," + int(start) + "," + custId)
    return{
    "name": name,
    "acc_type": type,
    "initial_deposit": start
    }

def deleteAccount(name:str,type:str):
    custNum = util.findItem("data/customer.txt",name)[0]
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    prev = ""
    for line in lines:
        lineS= line.split(",")
        if lineS[3] == custNum:
            if lineS[1] == type:
                accNo = lineS[0]
                prev = lineS[2]
                os.rename("data/statements/statement_{accNo}.txt", "data/removed_accounts/statement_{accNo}.txt")
                with open("data/dump.txt","a") as f:
                    f.seek(0,2)
                    f.write("\n")
                    f.write("account:")
                    for i in lineS:
                        f.write(i + ",")
                    f.write(str(date.today()))
                continue
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)
    return{
        "refund_amount":int(prev)
    }

def deleteAccount(acc:int):
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    prev = ""
    for line in lines:
        lineS= line.split(",")
        if lineS[0] == str(acc):
            prev = lineS[2]
            os.rename("data/statements/statement_{acc}.txt", "data/removed_accounts/statement_{acc}.txt")
            with open("data/dump.txt","a") as f:
                f.seek(0,2)
                f.write("\n")
                f.write("account:")
                for i in lineS:
                    f.write(i + ",")
                f.write(str(date.today()))
            continue
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)
    return{
        "refund_amount":int(prev)
    }
    
def deposit(name:str,type:str,amount:int):
    if amount < 0:
        return{
            "status":False,
            "message":"deposit amount too low"
        }
    custNum = util.findItem("data/customer.txt",name)[0]
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    for line in lines:
        lineS= line.split(",")
        if lineS[3] == custNum:
            if lineS[1] == type:
                accNo = lineS[0]
                prevBalance = lineS[2]
                lineS[2] = str(int(lineS[2]) + amount)
                util.replaceItem("data/account.txt",lineS)
                with open("data/statements/statement_{accNo}.txt","a"):
                    f.seek(0,2)
                    finLines = "\n"+str(date.today()) + "," + prevBalance + "," + "deposit" + "," + lineS[2]
                    f.write(finLines)
                line = lineS[0] + "," + lineS[1] + "," + lineS[2] + "," + lineS[3]
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)
                
def deposit(acc:int,amount:int):
    if amount < 0:
        return{
            "status":False,
            "message":"deposit amount too low"
        }
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    for line in lines:
        lineS= line.split(",")
        if lineS[0] == str(acc):
            accNo = lineS[0]
            prevBalance = lineS[2]
            lineS[2] = str(int(lineS[2]) + amount)
            util.replaceItem("data/account.txt",lineS)
            with open("data/statements/statement_{accNo}.txt","a"):
                f.seek(0,2)
                finLines = "\n"+str(date.today()) + "," + prevBalance + "," + "deposit" + "," + lineS[2]
                f.write(finLines)
            line = lineS[0] + "," + lineS[1] + "," + lineS[2] + "," + lineS[3]
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)

def withdraw(name:str,type:str,amount:int):
    if amount < 0:
        return{
            "status":False,
            "message":"withdrawal amount too low"
        }
    custNum = util.findItem("data/customer.txt",name)[0]
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    for line in lines:
        lineS= line.split(",")
        if lineS[3] == custNum:
            if lineS[1] == type:
                accNo = lineS[0]
                prevBalance = lineS[2]
                if int(lineS[2]) < amount:
                    return{
                    "status":False,
                    "message":"insuficiant balance"
                    }
                lineS[2] = str(int(lineS[2]) - amount)
                util.replaceItem("data/account.txt",lineS)
                with open("data/statements/statement_{accNo}.txt","a"):
                    f.seek(0,2)
                    finLines = "\n"+str(date.today()) + "," + prevBalance + "," + "withdrawal" + "," + lineS[2]
                    f.write(finLines)
                line = lineS[0] + "," + lineS[1] + "," + lineS[2] + "," + lineS[3]
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)
                
def withdraw(acc:int,amount:int):
    if amount < 0:
        return{
            "status":False,
            "message":"withdrawal amount too low"
        }
    lines = ""
    with open("data/accounts.txt","r")as f:
        lines = f.readlines()
    newLines =""
    for line in lines:
        lineS= line.split(",")
        if lineS[0] == str(acc):
            accNo = lineS[0]
            prevBalance = lineS[2]
            if int(lineS[2]) < amount:
                return{
                "status":False,
                "message":"insuficiant balance"
                }
            lineS[2] = str(int(lineS[2]) - amount)
            util.replaceItem("data/account.txt",lineS)
            with open("data/statements/statement_{accNo}.txt","a"):
                f.seek(0,2)
                finLines = "\n"+str(date.today()) + "," + prevBalance + "," + "withdrawal" + "," + lineS[2]
                f.write(finLines)
            line = lineS[0] + "," + lineS[1] + "," + lineS[2] + "," + lineS[3]
        newLines = newLines + line
    newLines = newLines[:-1]
    with open("data/accounts.txt","w") as f:
        f.writelines(newLines)