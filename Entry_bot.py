import time

from selenium import webdriver
from selenium.webdriver.common.by import By

FORM = 'https://forms.gle/ThY6SBDiHWfZ6vaW6'


class Bot():

    def __init__(self):
        self.site = FORM
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.site)

    def Entry(self, add, price, link):
        time.sleep(3)
        self.List = self.driver.find_elements(
            By.CSS_SELECTOR,
            '.Xb9hP input'
            )

        self.address = self.List[0]
        self.price = self.List[1]
        self.link = self.List[2]

        self.address.send_keys(add)
        self.price.send_keys(price)
        self.link.send_keys(link)
        self.Submit()
        self.driver.close()

    def Submit(self):
        self.submit = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
        )
        self.submit.click()




