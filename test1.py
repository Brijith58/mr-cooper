class Product:
    def __init__(self, productId, name, category, price, stock, sellerId):
        self.__productId = productId
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock
        self.__sellerId = sellerId

    def getProductId(self): return self.__productId
    def getName(self): return self.__name
    def getCategory(self): return self.__category
    def getPrice(self): return self.__price
    def getStock(self): return self.__stock

    def updateStock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False

    def cost(self): return self.__price


class DigitalProduct(Product):
    def __init__(self, productId, name, category, price, sellerId, link):
        super().__init__(productId, name, category, price, 999, sellerId)
        self.__link = link

    def updateStock(self, qty):
        return True


class Cart:
    def __init__(self, cid, uid):
        self.__cid = cid
        self.__uid = uid
        self.__items = []
        self.__total = 0

    def addItem(self, p):
        if p.getStock() > 0:
            self.__items.append(p)
            self.__total += p.cost()
            print("Added:", p.getName())
        else:
            print("Out of stock:", p.getName())

    def removeItem(self, name):
        for p in self.__items:
            if p.getName().lower() == name.lower():
                self.__items.remove(p)
                self.__total -= p.cost()
                print("Removed:", name)
                return
        print("Not found")

    def applyVoucher(self, code):
        if not self.__items:
            print("Cart empty")
            return
        if code == "SAVE10":
            d = self.__total * 0.1
        elif code == "SAVE20":
            d = self.__total * 0.2
        else:
            print("Invalid code")
            return
        self.__total -= d
        print("Discount:", d)

    def show(self):
        print("\nCart:")
        for p in self.__items:
            print(p.getName(), p.cost())
        print("Total:", self.__total)

    def items(self): return self.__items
    def total(self): return self.__total


class Order:
    def __init__(self, oid, uid, items):
        self.__oid = oid
        self.__uid = uid
        self.__items = items
        self.__status = "Pending"

    def place(self):
        if not self.__items:
            print("Empty order")
            return False
        for p in self.__items:
            if not p.updateStock(1):
                print("Stock issue")
                return False
        self.__status = "Placed"
        print("Order placed")
        return True

    def setStatus(self, s):
        self.__status = s

    def status(self):
        print("Status:", self.__status)


class Payment:
    def __init__(self, amount, total):
        self.amount = amount
        self.total = total
        self.status = "Pending"

    def process(self):
        if round(self.amount,2) == round(self.total,2):
            self.status = "Success"
            print("Payment success")
        else:
            self.status = "Failed"
            print("Payment failed")


class OnlinePayment(Payment):
    def __init__(self, amount, total, otp):
        super().__init__(amount, total)
        self.otp = otp

    def process(self):
        user = input("Enter OTP: ")
        if user == self.otp:
            super().process()
        else:
            print("OTP wrong")
            self.status = "Failed"


class Shipment:
    def __init__(self, sid):
        self.sid = sid
        self.status = "Packed"

    def update(self, s):
        self.status = s
        print("Shipment:", s)

    def deliver(self):
        self.status = "Delivered"
        print("Delivered")


class ExpressShipment(Shipment):
    def deliver(self):
        super().deliver()
        print("Express alert sent")


# ================= MAIN =================

if __name__ == "__main__":

    uid = int(input("Customer ID: "))
    n = int(input("No. of products: "))

    products = []

    for i in range(n):
        print("\nProduct", i+1)
        t = input("Type (normal/digital): ").lower()
        pid = int(input("ID: "))
        name = input("Name: ")
        cat = input("Category: ")
        price = float(input("Price: "))

        if t == "digital":
            link = input("Link: ")
            p = DigitalProduct(pid, name, cat, price, 1, link)
        else:
            stock = int(input("Stock: "))
            p = Product(pid, name, cat, price, stock, 1)

        products.append(p)

    cart = Cart(1, uid)

    for p in products:
        cart.addItem(p)

    cart.show()

    if input("Apply voucher? ").lower() == "yes":
        code = input("Code: ").upper()
        cart.applyVoucher(code)
        cart.show()

    if input("Remove item? ").lower() == "yes":
        name = input("Enter name: ")
        cart.removeItem(name)
        cart.show()

    order = Order(1, uid, cart.items())

    if order.place():

        total = cart.total()
        print("Total:", total)

        if input("Online payment? ").lower() == "yes":
            import random
            otp = str(random.randint(1000,9999))
            print("OTP:", otp)
            amt = float(input("Enter amount: "))
            pay = OnlinePayment(amt, total, otp)
        else:
            amt = float(input("Enter amount: "))
            pay = Payment(amt, total)

        pay.process()

        if pay.status == "Success":
            if input("Express shipment? ").lower() == "yes":
                ship = ExpressShipment(1)
            else:
                ship = Shipment(1)

            ship.update("In Transit")

            if input("Delivered? ").lower() == "yes":
                ship.deliver()
                order.setStatus("Delivered")
                order.status()

                if input("Return? ").lower() == "yes":
                    order.setStatus("Return Initiated")
                    order.status()
        else:
            print("Retry payment")
            amt = float(input("Correct amount: "))
            retry = Payment(amt, total)
            retry.process()
    else:
        print("Order failed due to stock")