from selenium import webdriver
from prettytable import PrettyTable
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from web3 import Web3, HTTPProvider
from main.result_check import Result_Checker
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from utils import get_raffle_urls, get_single_wallet


class Premint_Status(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        self.raffle_urls = get_raffle_urls()
        self.wallet_address = get_single_wallet()
        self.results = []
        self.endpoint = 'https://geth.mytokenpocket.vip' # Replace this with your own provider if it does not work
        self.connection = Web3(HTTPProvider(self.endpoint))
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')
        
        super(Premint_Status, self).__init__(chrome_options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
        self.maximize_window()
        self.implicitly_wait(10)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
            
    def raffle_status_check(self):
        print("Fetching results. Please wait...")
        index = 0
        try:
            for raffle_url in self.raffle_urls:
                index += 1
                url = f"{raffle_url}/verify/?wallet={self.wallet_address}"
                verify = Result_Checker(self)
                verify.land_page(url)
                phrase = verify.check_win()
                result = [index, raffle_url, phrase]
                self.results.append(result)
        except Exception as e:
            self.get_screenshot_as_file("screenshot.png")
            print(e)
    
    def display_results(self):
        table = PrettyTable(field_names=["Index", "Raffle URL", "Status"])
        table.add_rows(self.results)
        print(table)