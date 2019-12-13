import allure
import pytest
from Login.LoginPage import LoginPage

"""
@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
with allure.step # 用于将一个测试用例，分成几个步骤在报告中输出
allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
@pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
"""


@allure.feature('APP登录功能')
class TestLogin:

    login_page = LoginPage.LoginPage()

    @allure.title("测试用例：账号密码登录虎嗅APP")
    @allure.description("用例描述：使用账号密码的登录方式，登录虎嗅APP")
    @allure.story("使用账号密码登录")
    @allure.severity(allure.severity_level.BLOCKER)
    # @allure.step("第一步：登录APP")
    @pytest.mark.dependency()
    # @pytest.mark.run(order=2)
    def test_account_login(self, account="15210239410", password="13271353615"):

        with allure.step("点击我的"):
            self.login_page.click_me()
        with allure.step("点击登录注册"):
            self.login_page.click_login_and_register()
        with allure.step("点击账号密码登录"):
            self.login_page.click_account()
        with allure.step("输入账号"):
            allure.attach("账号", account)
            self.login_page.input_account(account)
        with allure.step("输入密码"):
            allure.attach("密码", password)
            self.login_page.input_password(password)
        with allure.step("确认登录"):
            self.login_page.click_login()
        with allure.step("断言是否登录成功！"):
            self.login_page.assert_login()

    @allure.title("测试用例：账号退出虎嗅APP")
    @allure.description("用例描述：进入APP设置，退出虎嗅APP")
    @allure.story("退出登录")
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step("第二步：退出登录")
    @pytest.mark.dependency(depends=['TestLogin::test_account_login'])
    # @pytest.mark.run(order=1)
    def test_sign_out(self):

        with allure.step("点击我的"):
            self.login_page.click_me()
        with allure.step("点击设置"):
            self.login_page.click_setting()
        with allure.step("点击退出登录"):
            self.login_page.click_sign_out()
        with allure.step("点击确认"):
            self.login_page.click_confirm()

    def teardown(self):
        # self.login_page.driver.quit()
        pass
