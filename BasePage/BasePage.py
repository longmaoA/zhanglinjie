#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from BasePage import AppiumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self):
        self.driver = AppiumDriver.AppiumDriver().app_driver()

    def is_element_exist(self, element):
        """
        查看元素是否在当前的Page_source中

        element: 要查找的元素

        :return: True or False

        Usages：is_element_exist(element)
        """
        time.sleep(1)  # 在当前页面停留1s后，打印page_source，增加容错性
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def find_element(self, locator):
        """
        在当前页面找元素，如果找到，返回此元素

        :arg locator

        :return 返回查找到的元素

        Usages：查找元素，输入元组 locator，例如 (By.XPATH, "//*[@text='我的']")
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            self.handle_exception()
            # TODO:不断的查找元素的深度
            # self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        """
        在当前页面找元素，并点击

        :arg locator

        Usages：查找元素并执行点击操作，输入元组 locator，例如 (By.XPATH, "//*[@text='我的']")
        """
        try:
            self.find_element(locator).click()
        except NoSuchElementException:
            self.handle_exception()
            self.find_element(locator).click()

    def find_element_and_input(self, locator, value):
        """
        在当前页面找元素，并点击

        :Arg
        - locator 定位元素的元祖
        - value   要输入的字符串、数字

        Usages：查找元素并执行点击操作，输入元组 locator，输入数据 value
        例如 find_element_and_input((By.XPATH, "//*[@text='我的']"), 1521023)
        """
        try:
            self.find_element(locator).send_keys(value)
        except NoSuchElementException:
            self.handle_exception()
            self.find_element(*locator).send_keys(value)

    # 定义一个黑名单，便于找不到元素时，处理异常弹窗上的元素
    _black_list = [(By.ID, "iv_close")]

    def handle_exception(self):
        """
        找到不元素时，处理可能会出现的异常情况

        Usages：handle_exception()
        """
        print(":Exception")
        # 一旦进入异常处理，则查找元素的隐式等待时间设置为0秒
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            elements = self.driver.find_elements(*locator)

            if len(elements) >= 1:
                # TODO:并不是所有的弹窗处理都需要点击
                elements[0].click()
            else:
                print("\n【%s】 not found !" % str(locator))

            # TODO：page source 会更快的定位元素
            # page_source = self.driver.page_source()
            # if "xxx" in page_source:
            #     self.driver.find_element(*locator).click()
            # elif "yyy" in page_source:
            #     pass

        # 处理完成之后再把隐式时间改回到10s
        self.driver.implicitly_wait(10)
    """
    Usages：在可滑动的控件内，自动滑动页面寻找需要点击的元素，先向上滑动寻找，然后在向下滑动寻找
    
    :arg element_text，例如 swipe_and_click("退出账号")
    """
    def swipe_and_click(self, element_text):
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("'+element_text+'").instance(0));'
        ).click()

    def get_app_width(self):
        width = self.driver.get_window_size()["width"]
        return width

    def get_app_height(self):
        height = self.driver.get_window_size()["height"]
        return height

    def swipe_up(self, t=500, n=1):
        """
        向上滑动屏幕

        :Args
        - t 滑动持续时间，单位毫秒，默认持续时间500毫秒
        - n 循环滑动几次，默认滑动次数为1

        :Usages
        swipe_up(500,3)
        """
        width_and_height = self.driver.get_window_size()
        x1 = width_and_height['width'] * 0.5  # x坐标
        y1 = width_and_height['height'] * 0.75  # 起始y坐标
        y2 = width_and_height['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        """
        向下滑动屏幕

        :Args
        - t 滑动持续时间，单位毫秒，默认持续时间500毫秒
        - n 循环滑动几次，默认滑动次数为1

        :Usages
        swipe_down(500,3)
        """
        width_and_height = self.driver.get_window_size()
        x1 = width_and_height['width'] * 0.5  # x坐标
        y1 = width_and_height['height'] * 0.25  # 起始y坐标
        y2 = width_and_height['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        """
        向左滑动屏幕

        :Args
        - t 滑动持续时间，单位毫秒，默认持续时间500毫秒
        - n 循环滑动几次，默认滑动次数为1

        :Usages
        swipe_left(500,3)
        """
        width_and_height = self.driver.get_window_size()
        x1 = width_and_height['width'] * 0.75
        y1 = width_and_height['height'] * 0.5
        x2 = width_and_height['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        """
        向右滑动屏幕

        :Args
        - t 滑动持续时间，单位毫秒，默认持续时间500毫秒
        - n 循环滑动几次，默认滑动次数为1

        :Usages
        swipe_right(500,3)
        """
        width_and_height = self.driver.get_window_size()
        x1 = width_and_height['width'] * 0.25
        y1 = width_and_height['height'] * 0.5
        x2 = width_and_height['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def smart_find_and_click(self, locator, circle_num=5):
        """
        先向下查找元素，如果发现元素则点击，如果没有发元素，则向上回到初始地点后，继续查找

        :Args
        - locator 要定位的元素，以及定位方法
        - circle_num 循环上下查找几次，默认是5次

        :Usages
        smart_find_and_click((By.XPATH, "//*[@text='退出账号']"), 5)
        """
        i = 0
        if i < circle_num:
            while i < circle_num:
                try:
                    # 尝试点击元素
                    self.find_element(locator).click()
                    break
                except NoSuchElementException:
                    # 滑动屏幕
                    self.swipe_up(1500, 1)
                    i += 1

        if i == circle_num:
            # i归零
            i = 0
            while i < circle_num * 2:
                try:
                    # 尝试点击元素
                    self.find_element(locator).click()
                    break
                except NoSuchElementException:
                    # 滑动屏幕
                    self.swipe_down(1500, 1)
                    i += 1

    def smart_lr_find_click(self, locator, circle_num=5):
        """
        先向右查找元素，如果发现元素则点击，如果没有发元素，则向左回到初始地点后，继续查找

        :Args
        - locator 要定位的元素，以及定位方法
        - circle_num 循环上下查找几次，默认是5次

        :Usages
        smart_lr_find_click((By.XPATH, "//*[@text='退出账号']"), 5)
        """
        i = 0
        if i < circle_num:
            while i < circle_num:
                try:
                    # 尝试点击元素
                    self.find_element(locator).click()
                    break
                except NoSuchElementException:
                    # 滑动屏幕
                    self.swipe_up(1500, 1)
                    i += 1

        if i == circle_num:
            # i归零
            i = 0
            while i < circle_num * 2:
                try:
                    # 尝试点击元素
                    self.find_element(locator).click()
                    break
                except NoSuchElementException:
                    # 滑动屏幕
                    self.swipe_down(1500, 1)
                    i += 1

# class AllureMethods:
#     def __init__(self):
#         self.config = None
#
#     def pytest_sessionfinish(self):
#         """测试完成自动生成并打开allure报告"""
#         if self.config.getoption('allure_report_dir'):
#             try:
#                 # 判断allure在环境路径中，通常意味着可以直接执行
#                 if [i for i in os.getenv('path').split(';') if os.path.exists(i) and 'allure' in os.listdir(i)]:
#                     # 默认生成报告路径为: ./allure-report
#                     os.system(f"allure generate -c {self.config.getoption('allure_report_dir')}")
#                     os.system(f"allure open allure-report")
#                 else:
#                     logger.warn('allure不在环境变量中，无法直接生成html报告！')
#             except Exception as e:
#                 logger.warn(e)
