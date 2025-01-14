from utils.colors import *
from utils.header import header_customer, header_menu
from utils.input_utils import input_string
from utils.message import message


class Customer:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.transactions = []

    def __str__(self):
        return f"{BRIGHT_BLUE}{self.id:<5} {self.name:<20} {self.email:<20}{RESET}"

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        return f"Transaction ID: {transaction.id} has been added to {self.name}"

    @classmethod
    def create(cls, customers):
        header_menu("Add Customer")
        # Get customer details
        name = input_string("Enter customer name: ")
        email = input_string("Enter customer email: ")

        # Check if customer already exists
        for customer in customers:
            if customer.email.lower() == email.lower():
                message(f"{email} already exists. Please try again.", True)
                return

        # Get the next id
        id = len(customers) + 1

        # Create Customer object
        customer = Customer(id, name, email)
        customers.append(customer)
        message(f"{name} has been added successfully.")

    @classmethod
    def view(cls, customers):
        header_menu("List of Customers")
        header_customer()
        # Check if customer list is empty
        if not customers:
            message("Customer list is empty", True)
            return

        # Display customer list
        for customer in customers:
            print(customer)
