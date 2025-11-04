from typing import List, Dict
from common.models import Product
from common.interfaces import ProductRepo

class SimpleProductRepository(ProductRepo):
    def __init__(self):
        # Створюємо тестові товари
        self._products: Dict[str, Product] = {
            "prod_1": Product(
                id="prod_1",
                title="iPhone 15",
                price=999.99,
                stock=10,
                tags=["phone", "apple", "smartphone"]
            ),
            "prod_2": Product(
                id="prod_2", 
                title="Samsung Galaxy",
                price=799.99,
                stock=5,
                tags=["phone", "samsung", "android"]
            ),
            "prod_3": Product(
                id="prod_3",
                title="MacBook Pro", 
                price=1999.99,
                stock=3,
                tags=["laptop", "apple", "computer"]
            )
        }
    
    def get(self, product_id: str) -> Product:
        # Знайти товар по ID
        return self._products.get(product_id)
    
    def list(self) -> List[Product]:
        # Отримати всі товари
        return list(self._products.values())
    
    def update(self, product: Product) -> None:
        # Оновити товар
        self._products[product.id] = product