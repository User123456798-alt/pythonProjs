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

account_router = APIRouter()
app.include_router(account_router,prefix="/account",tags=["account"])

@account_router.post("/create")
def callCreateAccount(name:str,type:str,start:int):
    return account.createAccount(name,type,start)