def message(message: str, eror: bool = False):
    if eror:
        print(f"\033[91m{message}\033[0m")
    else:
        print(f"\033[92m{message}\033[0m")
