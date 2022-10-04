# Premint raffle result checker with proxies support
The original repo : `https://github.com/websterhasnoheart/premint_checker`

## 1. Introduction
- The script is created to check the premint raffle results.
- A template for filling in wallet addresses is provided as wallets_info.csv (please do not change the name of the csv file)
- Improvements were made to adapt the authors’ situation
- Wallet balance will also be checked
- You need to buy proxies for your own

## 2. Requirement

- `Python 3.8`
- `web3.py`
- `selenium`
- `prettytable`
- `webdriver_manager`

## 3. Installation

1. Git clone `git@github.com:websterhasnoheart/Premint_Checker_with_Proxy_Support.git`
2. cd `Premint_Checker_with_Proxy_Support`
3. `py run.py`
4. input `premint link` eg : [`https://www.premint.xyz/Luskorpnft/`](https://www.premint.xyz/Luskorpnft/)

### 4. Manual
- Fill in your wallet name(customized) and address into csv file
- Fill in your IP address (1-ip-to-1-wallet for preventing anti-bots measurement)
- Fill in the username and password of proxies(You should get them from proxy sellers)
- Fill in the raffle link on command line
- Sit back and check your raffle results

### 5. Warning
- Premint is busting their asses to eliminate bots, so please use this version instead of the old one to check your raffle results, you could never be careful enough.

![image](https://user-images.githubusercontent.com/66870019/193582588-5eecaddf-21d5-4b16-bb83-b1f61b4f3949.png)

### 6. Update log
- `04/10/2022` The bot now support both socks5 and http proxy types now