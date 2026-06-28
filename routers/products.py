from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_all_products():
    return [
        {
            "id": 1,
            "name": "Laptop",
            "price": 65000
        },
        {
            "id": 2,
            "name": "Keyboard",
            "price": 1500
        }
    ]

@router.get("/{id}")
def get_product(id: int):
    return {
        "id": id,
        "name": "Laptop",
        "price": 65000
    }
