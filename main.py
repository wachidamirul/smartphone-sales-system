from model.store import Store
from utils.message import message
from utils.clear import clear


def main():
    store = Store()

    while True:
        print("\n====== Menu ======")
        print("1. Add Smartphone")
        print("2. Display Smartphones")
        print("3. Add Customer")
        print("4. Display Customers")
        print("99. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            store.add_smartphone()
        elif choice == "2":
            clear()
            store.display_smartphones()
        elif choice == "3":
            clear()
            store.add_customer()
        elif choice == "4":
            clear()
            store.display_customers()
        elif choice == "99":
            clear()
            message("Exiting System, Goodbye!")
            break
        else:
            clear()
            message("Invalid choice, please try again.", True)


if __name__ == "__main__":
    main()
