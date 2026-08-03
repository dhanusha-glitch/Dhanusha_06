# -------------------- User Class --------------------

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name


# -------------------- Customer Class --------------------

class Customer(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.cart = Cart()
        self.orders = []


# -------------------- Product Class --------------------

class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


# -------------------- Cart Class --------------------

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):

        if product.get_id() in self.items:
            self.items[product.get_id()][1] += quantity
        else:
            self.items[product.get_id()] = [product, quantity]

        print("Product added to cart.")

    def remove_item(self, product_id):

        if product_id in self.items:
            del self.items[product_id]
            print("Product removed from cart.")
        else:
            print("Product not found in cart.")

    def update_quantity(self, product_id, quantity):

        if product_id in self.items:
            if quantity > 0:
                self.items[product_id][1] = quantity
                print("Quantity updated.")
            else:
                self.remove_item(product_id)
        else:
            print("Product not found.")

    def calculate_total(self):

        total = 0

        for item in self.items.values():
            total += item[0].get_price() * item[1]

        return total

    def display_cart(self):

        if len(self.items) == 0:
            print("Cart is Empty.")
            return

        print("\n----------- Shopping Cart -----------")

        for item in self.items.values():
            product = item[0]
            qty = item[1]
            subtotal = product.get_price() * qty

            print(product.get_name(),
                  "| Qty:", qty,
                  "| Price: ₹", product.get_price(),
                  "| Total: ₹", subtotal)

        print("Grand Total: ₹", self.calculate_total())

    def clear_cart(self):
        self.items.clear()


# -------------------- Order Class --------------------

class Order:
    order_no = 1001

    def __init__(self, amount):
        self.order_id = Order.order_no
        Order.order_no += 1

        self.amount = amount

    def show_order(self):
        print("Order ID:", self.order_id,
              "| Amount Paid: ₹", self.amount)


# -------------------- Product List --------------------

products = [
    Product("P101", "Laptop", 45000),
    Product("P102", "Keyboard", 1200),
    Product("P103", "Mouse", 700),
    Product("P104", "Headphones", 2500),
    Product("P105", "Monitor", 8500)
]

customer = Customer("C101", "Customer")


# -------------------- Helper Function --------------------

def show_products():

    print("\n----------- Available Products -----------")

    for p in products:
        print(p.get_id(), "-", p.get_name(),
              "- ₹", p.get_price())


def find_product(product_id):

    for p in products:
        if p.get_id().lower() == product_id.lower():
            return p

    return None


# -------------------- Main Program --------------------

while True:

    print("\n========= ONLINE SHOPPING CART =========")
    print("1. Show Products")
    print("2. Add Product to Cart")
    print("3. Remove Product")
    print("4. Update Quantity")
    print("5. View Cart")
    print("6. Checkout")
    print("7. Order History")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":

        pid = input("Enter Product ID: ")
        product = find_product(pid)

        if product:
            qty = int(input("Enter Quantity: "))
            customer.cart.add_item(product, qty)
        else:
            print("Invalid Product ID.")

    elif choice == "3":

        pid = input("Enter Product ID: ")
        customer.cart.remove_item(pid)

    elif choice == "4":

        pid = input("Enter Product ID: ")
        qty = int(input("Enter New Quantity: "))
        customer.cart.update_quantity(pid, qty)

    elif choice == "5":

        customer.cart.display_cart()

    elif choice == "6":

        total = customer.cart.calculate_total()

        if total == 0:
            print("Cart is Empty.")
            continue

        discount = 0

        if total >= 5000:
            discount = total * 0.10

        final_amount = total - discount

        print("\nTotal Amount : ₹", total)
        print("Discount     : ₹", discount)
        print("Final Amount : ₹", final_amount)

        confirm = input("Confirm Order (Y/N): ")

        if confirm.lower() == "y":

            order = Order(final_amount)
            customer.orders.append(order)

            customer.cart.clear_cart()

            print("Order Placed Successfully.")
            order.show_order()

    elif choice == "7":

        if len(customer.orders) == 0:
            print("No Orders Found.")
        else:
            print("\n--------- Order History ---------")
            for order in customer.orders:
                order.show_order()

    elif choice == "8":

        print("Thank You for Shopping.")
        break

    else:
        print("Invalid Choice.")