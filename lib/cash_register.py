#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.transactions = []
        self.last_transaction = ()
    
    def add_item(self, title, price, quantity = 1):
        self.last_transaction = (title, price, quantity)
        self.total += round(price * quantity, 2)
        for num in range(quantity):
            self.items.append(title)
            self.transactions.append(price)
        return self.items

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round((self.discount / 100) * self.total) * 4
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        last_transaction_quantity = self.last_transaction[2]
        for num in range(last_transaction_quantity):
            self.items.pop()
            self.total -= self.transactions.pop()
        if len(self.items) == 0:
            self.total = 0
        
        

