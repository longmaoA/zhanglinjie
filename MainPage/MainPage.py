from BasePage import BasePage
from selenium.webdriver.common.by import By
from Login.LoginPage.LoginPage import LoginPage


class MainPage(BasePage.BasePage):

    _click_me = (By.XPATH, "//*[@text='我的']")
    _click_search = (By.ID, "fl_search")

    def to_search(self):
        self.find_element_and_click(self._click_search)

    def to_login(self):
        self.find_element_and_click(self._click_me)
        return LoginPage
