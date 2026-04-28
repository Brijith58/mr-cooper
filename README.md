# 🛒 E-Commerce Order Management System (UC-005)

A console-based Python application that simulates a complete e-commerce workflow — from product selection to order delivery — using Object-Oriented Programming (OOP).

---

## 🚀 Features

- Product management (Normal & Digital)
- Add / Remove items from cart
- Voucher system (SAVE10, SAVE20)
- Order placement with stock validation
- Payment processing (Normal + OTP-based)
- Shipment tracking (Normal & Express)
- Delivery and return handling
- Payment retry on failure

---

## 🧠 OOP Concepts Used

- Encapsulation → Private attributes in all classes  
- Inheritance →  
  - DigitalProduct → Product  
  - OnlinePayment → Payment  
  - ExpressShipment → Shipment  
- Polymorphism → Method overriding:
  - updateStock()
  - process()
  - deliver()

---

## 🏗️ Workflow

Customer → Add Products → Cart → Apply Voucher → Place Order  
→ Payment → Shipment → Delivery → Return (optional)

---

## 📦 Classes

- Product  
- DigitalProduct  
- Cart  
- Order  
- Payment  
- OnlinePayment  
- Shipment  
- ExpressShipment  

---

## ▶️ How to Run

1. Install Python (3.x)
2. Save file as `ecommerce.py`
3. Run:

```bash
python ecommerce.py
