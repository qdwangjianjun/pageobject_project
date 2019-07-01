from selenium.webdriver.common.by import By
from page.basepage import BasePage
from page.profilepage import ProfilePage


class MainPage(BasePage):
    _profile_button=(By.ID, "user_profile_icon")

    def gotoProfile(self):
        self.find(MainPage._profile_button).click()
        return ProfilePage()