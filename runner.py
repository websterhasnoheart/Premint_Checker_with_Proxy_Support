from utils import get_wallet_info, get_raffle_url, premint_check_runner
from prettytable import PrettyTable
from concurrent.futures import ThreadPoolExecutor
import time
import yaml

config = open('./config.yaml', 'r', encoding='utf-8')
data = yaml.load(config, Loader=yaml.FullLoader)
max_worker = data['max_worker']
config.close()
thread_pool = ThreadPoolExecutor(max_workers=max_worker)
table = PrettyTable(
    field_names=["Wallet Name", "Wallet", "Result", "Balance"]
)
wallet_count = 0

try:
    wallets_info = get_wallet_info()
    base_url = get_raffle_url()
    begin_time = time.time()
    
    for wallet_info in wallets_info:
        thread_pool.submit(premint_check_runner, wallet_info, base_url, table)
        wallet_count += 1
    thread_pool.shutdown(wait=True)
    end_time = time.time()
    print(table)
    print("Raffle result checking completed, <" +  str(wallet_count) + "> wallets have been checked, " ,"congrats if you won!")
    print("Execution time:" + str(round(end_time - begin_time, 2)) + "s" +"\n")
    
except Exception as e:
    print(e)

input("Press any key to exit")