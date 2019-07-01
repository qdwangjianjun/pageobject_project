from page.basepage import BasePage
from page.mainpage import MainPage


class APP(BasePage):
    @classmethod
    def app_home(cls):
        cls.get_client().restart_app()
        return MainPage()


