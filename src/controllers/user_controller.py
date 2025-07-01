from fastapi import APIRouter,FastAPI
from ..services.user_service import UserService

router = APIRouter()

# service=UserService
@router.post("/users/create")
def create_user():
    service=UserService()
    pass