class  Product:
    def __init__(self,productId,name,category,price,stock,sellerId):
        self.productId=productId
        self.name=name
        self.category=category
        self.price=price
        self.stock=stock
        self.sellerId=sellerId
    def updateStock(self,new):
        self.stock-=new
    def applyDiscount(self,voucher):
        if voucher == "discount":
            self.price = self.price-(self.price/10)
        else:
            print("Invalid Voucher : Enter correct voucher")
    def getDetails(self):
        print("product ID",self.productId)
        print("Name",self.name)
        print("Category",self.category)
        print("Price",self.price)
        print("Stock",self.stock)
        print("Seller ID",self.sellerId)
    def cost(self):
        return self.price
class Cart:
    def __init__(self,cartId,customerId):
        self.cartId=cartId
        self.customerId=customerId
        self.items=[10]
        self.Product=Product
        self.totalAmount=0
    def addItem(self,new):
        self.items.append(new)
        self.totalAmount+=new.cost()
        print(self.totalAmount)
    def removeItem(self,name):
        if name in self.items:
            self.items.remove(name)
        else:
            print("Item is not in the cart")
    def clearCart(self):
        if len(self.items)>0:
            self.items.pop()
    def applyVoucher(self,voucher):
        if voucher == "discount":
            self.totalAmount=self.totalAmount-(self.totalAmount/10)
    def amount(self):
        return self.totalAmount
class Order:
    def __init__(self,orderId,paymentId,trackingId):
        self.orderId=orderId
        self.status=""
        self.paymentId=paymentId
        self.trackingId=trackingId
        self.cart=Cart
    def placeOrder(self):
        self.status="placed"
        print("The order is placed")
    def cancelOrder(self):
        self.status="Cancel"
        print("The order is Cancelled")
    def returnOrder(self):
        self.status="Return"
        print("The order is in return")
class Payment:
    def __init__(self,method,amount,gateway,totalamount):
        self.method=method
        self.amount=amount
        self.totalAmount=totalamount
        self.gateway=gateway
        self.Order=Order
        self.Cart=Cart
    def processPayment(self):
        print("Your Payment is being processed")
        if self.verifyTransaction() :
            print("Confirmed")
    def refund(self):
        print("The Amount Will be refund")
    def verifyTransaction(self):
        if self.amount == self.totalAmount:
            return True
        else:
            self.refund()
class Shipment:
    def __init__(self,shipmentId,payment,carrier,status,estimatedDelivery):
        self.shipmentId=shipmentId
        self.payment=payment
        self.carrier=carrier
        self.status=status
        self.estimatedDelivery=estimatedDelivery
    def updateStatus(self,stat):
        self.status=stat
    def getTracking(self):
        print(self.status)
    def markDelivered(self):
        self.status="delivered"

A1=input("Enter Product1 Name: ")
V1=int(input("Enter Product1 amount: "))
a=Product(191,A1,"ft",V1,5,234)
B1=input("Enter Product2 Name: ")
V2=int(input("Enter Product1 amount: "))
b=Product(192,B1,"ft",V2,5,234)
p=Cart(172,191)
p.addItem(a)
p.addItem(b)
vou=input("Enter the voucher: ")
p.applyVoucher(vou)
o=Order(172,457,123)
o.placeOrder()
print("The total Amount",p.amount())
v=float(input("Enter The Amount: "))
pay=Payment("upi",v,"gpay",p.amount())
pay.processPayment()
sta=input()
s=Shipment(124,"upi","Truck",sta,"15.02.2026")
s.markDelivered()
