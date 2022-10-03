from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Result_Checker:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def land_page(self, url):
        self.driver.get(url)

    def check_win(self):
        card = self.driver.find_element(By.CLASS_NAME, "card")
        try:
            # The emoji extraction might fail
            emoji = card.find_element(By.CLASS_NAME, "heading-1").text
        except:
            emoji = ""
        text = card.find_element(By.CLASS_NAME, "heading-3").text
        result = emoji + text
        return result
