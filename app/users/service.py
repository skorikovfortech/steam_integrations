from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionDeps
from app.users.repo import UserRepo
from app.users.schemas import UserCreate, GetByEmailSchema
from fastapi import Depends, HTTPException, status 
from typing import Annotated
import argon2 


ph = argon2.PasswordHasher()


class UserService:

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = UserRepo(session)
        

    async def create_user(self, data: UserCreate):
        check_user = await self.repo.get_user_by_email(email=data.email)
        if check_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with this email already exists")
        
        hash_password = self.hash_password(data.password)
        return await self.repo.create_user(
            email=data.email,
            password_hash=hash_password,
            username=data.username
        )
    

    async def get_user_by_email(self, data: GetByEmailSchema):
        return await self.repo.get_user_by_email(**data.model_dump())

    
    @staticmethod
    def hash_password(password: str) -> str:
        hash_password = ph.hash(password=password)
        return hash_password
    

    @staticmethod
    def verify_password(hash_password: str, password: str) -> bool:
        return ph.verify(hash_password, password)
    
    
    


def get_user_service(session: AsyncSessionDeps) -> UserService:
    return UserService(session=session)



UserServiceDeps = Annotated[UserService, Depends(get_user_service)]