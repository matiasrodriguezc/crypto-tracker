from pydantic import BaseModel
from datetime import datetime

class PriceBase(BaseModel):
    price: float
    timestamp: datetime

    class Config:
        orm_mode = True