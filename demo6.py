from pydantic import BaseModel
import requests
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# print(response.json())
#POST
# url = "https://jsonplaceholder.typicode.com/posts"
# payload = {
#     "title":"Python",
#     "body":"Learning APIs",
#     "userId":1
# }
# response = requests.post(url, json=payload)
# print(response.status_code)

# GET

# url = "https://jsonplaceholder.typicode.com/posts?userId=1"
# response = requests.get(url)
# print(response.json())

# def postUser(title:str,body:str,userId:int):
#     url = "https://jsonplaceholder.typicode.com/posts"
#     payload = {"title":title,"body":body,"userId":userId}
#     response = requests.post(url,json=payload)
#     print(response.status_code)
# postUser("a","rriheiofe",3)
# postUser("b","the quick brown fox jumped over the lazy dog",4)
# postUser("c","",5)

from fastapi import APIRouter, FastAPI

app = FastAPI()
api_router = APIRouter()
api_router1 = APIRouter()
app.include_router(api_router,prefix="/students")
app.include_router(api_router1,prefix="/empolyees",tags=["EMploye"])

@api_router.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

@api_router1.get("/")
def home():
    return {"message": "Welcome to FastAPI!2"}


@api_router.get("/hello")
def say_hello():
    return {"message": "Hello, User"}


@api_router.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "name": "John",
        "marks": 90
    }

class Student(BaseModel):
    id: int
    name: str
    marks: int

@api_router.post("/students")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "student": student
    }

@api_router.patch("/update")
def update_student(student: Student):
    return {
        "message": "Student Updated",
        "student": student
    }

@api_router.delete("/remove/{id}")
def remove_student(id:int):
    return{
        "message": "Student Removed"
    }