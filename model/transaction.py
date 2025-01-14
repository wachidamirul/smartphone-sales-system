from utils.clear import clear
from utils.colors import *
from utils.header import (
    header_customer,
    header_product,
    header_transaction,
)
from utils.input_utils import input_float, input_int
from utils.message import message


class Transaction:

    def __init__(self, id: int, customer, smartphone, quantity: int, total: float):
        self.id = id
        self.customer = customer
        self.smartphone = smartphone
        self.quantity = quantity
        self.total = total

    def __str__(self):
        return f"{BRIGHT_BLUE}{self.id:<5} {self.customer.name:<10} {self.smartphone.name:<15} {self.quantity:<10} Rp {self.total:<15,.2f}{RESET}"

    def calculate_total(self, smartphones):
        for smartphone in smartphones:
            if smartphone.id == self.smartphone:
                self.total = smartphone.price * self.quantity
                break

    @classmethod
    def create(cls, customers, smartphones, transactions):
        # show list of customers
        header_customer()
        for customer in customers:
            print(customer)
        customer_id = input_int("Enter customer ID: ", 0)

        # show list of smartphones
        clear()
        header_product()
        for smartphone in smartphones:
            print(smartphone)
        print(f"Enter customer ID: {customer_id}")
        smartphone_id = input_int("Enter smartphone ID: ", 0)
        quantity = input_int("Enter quantity: ", 0)

        # Get the next id
        id = len(transactions) + 1

        # Create Transaction object
        transaction = Transaction(
            id, customers[customer_id], smartphones[smartphone_id], quantity, 0
        )

        # Calculate total
        transaction.calculate_total(smartphones)
        transactions.append(transaction)
        message(f"{id} has been added successfully.")

    @classmethod
    def view(cls, transactions):
        header_transaction()
        # Check if transaction list is empty
        if not transactions:
            message("Transaction list is empty", True)
            return

        # Display transaction list
        for transaction in transactions:
            print(transaction)
