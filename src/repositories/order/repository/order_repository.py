from typing import Dict
from common.models import Order
from common.interfaces import OrderRepo

class SimpleOrderRepository(OrderRepo):
    def __init__(self):
        self._orders: Dict[str, Order] = {}
    
    def get(self, order_id: str) -> Order:
        # Знайти замовлення по ID
        return self._orders.get(order_id)
    
    def add(self, order: Order) -> None:
        # Додати нове замовлення
        self._orders[order.id] = order
    
    def update(self, order: Order) -> None:
        # Оновити замовлення
        self._orders[order.id] = order