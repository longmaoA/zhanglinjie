from selenium.webdriver.common.by import By
from BasePage import BasePage


class LoginPage(BasePage.BasePage):

    # 元素单独拿出来便于复用
    # 变量前面加下划线，类里面的私有变量
    _click_me = (By.XPATH, "//*[@text='我的']")
    _click_login_and_register = (By.XPATH, "//*[@text='登录 / 注册']")
    _click_account = (By.XPATH, "//*[@text='账号密码登录']")
    _input_account = (By.XPATH, "//*[@text='手机号/邮箱/账户名']")
    _input_password = (By.XPATH, "//*[@text='密码']")
    _click_login = (By.XPATH, "//*[@text='登 录']")
    _click_setting = (By.ID, "iv_setting")
    _click_confirm = (By.XPATH, "//*[@text='确定']")

    def click_me(self):
        self.find_element_and_click(self._click_me)
        return self

    def click_login_and_register(self):
        self.find_element_and_click(self._click_login_and_register)
        return self

    def click_account(self):
        self.find_element_and_click(self._click_account)
        return self

    def input_account(self, account):
        self.find_element_and_input(self._input_account, account)
        return self

    def input_password(self, password):
        self.find_element_and_input(self._input_password, password)
        return self

    def click_login(self):
        self.find_element_and_click(self._click_login)
        return self

    def assert_login(self):
        assert self.is_element_exist("评论")

    def click_setting(self):
        self.find_element_and_click(self._click_setting)
        return self

    def click_sign_out(self):
        # 自动滑动页面寻找需要点击的元素，先向上滑动寻找，然后在向下滑动寻找
        self.swipe_and_click("退出账号")
        return self

    def click_confirm(self):
        self.find_element_and_click(self._click_confirm)
        return self

    def print_width(self):
        print(self.get_app_width())
