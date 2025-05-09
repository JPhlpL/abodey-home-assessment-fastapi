from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
    
class Contact(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    class Config:
        from_attributes = True
