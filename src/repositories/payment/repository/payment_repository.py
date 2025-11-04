from typing import Dict
from common.models import Payment
from common.interfaces import PaymentRepo

class SimplePaymentRepository(PaymentRepo):
    def __init__(self):
        self._payments: Dict[str, Payment] = {}
    
    def get(self, payment_id: str) -> Payment:
        return self._payments.get(payment_id)
    
    def add(self, payment: Payment) -> None:
        self._payments[payment.id] = payment
    
    def update(self, payment: Payment) -> None:
        self._payments[payment.id] = payment