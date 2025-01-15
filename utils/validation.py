from utils.input_utils import input_int
from utils.message import message


def get_valid_id(prompt, items, item_name):
    while True:
        item_id = input_int(prompt, 0)
        if 0 < item_id <= len(items):
            return item_id
        message(f"{item_name} does not exist. Please try again.", True)


def get_valid_quantity(prompt, max_quantity):
    while True:
        quantity = input_int(prompt, 0)
        if 0 < quantity <= max_quantity:
            return quantity
        message(
            f"Quantity must be between 1 and {max_quantity}. Please try again.",
            True,
        )
