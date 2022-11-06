import csv
from imp import lock_held
import threading
from prettytable import PrettyTable
from main.premint_check import Premint_Checker
import random

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
    
    
def get_single_wallet():
    with open('wallets_info.csv') as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        wallets = [row['wallet_address'] for row in reader]
        wallet_count = len(wallets)
        wallet_index = random.randint(1, wallet_count)
        return wallets[wallet_index]


def get_raffle_urls():
    base_urls = []
    raffle_file = open('raffle_urls.txt', 'r')
    raffle_entries = raffle_file.readlines()
    for raffle_url in raffle_entries:
        url = raffle_url.split('/')
        https, _, domain, raffle, *end = url
        base_url = f"{https}//{domain}/{raffle}" 
        base_urls.append(base_url)
    return base_urls
