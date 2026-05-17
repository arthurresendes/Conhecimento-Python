import uuid
import datetime
import random

class LegacyEcommerceSystem:
    def __init__(self):
        self.db = {
            "users": [],
            "products": [],
            "orders": []
        }
        self.users = Users(self.db)
        self.products = Products(self.db)
        self.orders = Orders(self.db)
        self.reports = Reports(self.db)
        self.seeder = DataSeeder(self.db, self.users, self.products, self.orders)

class Users:
    def __init__(self, db):
        self.db = db

    def create_user(self, name, email, password, role):
        user = {
            "id": str(uuid.uuid4()),
            "name": name, "email": email, "password": password,
            "role": role, "active": True, "login_attempts": 0,
            "created_at": datetime.datetime.now()
        }
        self.db["users"].append(user)
        return user

    def list_users(self):
        return self.db["users"]

class Products:
    def __init__(self, db):
        self.db = db

    def create_product(self, name, price, stock):
        product = {
            "id": str(uuid.uuid4()),
            "name": name, "price": price, "stock": stock,
            "active": True, "created_at": datetime.datetime.now()
        }
        self.db["products"].append(product)
        return product

class Orders:
    def __init__(self, db):
        self.db = db
    def create_order(self, user_id):
        order = {
            "id": str(uuid.uuid4()),
            "user_id": user_id, "items": [],
            "status": "pending", "created_at": datetime.datetime.now()
        }
        self.db["orders"].append(order)
        return order

    def add_item_to_order(self, order_id, product_id, quantity):
        product = next((p for p in self.db["products"] if p["id"] == product_id), None)
        order = next((o for o in self.db["orders"] if o["id"] == order_id), None)

        if order and product and product["stock"] >= quantity:
            order["items"].append({
                "product_id": product_id,
                "price": product["price"],
                "quantity": quantity
            })
            product["stock"] -= quantity

    def complete_order(self, order_id):
        for order in self.db["orders"]:
            if order["id"] == order_id:
                order["status"] = "completed"

class Reports:
    def __init__(self, db):
        self.db = db

    def full_report(self):
        print("\n=== USERS REPORT ===")
        for u in self.db["users"]:
            print(f"Nome: {u['name']} | Role: {u['role']}")

        print("\n=== PRODUCTS REPORT ===")
        for p in self.db["products"]:
            print(f"Produto: {p['name']} | Estoque: {p['stock']}")

        total_sales = sum(
            sum(item['price'] * item['quantity'] for item in o['items'])
            for o in self.db["orders"] if o["status"] == "completed"
        )
        print(f"\n=== TOTAL SALES: R$ {total_sales:.2f} ===")

class DataSeeder:
    def __init__(self, db, users_tool, products_tool, orders_tool):
        self.db = db
        self.users_tool = users_tool
        self.products_tool = products_tool
        self.orders_tool = orders_tool

    def seed_data(self):
        for i in range(5):
            self.users_tool.create_user(f"User {i}", f"u{i}@test.com", "123456", "customer")
       
        for i in range(5):
            self.products_tool.create_product(f"Item {i}", random.randint(50, 100), 10)

    def generate_random_orders(self):
        users = self.db["users"]
        products = self.db["products"]
       
        for _ in range(3):
            if not users or not products:
                break
            user = random.choice(users)
            order = self.orders_tool.create_order(user["id"])
            product = random.choice(products)
           
            self.orders_tool.add_item_to_order(order["id"], product["id"], 2)
            self.orders_tool.complete_order(order["id"])

if __name__ == "__main__":
    system = LegacyEcommerceSystem()
    system.seeder.seed_data()
    system.seeder.generate_random_orders()
    system.reports.full_report()