def header_menu(prompt: str):
    print(prompt)
    print("-" * len(prompt))


def header_product():
    print(f"{'ID':<5} {'Product':<20} {'Stock':<10} {'Price':<15}")


def header_customer():
    print(f"{'ID':<5} {'Name':<20} {'Email':<20}")


def header_transaction():
    print(
        f"{'ID':<5} {'Customer':<10} {'Smartphone':<15} {'Quantity':<10} {'Total':<15}"
    )
