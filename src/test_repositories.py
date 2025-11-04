from user.repository.user_repository import SimpleUserRepository
from catalog.repository.product_repository import SimpleProductRepository
from cart.repository.cart_repository import SimpleCartRepository
from order.repository.order_repository import SimpleOrderRepository

def test_repositories():
    print("🧪 Тестуємо репозиторії...")
    
    # Тестуємо User Repository
    user_repo = SimpleUserRepository()
    user = user_repo.get("user_1")
    print(f"✅ Користувач: {user.email}")
    
    # Тестуємо Product Repository  
    product_repo = SimpleProductRepository()
    products = product_repo.list()
    print(f"✅ Товари: {len(products)} шт")
    for product in products:
        print(f"   - {product.title}: ${product.price}")
    
    # Тестуємо Cart Repository
    cart_repo = SimpleCartRepository()
    cart = cart_repo.get("user_1")
    print(f"✅ Кошик: {len(cart.items)} товарів")
    
    # Тестуємо Order Repository
    order_repo = SimpleOrderRepository()
    print(f"✅ Order репозиторій готовий")
    
    print("🎉 Всі репозиторії працюють!")

if __name__ == "__main__":
    test_repositories()