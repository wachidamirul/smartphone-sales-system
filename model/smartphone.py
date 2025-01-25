from utils.colors import *
from utils.emei import generate_imei
from utils.header import header_product
from utils.input_utils import input_float, input_int, input_string
from utils.message import message


class Smartphone:
    def __init__(self, id: int, name: str, price: float, stock: int, imei: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.imei = imei

    def __str__(self):
        if self.stock == 0:
            color = BRIGHT_RED
        else:
            color = BRIGHT_BLUE
        return f"{color}{self.id:<5} {self.name:<25} {self.stock:<10} Rp {self.price:<15,.2f} {self.imei:<20}{RESET}"

    def update_stock(self, quantity: int):
        self.stock -= quantity

    def is_available(self, stock: int) -> bool:
        return self.stock >= stock and stock > 0

    @classmethod
    def create(cls, smartphones):
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

        # generate imei
        imei = generate_imei(smartphones)

        # Create Smartphone object
        smartphone = Smartphone(id, name, price, stock, imei)
        smartphones.append(smartphone)
        message(f"{name} has been added successfully.")

    @classmethod
    def view(cls, smartphones):
        header_product()

        # Check if smartphone list is empty
        if not smartphones:
            message("Smartphone list is empty", True)
            return

        # Display smartphone list
        for smartphone in smartphones:
            print(smartphone)
