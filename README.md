# 🛒 E-Commerce Order Management System (UC-005)

---

## 📌 Problem Statement

Design and implement a console-based E-Commerce Order Management System using Object-Oriented Programming (OOP) concepts.  
The system should simulate real-world e-commerce operations including product browsing, cart management, checkout, payment processing, and order tracking.

---

## 🧠 Approach / Logic Used

The system is designed using core OOP principles:

### 1. Encapsulation
All class attributes are private and accessed using methods.

### 2. Inheritance
- DigitalProduct inherits Product  
- OnlinePayment inherits Payment  
- ExpressShipment inherits Shipment  

### 3. Polymorphism
Method overriding is used:
- updateStock() → Digital vs Normal product  
- process() → Payment vs OnlinePayment  
- deliver() → Shipment vs ExpressShipment  

---

## 📘 Use Case Coverage

### Actors
- Customer  
- Seller  
- Delivery Partner  
- Payment Gateway  

### Main Flow
1. Customer browses products  
2. Adds items to cart  
3. Proceeds to checkout  
4. Applies voucher (optional)  
5. Makes payment  
6. Order is placed  
7. Shipment is initiated  
8. Product is delivered  

### Alternate Flows
- A1: Product out of stock → User notified  
- A2: Voucher applied → Discount applied  
- A3: Return initiated after delivery  

### Exception Flows
- E1: Payment failure → Retry option  
- E2: Inventory mismatch → Order blocked  
- E3: Delivery issue → Shipment held  

---

## ⚙️ Steps to Execute the Code

1. Install Python (3.x)

2. Clone the repository:
   
4. Navigate to the folder:
   cd <file_name>

5. Run the program:
   python <file_name>.py

6. Follow the on-screen instructions to:
   - Add products  
   - Manage cart  
   - Apply voucher  
   - Place order  
   - Make payment  
   - Track shipment  

---

## 🚀 Features

- Product management (Normal & Digital)
- Add / Remove items from cart
- Voucher system (SAVE10, SAVE20)
- Order placement with stock validation
- Payment system with OTP option
- Shipment tracking (Normal & Express)
- Delivery confirmation
- Return handling
- Payment retry mechanism

---

## ⚠️ Error Handling

- Prevents adding out-of-stock products  
- Handles invalid voucher codes  
- Detects incorrect payment amount  
- OTP verification failure handling  
- Handles stock mismatch during order  
- Retry option for failed payment  
- Handles delivery address issues  

---



## 🎯 Use Case

- Academic mini project  
- OOP concept demonstration  
- Interview preparation  

---

