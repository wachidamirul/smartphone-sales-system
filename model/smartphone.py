from utils.colors import *
from utils.header import header_menu, header_product
from utils.input_utils import input_float, input_int, input_string
from utils.message import message


class Smartphone:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{BRIGHT_BLUE}{self.id:<5} {self.name:<20} {self.stock:<10} Rp {self.price:<15,.2f}{RESET}"

    def update_stock(self, stock: int):
        self.stock += stock

    def is_available(self, stock: int) -> bool:
        return self.stock >= stock

    @classmethod
    def create(cls, smartphones):
        header_menu("Add Smartphone")
        # Get smartphone details
        name = input_string("Enter smartphone name: ")
        price = input_float("Enter smartphone price: ", 0.01)
        stock = input_int("Enter smartphone stock: ", 0)

        # Check if smartphone already exists
        for smartphone in smartphones:
            if smartphone.name.lower() == name.lower():
                message(f"{name} already exists. Please try again.", True)
                return

        # Get the next id
        id = len(smartphones) + 1

        # Create Smartphone object
        smartphone = Smartphone(id, name, price, stock)
        smartphones.append(smartphone)
        message(f"{name} has been added successfully.")

    @classmethod
    def view(cls, smartphones):
        header_menu("List of Smartphones")
        header_product()

        # Check if smartphone list is empty
        if not smartphones:
            message("Smartphone list is empty", True)
            return

        # Display smartphone list
        for smartphone in smartphones:
            print(smartphone)
