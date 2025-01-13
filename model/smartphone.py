from utils.colors import *


class Smartphone:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{BRIGHT_BLUE}{self.id:<5} {self.name:<20} {self.stock:<10} Rp {self.price:<15,.2f}{RESET}"

    def update_stock(self, stock: int):
        self.stock += stock

    def is_available(self, stock: int) -> bool:
        return self.stock >= stock
