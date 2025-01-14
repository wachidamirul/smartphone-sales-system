from model.customer import Customer
from model.smartphone import Smartphone
from model.store import Store


def sample_data():
    Store.smartphones = [
        Smartphone(1, "iPhone 13", 5000000, 10),
        Smartphone(2, "Samsung Galaxy S21", 4000000, 15),
        Smartphone(3, "Google Pixel 6", 3000000, 20),
    ]

    Store.customers = [
        Customer(1, "Budi", "budi@mail.com"),
        Customer(2, "Joko", "joko@mail.com"),
        Customer(3, "Rina", "rina@mail.com"),
    ]


def main():
    sample_data()
    Store.menu()


if __name__ == "__main__":
    main()
