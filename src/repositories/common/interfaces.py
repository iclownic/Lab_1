from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepo(ABC):
    @abstractmethod
    def get(self, user_id: str): pass
    @abstractmethod
    def get_by_email(self, email: str): pass
    @abstractmethod
    def update(self, user): pass

class ProductRepo(ABC):
    @abstractmethod
    def get(self, product_id: str): pass
    @abstractmethod
    def list(self) -> List: pass
    @abstractmethod
    def update(self, product): pass

class CartRepo(ABC):
    @abstractmethod
    def get(self, user_id: str): pass
    @abstractmethod
    def save(self, cart): pass
    @abstractmethod
    def clear(self, user_id: str): pass

class OrderRepo(ABC):
    @abstractmethod
    def get(self, order_id: str): pass
    @abstractmethod
    def add(self, order): pass
    @abstractmethod
    def update(self, order): pass

class PaymentRepo(ABC):
    @abstractmethod
    def get(self, payment_id: str): pass
    @abstractmethod
    def add(self, payment): pass
    @abstractmethod
    def update(self, payment): pass

class ShipmentRepo(ABC):
    @abstractmethod
    def get(self, shipment_id: str): pass
    @abstractmethod
    def get_by_order(self, order_id: str): pass
    @abstractmethod
    def add(self, shipment): pass
    @abstractmethod
    def update(self, shipment): pass

# Допоміжні інтерфейси
class PasswordHasher(ABC):
    @abstractmethod
    def verify(self, plain_password: str, hashed_password: str) -> bool: pass

class TokenIssuer(ABC):
    @abstractmethod
    def issue(self, user_id: str) -> str: pass

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, order_id: str, amount: float) -> tuple[bool, str]: pass

class ShippingProvider(ABC):
    @abstractmethod
    def create_shipment(self, order_id: str) -> str: pass
    @abstractmethod
    def track(self, tracking_number: str) -> str: pass

class ReviewRepo(ABC):
    @abstractmethod
    def get(self, review_id: str): pass
    @abstractmethod
    def add(self, review): pass
    @abstractmethod
    def update(self, review): pass
    @abstractmethod
    def list_for_product(self, product_id: str): pass

class WishlistRepo(ABC):
    @abstractmethod
    def get(self, user_id: str): pass
    @abstractmethod
    def save(self, wishlist): pass

class NotificationRepo(ABC):
    @abstractmethod
    def get(self, notification_id: str): pass
    @abstractmethod
    def add(self, notification): pass
    @abstractmethod
    def list_for_user(self, user_id: str): pass
    @abstractmethod
    def mark_as_read(self, notification_id: str): pass