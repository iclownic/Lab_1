from typing import Dict
from common.models import Cart, CartItem
from common.interfaces import CartRepo

class SimpleCartRepository(CartRepo):
    def __init__(self):
        # «бер≥гаЇмо кошики по user_id
        self._carts: Dict[str, Cart] = {}
    
    def get(self, user_id: str) -> Cart:
        # якщо кошика немаЇ - створюЇмо новий порожн≥й
        if user_id not in self._carts:
            self._carts[user_id] = Cart(user_id=user_id, items=[])
        return self._carts[user_id]
    
    def save(self, cart: Cart) -> None:
        # «берегти кошик
        self._carts[cart.user_id] = cart
    
    def clear(self, user_id: str) -> None:
        # ќчистити кошик
        if user_id in self._carts:
            self._carts[user_id].items = []