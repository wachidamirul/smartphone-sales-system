from model.customer import Customer
from model.smartphone import Smartphone
from model.store import Store
from model.transaction import Transaction
from model.cashier import Cashier


def sample_data():
    Store.smartphones = [
        Smartphone(1, "iPhone 13", 5000000, 10),
        Smartphone(2, "Samsung Galaxy S21", 4000000, 2),
        Smartphone(3, "Google Pixel 6", 3000000, 20),
    ]

    Store.customers = [
        Customer(1, "Budi", "budi@mail.com"),
        Customer(2, "Joko", "joko@mail.com"),
        Customer(3, "Rina", "rina@mail.com"),
    ]

    Store.cashiers = [
        Cashier(1, "Alice"),
        Cashier(2, "Bob"),
    ]

    Store.transactions = [
        Transaction(
            1,
            "2025-01-05 10:02:50",
            Store.customers[0],
            Store.smartphones[1],
            2,
            Store.cashiers[0],
        ),
    ]

    # Update stock
    Store.transactions[0].smartphone.update_stock(2)


def main():
    sample_data()
    Store.menu()


if __name__ == "__main__":
    main()
