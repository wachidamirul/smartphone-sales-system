from model.customer import Customer
from model.smartphone import Smartphone
from utils.clear import clear
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
        try:
            while True:
                print("\n====== Menu ======")
                print("1. Add Smartphone")
                print("2. Display Smartphones")
                print("3. Add Customer")
                print("4. Display Customers")
                print("5. Add Transaction")
                print("6. Display Transactions")
                print("99. Exit")
                choice = int(
                    input(
                        f"Enter your choice {BRIGHT_YELLOW}(1-6 or 99 to exit){RESET}: "
                    )
                )

                if choice == 1:
                    clear()
                    Smartphone.create(Store.smartphones)
                elif choice == 2:
                    clear()
                    Smartphone.view(Store.smartphones)
                elif choice == 3:
                    clear()
                    Customer.create(Store.customers)
                elif choice == 4:
                    clear()
                    Customer.view(Store.customers)
                elif choice == 5:
                    clear()
                    message("Under construction", True)
                elif choice == 6:
                    clear()
                    message("Under construction", True)
                elif choice == 99:
                    clear()
                    message("Exiting System, Goodbye!")
                    break
                else:
                    clear()
                    message("Invalid choice, please try again.", True)
        except ValueError:
            message("Invalid input, please enter a number.", True)
