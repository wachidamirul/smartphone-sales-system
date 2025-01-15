from utils.clear import clear
from utils.colors import *
from utils.header import (
    header_customer,
    header_menu,
    header_product,
    header_transaction,
)
from utils.validation import get_valid_id, get_valid_quantity
from utils.message import message


class Transaction:

    def __init__(self, id: int, customer, smartphone, quantity: int):
        self.id = id
        self.customer = customer
        self.smartphone = smartphone
        self.quantity = quantity

    def __str__(self):
        total = self.smartphone.price * self.quantity
        return f"{BRIGHT_BLUE}{self.id:<5} {self.customer.name:<15} {self.smartphone.name:<25} {self.quantity:<10} Rp {total:<15,.2f}{RESET}"

    @classmethod
    def create(cls, customers, smartphones, transactions):
        header_customer()
        for customer in customers:
            print(customer)
        customer_id = get_valid_id("Enter customer ID: ", customers, "Customer")

        clear()
        header_menu("Add Transaction")
        header_product()
        for smartphone in smartphones:
            print(smartphone)
        print(f"Enter customer ID: {customer_id}")

        smartphone_id = get_valid_id("Enter smartphone ID: ", smartphones, "Smartphone")
        smartphone = smartphones[smartphone_id - 1]

        while not smartphone.is_available(smartphone.stock):
            message(
                f"Stock for {smartphone.name} is not available. Please select another smartphone.",
                True,
            )
            smartphone_id = get_valid_id(
                "Enter smartphone ID: ", smartphones, "Smartphone"
            )
            smartphone = smartphones[smartphone_id - 1]

        quantity = get_valid_quantity("Enter quantity: ", smartphone.stock)
        transaction_id = len(transactions) + 1

        transaction = Transaction(
            transaction_id, customers[customer_id - 1], smartphone, quantity
        )
        transactions.append(transaction)
        smartphone.update_stock(quantity)

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
