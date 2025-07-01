from dataclasses import dataclass
from typing import Optional


@dataclass
class post:
    id
    user_id: str = ""
    title: str = ""
    content: str = ""
    word_count: str = ""
    status: Optional[str] =None
    scheduled: Optional[str] =None
    created_at:Optional[str]= None
    tone_id:Optional[str]=None
  
