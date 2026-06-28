from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_orders():
    return []

@router.delete("/{id}")
def delete_order(id: int):
    return {"deleted": id}
