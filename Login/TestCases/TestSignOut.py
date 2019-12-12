import allure
from Login.LoginPage import LoginPage


@allure.title("退出登录用例")
@allure.description("这条用例主要任务是，推出虎嗅APP！")
def test_account_sign_out():

    login_page = LoginPage.LoginPage()

    login_page.click_setting()
    login_page.click_sign_out()
    login_page.click_confirm()



