from fastapi import APIRouter, FastAPI

app = FastAPI()
api_router = APIRouter()
app.include_router(api_router,prefix="/finance",tags=["finance"])

@api_router.get("/add")
def add(x:int,y:int):
    return {"result": x+y}