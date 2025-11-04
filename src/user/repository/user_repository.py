from typing import Optional, Dict
from common.models import User
from common.interfaces import UserRepo

class SimpleUserRepository(UserRepo):
    def __init__(self):
        # Проста "база даних" у пам'яті - словник
        self._users: Dict[str, User] = {}
        
        # Додаємо тестового користувача для прикладу
        test_user = User(
            id="user_1",
            email="admin@example.com", 
            password_hash="hash123",
            is_active=True
        )
        self._users[test_user.id] = test_user
        
    def get(self, user_id: str) -> Optional[User]:
        # Знайти користувача по ID
        return self._users.get(user_id)
    
    def get_by_email(self, email: str) -> Optional[User]:
        # Знайти користувача по email
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def update(self, user: User) -> None:
        # Оновити користувача
        self._users[user.id] = user