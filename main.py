from fastapi import FastAPI
from routers.products import router as productRouter

app = FastAPI()

app.include_router(
    productRouter,
    prefix="/products",
    tags=["Products"]
)

@app.get("/")
def home():
    return {
        "message": "Shopping API Running"
    }
