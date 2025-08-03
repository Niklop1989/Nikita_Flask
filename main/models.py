
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declarative_base, relationship
from sqlalchemy import Column, Identity
from sqlalchemy import Integer, String, Date,ARRAY, ForeignKey,Float
from typing import Dict, Any, List
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(200),nullable=True)
    price: Mapped[float] = mapped_column(Float,nullable=True)
    user_id: Mapped[int] = mapped_column(Integer,ForeignKey('users.id'))
    #
    user = relationship('User',backref='products')

    def __repr__(self):
        return (f"Product id={self.id}, title={self.title},"
                f"price={self.price},descr={self.description}")

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    second_name:Mapped[str] = mapped_column(String(50),nullable=True)
    birth_date:Mapped[Date] = mapped_column(Date,nullable=True)
    age: Mapped[int] = mapped_column(Integer)
    address: Mapped[str] = mapped_column(String(200))
    country: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return (f"User id={self.id}, name={self.first_name},"
                f"age={self.age},address={self.address},country={self.country}")

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
