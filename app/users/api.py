from fastapi import APIRouter, Depends
from app.users.service import UserServiceDeps
from app.users.schemas import UserCreate, GetByEmailSchema, UserReadSchema, UserCreateResponse

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/", response_model=UserCreateResponse)
async def create_user(
    user_service: UserServiceDeps,
    data: UserCreate
):
    user = await user_service.create_user(data=data)
    return user


@user_router.get("/", response_model=UserReadSchema)
async def get_user_by_email(
    user_service: UserServiceDeps,
    data: GetByEmailSchema = Depends(),
    
):
    user = await user_service.get_user_by_email(data=data)
    return user

@user_router.delete("/", response_model=GetByEmailSchema)
async def delete_user(
    user_service: UserServiceDeps,
    data: GetByEmailSchema,
):
    await user_service.delete_user(data=data)
    return "user delete"