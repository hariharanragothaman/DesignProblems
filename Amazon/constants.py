from enum import Enum

class Address:
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

class OrderStatus(Enum):
    NOT_SHIPPED = 1
    PENDING = 2
    SHIPPED = 3
    COMPLETED = 4
    CANCELLED = 5
    REFUND_APPLIED = 6

class ShipmentStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    ON_HOLD =  4

class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    FILLED = 4
    DECLINED = 5
    CANCELLED = 6
    ABANDONED = 7
    SETTLING = 8
    SETTLED = 9
    REFUNDED = 10