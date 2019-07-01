import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.basepage import BasePage
from page.profilepage import ProfilePage


class LoginPage(BasePage):
    _close_locator=(By.ID, "iv_close")
    _other_locator=(By.ID, "tv_login_by_phone_or_others")
    _register_phone_number=(By.ID, "register_phone_number")
    _register_code=(By.ID, "register_code")
    _button_next=(By.ID, "button_next")
    _tv_login_with_account=(By.ID, "tv_login_with_account")
    _login_account=(By.ID, "login_account")
    _login_password=(By.ID, "login_password")
    _close2_locator=(By.ID, "iv_action_back")
    _error_msg=(By.ID, "md_content")
    # _back_locator=(By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")
    _back_locator=(By.XPATH, "//*[contains(@resource-id,'sky_container')]//*[contains(@resource-id,'iv_action_back')]")

    def login_phone(self,phonenumber,key):
        self.find(LoginPage._other_locator).click()
        self.find(LoginPage._register_phone_number).send_keys(phonenumber)
        self.find(LoginPage._register_code).send_keys(key)
        self.find(LoginPage._button_next).click()
        return self
    def login_account(self,account,password):
        self.find(LoginPage._other_locator).click()
        self.find(LoginPage._tv_login_with_account).click()
        self.find(LoginPage._login_account).send_keys(account)
        self.find(LoginPage._login_password).send_keys(password)
        self.find(LoginPage._button_next).click()
        return self

    def getErrorMsg(self):
        msg=self.find(LoginPage._error_msg).text
        self.find_ByText("确定").click()
        return msg

    def backward(self):
        # self.driver.back()
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(LoginPage._back_locator))
        time.sleep(2)
        self.find(LoginPage._back_locator).click()
        return ProfilePage()


