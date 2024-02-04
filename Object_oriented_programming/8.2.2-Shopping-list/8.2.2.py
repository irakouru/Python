"""Please write a function named total_units(my_list: ShoppingList), which takes a ShoppingList 
type object as its argument. The function should calculate the total number of units listed, 
and return the value."""

class ShoppingList:
    def __init__(self):
        self.items = []

    def add(self, item, amount):
        self.items.append((item, amount))

    def number_of_items(self):
        return len(self.items)

    def item(self, index):
        return self.items[index - 1][0]

    def amount(self, index):
        return self.items[index - 1][1]

def total_units(my_list: ShoppingList):
    total = 0
    for i in range(1, my_list.number_of_items() + 1):
        total += my_list.amount(i)
    return total
    
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("pineapple", 1)

    print(total_units(my_list))
