from model.smartphone import Smartphone
from utils.header import header_menu, header_product
from utils.input_utils import input_float, input_int, input_string
from utils.message import message


class Store:
    def __init__(self):
        self.smartphones = []

    def add_smartphone(self):
        header_menu("Add Smartphone")
        # Get smartphone details
        name = input_string("Enter smartphone name: ")
        price = input_float("Enter smartphone price: ", 0.01)
        stock = input_int("Enter smartphone stock: ", 0)

        # Check if smartphone already exists
        for smartphone in self.smartphones:
            if smartphone.name.lower() == name.lower():
                message(f"{name} already exists. Please try again.", True)
                return

        # Get the next id
        id = len(self.smartphones) + 1

        # Create Smartphone object
        smartphone = Smartphone(id, name, price, stock)
        self.smartphones.append(smartphone)
        message(f"{name} has been added successfully.")

    def display_smartphones(self):
        header_menu("List of Smartphones")
        header_product()

        # Check if smartphone list is empty
        if not self.smartphones:
            message("Smartphone list is empty", True)
            return

        # Display smartphone list
        for smartphone in self.smartphones:
            print(smartphone)
