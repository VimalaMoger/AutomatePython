from typing import List


#Implementing few tests for shopping cart
class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []  #adding items
        self.max_size = max_size

    def add(self, item: str):  # update items
        if self.size() == self.max_size:
            raise OverflowError("Items exceeded the size limit")
        self.items.append(item)

    def size(self) -> int:  #count number of items in items
        return len(self.items)

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price