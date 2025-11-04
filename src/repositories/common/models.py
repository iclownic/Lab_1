from dataclasses import dataclass
from typing import List, Optional

@dataclass
class User:
    id: str
    email: str
    password_hash: str
    is_active: bool = True

@dataclass  
class Product:
    id: str
    title: str
    price: float
    stock: int
    tags: List[str] = None

@dataclass
class CartItem:
    product_id: str
    qty: int

@dataclass
class Cart:
    user_id: str
    items: List[CartItem] = None

@dataclass
class OrderItem:
    product_id: str
    qty: int

@dataclass  
class Order:
    id: str
    user_id: str
    items: List[OrderItem]
    amount: float
    status: str = "CREATED"

@dataclass
class Payment:
    id: str
    order_id: str
    amount: float
    status: str = "PENDING"
    provider_txn_id: str = ""

@dataclass
class Shipment:
    id: str
    order_id: str
    tracking: str = ""
    status: str = "CREATED"

@dataclass
class Review:
    id: str
    product_id: str
    user_id: str
    rating: int
    text: str

@dataclass
class Wishlist:
    user_id: str
    product_ids: List[str] = None

@dataclass
class Notification:
    id: str
    user_id: str
    title: str
    message: str
    notification_type: str  # email, sms, push
    is_read: bool = False
    created_at: str = ""

def new_id():
    import uuid
    return str(uuid.uuid4())