class Cart:
    def init(self):
        self.items = []

cart = Cart()

while True:
    print("1 Add Item")
    print("2 Remove Item")
    print("3 View Cart")
    print("4 Checkout")

    selection = input("\nChoose: ")

    if selection == "1":
        item = input("Item: ")
        cart.items.append(item)

    elif selection == "2":
        item = input("Remove item: ")
        if item in cart.items:
            cart.items.remove(item)

    elif selection == "3":
        print("Cart:", cart.items)

    elif selection == "4":
        print("Checkout items:", cart.items)
        break

    else:
        print("invalid selection")