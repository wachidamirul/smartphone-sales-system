from utils.colors import *
from utils.header import header_cashier
from utils.input_utils import input_string
from utils.message import message


class Cashier:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{BRIGHT_BLUE}{self.id:<5} {self.name:<15}{RESET}"

    @classmethod
    def create(cls, cashiers):
        # Get cashier details
        name = input_string("Enter cashier name: ")

        # Check if cashier already exists
        for cashier in cashiers:
            if cashier.name.lower() == name.lower():
                message(f"{name} already exists. Please try again.", True)
                return

        # Get the next id
        id = len(cashiers) + 1

        # Create Cashier object
        cashier = Cashier(id, name)
        cashiers.append(cashier)
        message(f"{name} has been added successfully.")

    @classmethod
    def view(cls, cashiers):
        header_cashier()
        # Check if cashier list is empty
        if not cashiers:
            message("Cashier list is empty", True)
            return

        # Display cashier list
        for cashier in cashiers:
            print(cashier)
