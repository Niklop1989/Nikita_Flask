from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import date

class ProductBase(BaseModel):
    id: int
    title: str
    description: str
    price: float
    user_id:int


class ProductAddPost(ProductBase):
    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    id: int
    first_name: str
    second_name: str
    birth_date: date | None
    age: int
    address: str
    country: str


class UserAddPost(UserBase):
    model_config = ConfigDict(from_attributes=True)
