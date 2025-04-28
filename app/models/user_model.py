from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None