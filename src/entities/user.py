from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id
    name: str = ""
    email: str = ""
    password_hash: str = ""
    signup_method: str = ""
    created_at: Optional[str] =None
    updated_at: Optional[str] =None
  
