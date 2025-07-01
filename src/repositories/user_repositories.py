from supabase import create_client
import os
from ..entities.user import User


class UserRepository:
    def __init__(self):
        self.supabase=create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
    def create_user(self, user):
        
        result=self.supabase.table("users").insert(user).execute
        return result.data
        




