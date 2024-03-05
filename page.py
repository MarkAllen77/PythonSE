import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class ClassGoogle:
    def __init__(self, driver):
        self.driver = driver
        self.initsearchinput = "//textarea[@name='q']"

    def openPage(self, url):
        self.driver.get(url)
        time.sleep(2)

    def enterSearchInput(self, searchkeyword):
        # driver.find_element(By.XPATH, "//textarea[@name='q']").send_keys("python 3")
        self.driver.find_element(By.XPATH, self.initsearchinput).send_keys(searchkeyword)
        time.sleep(1)
        action = ActionChains(self.driver)
        action.key_down(Keys.ESCAPE)
        action.key_down(Keys.ENTER)
        action.perform()
        time.sleep(2)
