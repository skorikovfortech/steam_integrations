from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import AsyncSessionDeps
from app.users.repo import UserRepo
from app.users.schemas import UserCreate, GetByEmailSchema, GetByUsername
from fastapi import Depends, HTTPException, status 
from typing import Annotated
import argon2 


ph = argon2.PasswordHasher()


class UserService:

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = UserRepo(session)
        

    async def create_user(self, data: UserCreate):
        check_email = await self.repo.get_user_by_email(email=data.email)
        check_username = await self.repo.get_user_by_username(username=data.username)
        if check_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with this email already exists")
        if check_username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username already exists")
        
        hash_password = self.hash_password(data.password)
        return await self.repo.create_user(
            email=data.email,
            password_hash=hash_password,
            username=data.username
        )

    async def get_user_by_username(self, data: GetByUsername):
        return await self.repo.get_user_by_username(**data.model_dump())
            
    

    async def get_user_by_email(self, data: GetByEmailSchema):
        return await self.repo.get_user_by_email(**data.model_dump())


    async def delete_user(self, data: GetByEmailSchema):
        return await self.repo.delete_users(**data.model_dump())
    

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