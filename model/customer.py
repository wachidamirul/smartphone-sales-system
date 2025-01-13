class Customer:

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"\033[94m{self.id:<5} {self.name:<20} {self.email:<20}\033[0m"
