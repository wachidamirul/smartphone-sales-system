from utils.clear import clear
from utils.colors import *
from utils.header import (
    header_customer,
    header_menu,
    header_product,
    header_transaction,
)
from utils.input_utils import input_int
from utils.message import message


class Transaction:

    def __init__(self, id: int, customer, smartphone, quantity: int):
        self.id = id
        self.customer = customer
        self.smartphone = smartphone
        self.quantity = quantity

    def __str__(self):
        total = self.smartphone.price * self.quantity
        return f"{BRIGHT_BLUE}{self.id:<5} {self.customer.name:<10} {self.smartphone.name:<15} {self.quantity:<10} Rp {total:<15,.2f}{RESET}"

    @classmethod
    def create(cls, customers, smartphones, transactions):
        # show list of customers
        header_customer()
        for customer in customers:
            print(customer)
        customer_id = input_int("Enter customer ID: ", 0)

        # Check if customer exists
        while customer_id <= 0 or customer_id > len(customers):
            message("Customer does not exist. Please try again.", True)
            customer_id = input_int("Enter customer ID: ", 0)

        # show list of smartphones
        clear()
        header_menu("Add Transaction")
        header_product()
        for smartphone in smartphones:
            print(smartphone)
        print(f"Enter customer ID: {customer_id}")
        smartphone_id = input_int("Enter smartphone ID: ", 0)

        # Check if smartphone exists
        while smartphone_id <= 0 or smartphone_id > len(smartphones):
            message("Smartphone does not exist. Please try again.", True)
            smartphone_id = input_int("Enter smartphone ID: ", 0)

        quantity = input_int("Enter quantity: ", 0)
        id = len(transactions) + 1

        # Create Transaction object
        transaction = Transaction(
            id, customers[customer_id - 1], smartphones[smartphone_id - 1], quantity
        )
        transactions.append(transaction)
        message(
            f"Transaction from {transaction.customer.name} has been added successfully."
        )

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
