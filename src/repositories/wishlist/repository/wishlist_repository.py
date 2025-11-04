from typing import Dict, List
from common.models import Wishlist
from common.interfaces import WishlistRepo

class SimpleWishlistRepository(WishlistRepo):
    def __init__(self):
        # «бер≥гаЇмо списки бажань по user_id
        self._wishlists: Dict[str, Wishlist] = {}
    
    def get(self, user_id: str) -> Wishlist:
        # якщо списку бажань немаЇ - створюЇмо новий порожн≥й
        if user_id not in self._wishlists:
            self._wishlists[user_id] = Wishlist(user_id=user_id, product_ids=[])
        return self._wishlists[user_id]
    
    def save(self, wishlist: Wishlist) -> None:
        # «берегти список бажань
        self._wishlists[wishlist.user_id] = wishlist