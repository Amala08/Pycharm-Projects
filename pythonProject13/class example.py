class Product:
    price_after_discount = 0.9  # class attribute # after 10% discount
    all_products = []

    def __init__(self, product_name: str, price: float, quantity: int):
        assert price >= 0, "Price should be greater than zero"
        assert quantity >= 0, "Quantity should be greater than zero"

        self.name = product_name  # instance attribute
        self.price = price  # instance attribute
        self.quantity = quantity  # instance attribute

        Product.all_products.append(self)

    def calculate_total_price(self):
        return self.quantity * self.price

    def calculate_price_after_discount(self):
        return self.price * self.quantity * self.price_after_discount

    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.quantity})"


# object. or instance or instance variable
tv = Product("Tv", 100.00, 5)

print(tv.__dict__)
print(Product.__dict__)

tv_total_price = tv.calculate_total_price()
tv_final_price = tv.calculate_price_after_discount()
print(f"Tv total price: {tv_total_price}")
print(f"Tv final price after discount: {tv_final_price}")

fridge = Product("fridge", 120.5, 2)
fridge_total_price = fridge.calculate_total_price()
fridge_final_price = fridge.calculate_price_after_discount()
print(f"fridge total price: {fridge_total_price}")
print(f"fridge final price after discount: {fridge_final_price}")

ac = Product("ac", 1200.5, 2)
mixer = Product("mixer", 50.5, 10)
print(Product.all_products)