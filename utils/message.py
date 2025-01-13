from utils.colors import *


def message(message: str, eror: bool = False):
    if eror:
        print(f"{BRIGHT_RED}{message}{RESET}")
    else:
        print(f"{BRIGHT_GREEN}{message}{RESET}")
