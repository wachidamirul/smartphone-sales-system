from model.customer import Customer
from model.smartphone import Smartphone
from model.transaction import Transaction
from utils.clear import clear
from utils.header import header_menu
from utils.message import message
from utils.colors import *


class Store:
    smartphones = []
    customers = []
    transactions = []

    def __init__(self):
        pass

    @classmethod
    def menu(cls):
        while True:
            try:
                print("\n====== Menu ======")
                print("1. Add Smartphone")
                print("2. Display Smartphones")
                print("3. Add Customer")
                print("4. Display Customers")
                print("5. Add Transaction")
                print("6. Display Transactions")
                print("99. Exit")

                choice = input(
                    f"Enter your choice {BRIGHT_YELLOW}(1-6 or 99 to exit){RESET}: "
                )

                if not choice.isdigit():
                    raise ValueError("Choice must be a number.")

                choice = int(choice)

                if choice == 1:
                    clear()
                    header_menu("Add Smartphone")
                    Smartphone.create(cls.smartphones)
                elif choice == 2:
                    clear()
                    header_menu("List of Smartphones")
                    Smartphone.view(cls.smartphones)
                elif choice == 3:
                    clear()
                    header_menu("Add Customer")
                    Customer.create(cls.customers)
                elif choice == 4:
                    clear()
                    header_menu("List of Customers")
                    Customer.view(cls.customers)
                elif choice == 5:
                    clear()
                    header_menu("Add Transaction")
                    Transaction.create(cls.customers, cls.smartphones, cls.transactions)
                elif choice == 6:
                    clear()
                    header_menu("List of Transactions")
                    Transaction.view(cls.transactions)
                elif choice == 99:
                    clear()
                    message("Exiting System, Goodbye!")
                    break
                else:
                    clear()
                    message("Invalid choice. Please try again.", True)

            except ValueError as e:
                clear()
                message(f"Error: {e}. Please try again.", True)
            except KeyboardInterrupt:
                clear()
                message("Exiting System, Goodbye!")
                break
