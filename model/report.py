from datetime import datetime
from utils.clear import clear
from utils.header import header_report
from utils.message import message
from utils.colors import *


class Report:
    def __init__(self):
        pass

    def report_by_date(self, transactions, start_date, end_date):
        clear()
        print(
            f"Sales Report from {BRIGHT_YELLOW}{start_date}{RESET} to {BRIGHT_YELLOW}{end_date}{RESET}\n"
        )

        header_report()
        # Filter transactions by date if start_date and end_date are provided
        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                if start_date > end_date:
                    message("Start date cannot be later than end date.", True)
                    return

            except ValueError:
                message("Invalid date format. Use YYYY-MM-DD.", True)
                return

            transactions = [
                transaction
                for transaction in transactions
                if start_date <= transaction.date <= end_date
            ]

        # Check if transaction list is empty
        if not transactions:
            message(
                "Transaction list is empty or no transactions match the date filter.",
                True,
            )
            return

        # Display transaction list
        total_sales = 0
        for transaction in transactions:
            total = transaction.smartphone.price * transaction.quantity
            total_sales += total
            print(
                f"{BRIGHT_BLUE}{transaction.id:<5} {transaction.customer.name:<15} "
                f"{transaction.smartphone.name:<25} {transaction.quantity:<10} "
                f"Rp {total:<15,.2f}{RESET}"
            )

        print(f"\n{BRIGHT_GREEN}Total Sales: Rp {total_sales:<15,.2f}{RESET}")

    @staticmethod
    def filter(transactions):
        while True:
            try:
                start_date = input(
                    f"Enter start date {BRIGHT_YELLOW}(YYYY-MM-DD){RESET}: "
                )
                end_date = input(f"Enter end date {BRIGHT_YELLOW}(YYYY-MM-DD){RESET}: ")

                Report().report_by_date(transactions, start_date, end_date)
                break
            except ValueError:
                message("Invalid date format. Use YYYY-MM-DD.", True)
