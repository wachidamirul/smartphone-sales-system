import random


def generate_imei(smartphones) -> int:
    while True:
        imei = random.randint(100000000000000, 999999999999999)
        if not any(smartphone.imei == imei for smartphone in smartphones):
            return imei
