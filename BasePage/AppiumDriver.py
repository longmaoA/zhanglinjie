from appium import webdriver
from BasePage.AppiumSever import AppiumSever
from selenium.webdriver.remote.webdriver import WebDriver


class AppiumDriver:

    driver: WebDriver = None

    def __init__(self):
        self.start_sever = AppiumSever().start_appium_sever

    def app_driver(self, port=4725):
        # 启动APPIUM sever，并给sever传递一个端口号
        self.start_sever(port)

        caps = {
            'platformName': 'Android',
            'deviceName': '诺基亚',
            'appPackage': 'com.huxiu',
            'appActivity': '.ui.activity.SplashActivity',
            'automationName': 'uiautomator2',
            'autoGrantPermissions': True,
            'printPageSourceOnFindFailure': True,
            'newCommandTimeout': '66',
            'chromedriverExecutable': '/Users/PycharmProjects/System/Mobile/Mini/chromedriver_240',
            'neReset': True,
            # 'fullReset': False,
            # 'unicodeKeyboard': True,
            # 'resetKeyboard': True,
            # 'chromeOptions': {
            #     'androidProcess': 'com.tencent.mm:appbrand0'
            #           }
        }
        driver = webdriver.Remote("http://localhost:" + str(port) + "/wd/hub", caps)
        driver.implicitly_wait(10)  # 智能等待 10 秒
        return driver

    def quit_driver(self):
        self.driver.quit()
