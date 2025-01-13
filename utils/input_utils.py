from utils.message import message


def input_float(prompt: str, min_value: float):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                message(f"Value must be at least {min_value}. Please try again.", True)
            else:
                return value
        except ValueError:
            message("Invalid input. Please enter a valid number.", True)


def input_int(prompt: str, min_value: int):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                message(f"Value must be at least {min_value}. Please try again.", True)
            else:
                return value
        except ValueError:
            message("Invalid input. Please enter a valid integer.", True)


def input_string(prompt: str, allow_empty: bool = False):
    while True:
        value = input(prompt).strip()
        if not value and not allow_empty:
            message("Input cannot be empty. Please try again.", True)
        else:
            return value
