from utils.colors import *


def message(message: str, error: bool = False):
    color = BRIGHT_RED if error else BRIGHT_GREEN
    print(f"{color}{message}{RESET}")
