from utils.message import message


def input_float(prompt: str, min_value: float):
    return _input_value(prompt, float, min_value, "number")


def input_int(prompt: str, min_value: int):
    return _input_value(prompt, int, min_value, "integer")


def input_string(prompt: str, allow_empty: bool = False):
    while True:
        value = input(prompt).strip()
        if not value and not allow_empty:
            message("Input cannot be empty. Please try again.", True)
        else:
            return value


def _input_value(prompt: str, value_type, min_value, value_name: str):
    while True:
        try:
            value = value_type(input(prompt))
            if min_value is not None and value < min_value:
                message(f"Value must be at least {min_value}. Please try again.", True)
            else:
                return value
        except ValueError:
            message(f"Invalid input. Please enter a valid {value_name}.", True)
