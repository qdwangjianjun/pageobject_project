import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.basepage import BasePage

class ProfilePage(BasePage):
    def gotoLogin(self):
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@text='点击登录']")))
        time.sleep(2)
        self.find_ByText("点击登录").click()
        from page.loginpage import LoginPage
        return LoginPage()

    def backtohome(self):
        self.driver.back()
        from page.mainpage import MainPage
        return MainPage()

