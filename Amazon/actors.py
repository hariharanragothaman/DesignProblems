"""
This file is about the various actors in the problem
Admin, Guest, User etc.
"""
class Account:
    def __init__(self, user_name, password, name, email, phone, shipping_address, status=AccountStatus):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.shipping_address = shipping_address

    def add_product(self, product):
        pass

    def add_product_review(self, review):
        pass

    def reset_password(self):
        pass

from abc import ABC, abstractmethod

class Customer(ABC):
    def __init__(self, cart, order):
        self.cart = cart
        self.order = order

    def get_shopping_cart(self):
        return self.cart

    def remove_item_from_cart(self, item):
        pass

class Guest(Customer):
    def register_account(self):
        pass

    def place_order(self, order):
        pass

class Member(Customer):
    def __init__(self, account):
        self.account = account

    def place_order(self, order):
        pass
