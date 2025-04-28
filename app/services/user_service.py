import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class UserService:
    @staticmethod
    def create_user(user_data: dict):
        response = supabase.table("users").insert(user_data).execute()
        return response.data

    @staticmethod
    def get_user(user_id: int):
        response = supabase.table("users").select("*").eq("id", user_id).single().execute()
        return response.data

    @staticmethod
    def get_all_users():
        response = supabase.table("users").select("*").execute()
        return response.data

    @staticmethod
    def update_user(user_id: int, user_data: dict):
        response = supabase.table("users").update(user_data).eq("id", user_id).execute()
        return response.data

    @staticmethod
    def delete_user(user_id: int):
        response = supabase.table("users").delete().eq("id", user_id).execute()
        return response.data
