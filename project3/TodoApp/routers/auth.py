from fastapi import APIRouter
from pydantic import BaseModel
from models import Users
from starlette import status
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "JohnDoe",
                "email": "john.doe@email.com",
                "first_name": "John",
                "last_name": "Doe",
                "password": "password123",
                "role": "admin"
            }
        }
    }


@router.post("/auth", status_code=status.HTTP_200_OK)
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    return create_user_model
