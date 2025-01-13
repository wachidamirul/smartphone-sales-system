from utils.message import message
from utils.clear import clear


def main():
    while True:
        print("\n====== Menu ======")
        print("1. Add Store")
        print("2. Display Stores")
        print("99. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            message("Add Store")
        elif choice == "2":
            clear()
            message("Display Stores")
        elif choice == "99":
            clear()
            message("Exiting System, Goodbye!")
            break
        else:
            clear()
            message("Invalid choice, please try again.", True)


if __name__ == "__main__":
    main()
