from fastapi import APIRouter, Depends, requests
from app.core.db import AsyncSessionDeps
from app.users.service import UserServiceDeps
from app.users.schemas import UserCreate, GetByEmailSchema, UserReadSchema

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/")
async def create_user(
    user_service: UserServiceDeps,
    data: UserCreate
):
    await user_service.create_user(data=data)
    return "thank you for registration"


@user_router.get("/", response_model=UserReadSchema)
async def get_user_by_email(
    user_service: UserServiceDeps,
    data: GetByEmailSchema = Depends(),
    
):
    user = await user_service.get_user_by_email(data=data)
    return user