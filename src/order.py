class Order(object):
    def __init__(self, items, is_in_warehouse, imdb_rating):
        self.items = items

    def total(self):
        return sum(item['quantity'] * item['price'] for item in self.items)
