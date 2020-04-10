from enum import Enum

class Address:
    def __init__(self, street, city, state, country, zipcode):

class OrderStatus(Enum):
    NOT_SHIPPED = 0
    PENDING = 1
    SHIPPED = 2
    COMPLETED = 3
    CANCELLED = 4
    REFUND_APPLIED = 5

class ShipmentStatus(Enum):
    PENDING = 0
    SHIPPED = 1
    DELIVERED = 2
    ON_HOLD =  3
