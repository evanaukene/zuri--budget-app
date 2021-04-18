class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 0
        self.record_book = []

    def check_balance(self, balance):
        if self.balance < balance:
            return False
        else:
            return True

    def deposit_funds(self, amount, description=""):
        self.record_book.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw_funds(self, amount, description=""):
        if self.check_balance(amount):
            self.balance -= amount
            self.record_book.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def compute_category_bal(self):  # This function returns the total amount of money left in the budget app
        return self.balance

    def transfer_balance(self, amount, category):  # This function transfer's funds from one category to another
        if self.check_balance(amount):
            self.balance -= amount
            self.record_book.append({"amount": -amount, "description": "funds moved to " + category.category})
            category.record_book.append({"amount": amount, "description": "funds moved from " + self.category})
            category.balance += amount
            return True
        else:
            return False


food = Budget("Food")
food.deposit_funds(2000, "first payment")
food.withdraw_funds(120, "groceries")
food.withdraw_funds(120, "haha")
print(food.compute_category_bal())

entertainment = Budget("Entertainment")
food.transfer_balance(500, entertainment)
print(entertainment.record_book)
print(food.record_book)
print(food.compute_category_bal())


clothing = Budget("Clothing")
food.transfer_balance(500, clothing)
clothing.withdraw_funds(50)
clothing.withdraw_funds(50)
print(clothing.record_book)
print(food.compute_category_bal())
print(clothing.compute_category_bal())

