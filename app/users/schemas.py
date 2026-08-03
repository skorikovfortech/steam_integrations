from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email : EmailStr
    password: str
    username: str | None = None


class GetByEmailSchema(BaseModel):
    email: EmailStr


class UserReadSchema(BaseModel):
    email: EmailStr
    username: str | None = None
    is_active: bool
    is_admin: bool

class UserCreateResponce(BaseModel):
    email: EmailStr
    username: str