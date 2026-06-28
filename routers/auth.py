from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login Successful"}

@router.post("/signup")
def signup():
    return {"message": "Signup Successful"}
