from fastapi import APIRouter, FastAPI
import staff as staff
import customer as customer
import account as account
import role as role
import util as util
import os

if not os.path.isfile("data/accounts.txt"):
    file = open("data/accounts.txt","w")
    file.close()
if not os.path.isfile("data/customer.txt"):
    file = open("data/customer.txt","w")
    file.close()
if not os.path.isfile("data/dump.txt"):
    file = open("data/dump.txt","w")
    file.close()
if not os.path.isfile("data/role.txt"):
    file = open("data/role.txt","w")
    file.close()
if not os.path.isfile("data/staff.txt"):
    file = open("data/staff.txt","w")
    file.close()

app = FastAPI()

staff_router = APIRouter()
app.include_router(staff_router,prefix="/staff",tags=["staff"])

@staff_router.post("/create")
def callCreateStaff(name:str,mobile:int,email:str,role:str,dob:str):
    return staff.createStaff(name,mobile,email,role,dob)

@staff_router.get("/fetch/{name}")
def callFetchStaff(name:str):
    return staff.fetchStaff(name)

@staff_router.put("/update")
def callUpdateStaff(name:str,mobile=0,email="",role=""):
    return staff.updateStaff(name,mobile,email,role)

@staff_router.delete("/delete")
def callDeleteStaff(name:str):
    return staff.deleteStaff(name)

role_router = APIRouter()
app.include_router(role_router,prefix="/role",tags=["role"])

@role_router.post("/create")
def callCreateRole(name:str,salary:int,under:str=""):
    return role.createRole(name,salary,under)

@role_router.put("/update")
def callUpdateRole(name:str,salary="",under=""):
    return role.updateRole(name,salary,under)

@role_router.delete("/delete")
def callDeleteRole(name:str):
    return role.deleteRole(name)

@role_router.get("/fetch/{name}")
def callRoleFetch(name:str):
    return role.fetchRole(name)

customer_router = APIRouter()
app.include_router(customer_router,prefix="/customer",tags=["customer"])

@customer_router.post("/create")
def callCreateCustomer(name:str,mobile:str,email:str,dob:str):
    return customer.createCustomer(name,mobile,email,dob)

@customer_router.put("/update")
def callUpdateCustomer(name:str,mobile="",email=""):
    return customer.updateCustomer(name,mobile,email)

@customer_router.delete("/delete")
def callDeleteCustomer(name:str):
    return customer.removeCustomers(name)

account_router = APIRouter()
app.include_router(account_router,prefix="/account",tags=["account"])

@account_router.post("/create")
def callCreateAccount(name:str,type:str,start:int):
    return account.createAccount(name,type,start)

@account_router.put("/deposit")
def callDeposit(amount:int,name="",type="",acc=0):
    if acc!=0:
        return account.deposit(acc,amount)
    elif name != "" and type != "":
        return account.deposit(name,type,amount)
    else:
        return{
            "status":False,
            "message":"not enough parameters"
        }
    
@account_router.put("/delete")
def callDeleteAccount(name="",type="",acc=0):
    if acc!=0:
        return account.deleteAccount(acc)
    elif name != "" and type != "":
        return account.deleteAccount(name,type)
    else:
        return{
            "status":False,
            "message":"not enough parameters"
        }
    
@account_router.put("/withdraw")
def callWithdraw(amount:int,name="",type="",acc=0):
    if acc!=0:
        return account.withdraw(acc,amount)
    elif name != "" and type != "":
        return account.withdraw(name,type,amount)
    else:
        return{
            "status":False,
            "message":"not enough parameters"
        }
    
@account_router.put("/deposit")
def callWithdraw(amount:int,name="",type="",acc=0):
    if acc!=0:
        return account.deposit(acc,amount)
    elif name != "" and type != "":
        return account.deposit(name,type,amount)
    else:
        return{
            "status":False,
            "message":"not enough parameters"
        }
    
def main():
    cmd = -1
    cmd2 = -1
    while(cmd!=0):
        print("Welcome to G10X Banking System\nChoose your category:\n1. Staff\n2. Role\n3. Customer\n0. Quit")
        cmd = input()
        match cmd:
            case 1:
                print("1. Get Staff Details\n2. Add Staff\n3. Update Staff\n4. Delete Staff")
                cmd2 = input()
                match cmd2:
                    case 1:
                        print("enter id")
                        info = input()
                        staff.fetchStaff(info)
                        break
                    case 2:
                        print("enter staff info")
                        info = input()
                        info = info.split(",")
                        staff.createStaff(info[0],int(info[1]),info[2],info[3],info[4])
                        break
                    case 3:
                        staff.updateStaff()
                        break
                    case 4:
                        staff.deleteStaff()
                        break
                break
            case 2:
                print("1. Get Role Details\n2. Add Role\n3. Update Role\n4. Delete Role")
                cmd2 = input()
                match cmd2:
                    case 1:
                        role.fetchRole()
                        break
                    case 2:
                        role.createRole()
                        break
                    case 3:
                        role.updateRole()
                        break
                    case 4:
                        role.deleteRole()
                        break
                break
            case 3:
                print("1. Get Customer Details\n2. Add Customer\n3. Update Customer\n4. Delete Customer\n5. Deposit\n6. Withdraw")
                cmd2 = input()
                match cmd2:
                    case 1:
                        customer.findCustomer()
                        break
                    case 2:
                        customer.createCustomer()
                        break
                    case 3:
                        customer.updateCustomer()
                        break
                    case 4:
                        customer.removeCustomers()
                        break
                    case 5:
                        account.deposit()
                        break
                    case 6:
                        account.withdraw()
                        break
                break
            case 0:
                # Quit
                break