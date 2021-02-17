class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__descr = description
        self.__qty = units_in_inventory
        self.__price = price

    def set_description(self, description):
        self.__descr = description

    def set_quantity(self, units_in_inventory):
        self.__qty = units_in_inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__descr

    def get_quantity(self):
        return self.__qty

    def get_price(self):
        return self.__price

item1 = RetailItem('Jacket', 12, 59.95)
item2 = RetailItem('Designer Jeans', 40,34.95)
item3 = RetailItem('Shirt', 20, 24.95)