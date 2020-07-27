class ProductCategory:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProductReview:
    def __init__(self, rating, review, reviewer):
        self.rating = rating
        self.review = review
        self.reviewer = reviewer

class Product:
    def __init__(self, id, name, description, price, category, seller_account):
        self.product_id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.available_item_count = 0
        self.seller = seller_account

    def get_available_count(self):
        pass

s1 = "abcd"
s2 = "abcdef"

print(s1-s2)