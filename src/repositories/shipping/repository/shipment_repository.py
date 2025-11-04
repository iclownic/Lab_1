from typing import Dict
from common.models import Shipment
from common.interfaces import ShipmentRepo

class SimpleShipmentRepository(ShipmentRepo):
    def __init__(self):
        self._shipments: Dict[str, Shipment] = {}
        # Додатково зберігаємо зв'язок order_id -> shipment_id
        self._order_to_shipment: Dict[str, str] = {}
    
    def get(self, shipment_id: str) -> Shipment:
        return self._shipments.get(shipment_id)
    
    def get_by_order(self, order_id: str) -> Shipment:
        # Знайти доставку по order_id
        shipment_id = self._order_to_shipment.get(order_id)
        return self._shipments.get(shipment_id) if shipment_id else None
    
    def add(self, shipment: Shipment) -> None:
        self._shipments[shipment.id] = shipment
        self._order_to_shipment[shipment.order_id] = shipment.id
    
    def update(self, shipment: Shipment) -> None:
        self._shipments[shipment.id] = shipment