from appium.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException

from driver.AndroidClient import AndroidClient


class BasePage(object):

    def __init__(self):
        self.driver = BasePage.get_driver()

    @classmethod
    def get_driver(cls):
        return AndroidClient.driver

    @classmethod
    def get_client(cls):
        return AndroidClient

    def find(self, kv)->WebElement:
        return self.driver.find_element(*kv)

    def find_ByText(self, text)->WebElement:
        return self.driver.find_element_by_xpath("//*[contains(@text,'%s')]" % text)

    def iselementexist(self, locator) -> bool:
        try:
            self.find(locator)
            return True
        except NoSuchElementException:
            return False