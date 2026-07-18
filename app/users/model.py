from sqlalchemy.orm import Mapped, mapped_column
from app.core.base import Base
from pydantic import EmailStr
from datetime import datetime
from sqlalchemy import func

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str| None] = mapped_column(unique=True, nullable=True)
    password_hash: Mapped[str]
    steam_id: Mapped[str] = mapped_column(unique=True, nullable=True)
    trade_link: Mapped[str] = mapped_column(unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())



    