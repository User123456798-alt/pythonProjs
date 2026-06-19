from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

app = FastAPI()
finace_router = APIRouter()
app.include_router(finace_router,prefix="/finance",tags=["finance"])

@finace_router.get("/emi")
def calculateEMI(P:int,N:int,R:float):
    try:
        R = R/(12*100)
        return (P*R*(1 + R)**N)/((1 + R)**N - 1)
    except Exception as e:
        return {
            "error_message":str(e)
        }

class Items(BaseModel):
    name:str
    price: int
    quantity: int

class Bill(BaseModel):
    customer: str
    items: list[Items]

@finace_router.post("/bill")
def bill(bills:Bill):
    total = 0
    allItems = 0
    for item in bills.items:
        total += item.price * item.quantity
        allItems+= item.quantity
    return {
        "customer":bills.customer,
        "total_bill":total,
        "total_items":allItems
    }


student_router = APIRouter()
app.include_router(student_router,prefix="/student",tags=["student"])

class Student(BaseModel):
    name:str
    english:int
    maths:int
    science:int


@student_router.post("/student")
def newStudent(student:Student):
    total = student.english+student.maths+student.science
    return {
        "total":total,
        "average":total/3,
        "grade":assignGrade(total/3)
    }


def assignGrade(grade:float):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    

password_router = APIRouter()
app.include_router(password_router,prefix="/password",tags=["password"])

@password_router.get("/password")
def strenghtCheck(password:str):
    upper,lower,digit,special = False,False,False,False
    specialCh = ["@","#","$","%","&","*"]
    missing = ["short","no uppercase","no lowercase","no digit","no special charecter"]
    if len(password)>=8:
        missing.remove("short")
    for ch in password:
        if not upper and ch.isupper():
            upper = True
            missing.remove("no uppercase")
        elif not lower and ch.islower():
            lower = True
            missing.remove("no lowercase")
        elif not digit and ch.isdigit():
            digit = True
            missing.remove("no digit")
        elif not special and ch in specialCh:
            special = True
            missing.remove("no special charecter")
    if not missing:
        return{
            "strenght":"Strong"
        }
    else:
        return{
            "strenght":"Weak",
            "missing":missing
        }


price_router = APIRouter()
app.include_router(price_router,prefix="/price",tags=["price"])

@price_router.get("/bill")
def calcBill(baseP:int,disc:int):
    return{
        "original_price":baseP,
        "discount_percentage":disc,
        "discount_amount": baseP*(disc/100),
        "price_after_discount": baseP - (baseP*(disc/100)),
        "gst":(baseP - (baseP*(disc/100)))*.18,
        "final_amount":((baseP - (baseP*(disc/100)))*.18)+(baseP - (baseP*(disc/100)))
    }


number_router = APIRouter()
app.include_router(number_router,prefix="/number",tags=["number"])

@number_router.get("/analyse")
def numAnylisis(num:int):
    even = False
    prime = True 
    square = False
    digits = len(str(abs(num)))
    factors = []
    if num%2 == 0:
        even = True
    for i in range(1,num+1):
        if (num%i) == 0:
            factors.append(i)
            if i != 1 and i != num:
                prime = False
            if num/i == i:
                square = True
    return{
        "number":num,
        "even":even,
        "prime":prime,
        "perfect_square":square,
        "digits":digits,
        "factors":factors
    }


salary_router = APIRouter()
app.include_router(salary_router,prefix="/salary",tags=["salary"])

@salary_router.get("/salary")
def salaryCalc(name:str,basic:int):
    return{
        "employee":name,
        "basic_salary": basic,
        "hra": basic*.2,
        "da": basic*.1,
        "gross_salary": basic + (basic*.2) + (basic*.1),
        "tax": (basic + (basic*.2) + (basic*.1))*.05,
        "net_salary": (basic + (basic*.2) + (basic*.1))-((basic + (basic*.2) + (basic*.1))*.05)
    }


electric_router = APIRouter()
app.include_router(electric_router,prefix="/electric",tags=["electric"])

@electric_router.get("/bill")
def calcElectric(units:int):
    origUnits = units
    total = 0
    if units > 200:
        total += (units - 200) *8
        units = 200
    if units > 100:
        total += (units - 100) *5
        units = 100
    total+= units * 3
    return{
        "units": origUnits,
        "bill_amount": total
    }

