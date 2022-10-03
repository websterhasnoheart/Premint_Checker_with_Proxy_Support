import csv
from imp import lock_held
import threading
from prettytable import PrettyTable
from main.premint_check import Premint_Checker


def get_wallet_info():
    wallets = []
    with open('wallets_info.csv') as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        for row in reader:
            wallets.append(row)
    return wallets


def get_raffle_url():
    premint_url = input("Please enter your Premint raffle link: ").split('/')
    https, _, domain, raffle, *end = premint_url
    return f"{https}//{domain}/{raffle}"

    
def premint_check_runner(wallet_info, base_url_with_proxy, table):
    try:
        with Premint_Checker(wallet_info, base_url_with_proxy, teardown=True) as premint_checker:
            premint_checker.verify_wallets()
            lock = threading.Lock()
            lock.acquire()
            results = premint_checker.display_results(table)
            lock.release()
    except Exception as e:
        print(e)
    