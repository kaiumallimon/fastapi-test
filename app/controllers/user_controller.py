from fastapi import APIRouter, HTTPException
from app.models.user_model import User
from app.services.user_service import UserService

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    created_user = UserService.create_user(user.dict(exclude_unset=True))
    if not created_user:
        raise HTTPException(status_code=400, detail="User could not be created")
    return created_user

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = UserService.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users")
def list_users():
    if not UserService.get_all_users():
        raise HTTPException(status_code=404, detail="No users found")
    return UserService.get_all_users()

@router.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    updated_user = UserService.update_user(user_id, user.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found or not updated")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    deleted_user = UserService.delete_user(user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found or not deleted")
    return {"detail": "User deleted successfully"}
