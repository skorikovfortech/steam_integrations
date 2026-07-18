from sqlalchemy import select, update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.users.model import User


class UserRepo:


    def __init__(self, session: AsyncSession):
        self.session = session


    async def create_user(self, email: str, password_hash: str, username: str | None = None):
        stmt = insert(User).values(email=email, password_hash=password_hash, username=username)
        return await self.session.execute(stmt)
    
    async def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()