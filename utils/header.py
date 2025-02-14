def header_menu(prompt: str):
    print(prompt)
    print("-" * len(prompt))


def header_product():
    print(f"{'ID':<5} {'Product':<25} {'Stock':<10} {'Price':<15}")


def header_customer():
    print(f"{'ID':<5} {'Name':<15} {'Email':<20}")


def header_transaction():
    print(
        f"{'ID':<5} {'Date':<25} {'Customer':<15} {'Smartphone':<25} {'Quantity':<10} {'Total':<15} {'Cashier':>10}"
    )


def header_report():
    print(
        f"{'ID':<5} {'Date':<25} {'Customer':<15} {'Smartphone':<25} {'Quantity':<10} {'Total':<15} {' Cashier':<5}"
    )


def header_cashier():
    print(f"{'ID':<5} {'Name':<15}")
