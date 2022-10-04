import os
from seleniumwire import webdriver
from prettytable import PrettyTable
from main.result_check import Result_Checker
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from web3 import Web3, HTTPProvider


class Premint_Checker(webdriver.Chrome):
    def __init__(self, wallet, proxy_url, teardown=False):
        self.teardown = teardown
        self.base_url = proxy_url
        self.wallet_name = wallet['wallet_name']
        self.wallet_address = wallet['wallet_address']
        self.host = wallet['host']
        self.port = wallet['port']
        self.username = wallet['username']
        self.password = wallet['password']
        self.results = []
        self.endpoint = 'https://geth.mytokenpocket.vip'
        self.connection = Web3(HTTPProvider(self.endpoint))
        self.selenium_wire_storage = os.path.join(".", "selenium_wire")
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')

        options_seleniumWire = {
            'proxy': {
                'https': f'http://{self.username}:{self.password}@{self.host}:{self.port}',
                'http': f'http://{self.username}:{self.password}@{self.host}:{self.port}',
            },
            'request_storage_base_dir': self.selenium_wire_storage
        }
        
        super(Premint_Checker, self).__init__(chrome_options=chrome_options, seleniumwire_options=options_seleniumWire, service=ChromeService(ChromeDriverManager().install()))
        self.maximize_window()
        self.implicitly_wait(10)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
                
    def verify_wallets(self):
        print("Fetching results for wallet: <" + self.wallet_name + ">" + "\n")
        try:
            wallet_name = self.wallet_name
            wallet_address = self.wallet_address
            url = f"{self.base_url}/verify/?wallet={wallet_address}"
            balance = round(self.connection.fromWei(self.connection.eth.getBalance(wallet_address, 'latest'), 'ether'), 3)

            verify = Result_Checker(self)
            verify.land_page(url)
            phrase = verify.check_win()
            result = [wallet_name, wallet_address, phrase, balance]
            self.results.append(result)

        except Exception as e:
            self.get_screenshot_as_file("screenshot.png")
            print(e)

    def display_results(self, table):
        table.add_rows(self.results)
        return self.results