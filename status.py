from prettytable import PrettyTable
from main.premint_status_check import Premint_Status

with Premint_Status(teardown=True) as status_checker:
    status_checker.raffle_status_check()
    status_checker.display_results()