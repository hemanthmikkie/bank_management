from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionBase(BaseModel):
    customer_id: int
    transaction_type: str
    amount: float
    description: Optional[str] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionRead(TransactionBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
