def main():
    while True:
        print("\n====== Menu ======")
        print("1. Add Store")
        print("2. Display Stores")
        print("99. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdd Smartphone")
        elif choice == "2":
            print("\nDisplay Smartphone")
        elif choice == "99":
            print("Exiting System, Goodbye!")
            break
        else:
            print("Invalid choice, please try again.", True)


if __name__ == "__main__":
    main()
