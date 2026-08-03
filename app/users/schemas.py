from pydantic import BaseModel, ConfigDict, EmailStr


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

class UserCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    username: str | None = None

class GetByUsername(BaseModel):
    username: str