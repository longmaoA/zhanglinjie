#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import platform


class AppiumSever:
    # 获取当前系统
    _system_name = platform.system()

    def stop_appium_sever(self, post_num):
        """
        关闭appium服务
        """
        if self._system_name == 'Windows':
            p = os.popen(f'netstat -aon | findstr {post_num}')
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])  # 获取进程号
                os.popen(f'taskkill /F /PID {p1}')  # 结束进程
                print('\nAppium server 已结束\n')
        elif self._system_name == 'Darwin':
            p = os.popen(f'lsof -i tcp:{post_num}')
            p0 = p.read()
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen(f'kill {p1}')  # 结束进程
                print('\nAppium server 已结束\n')

    def start_appium_sever(self, post_num):
        """
        开启appium服务
        """
        # 先判断端口是否被占用，如果被占用则关闭该端口号
        self.stop_appium_sever(post_num)
        # 根据系统，启动对应的服务
        cmd_dict = {
            'Windows': f' start /b appium -a 127.0.0.1 -p {post_num} --session-override --no-reset --local-timezone',
            'Darwin': f'appium -a 127.0.0.1 -p {post_num} --session-override --no-reset --local-timezone &'
        }
        os.system(cmd_dict[self._system_name])
        time.sleep(3)  # 等待启动完成
        print('\n Appium sever 启动成功!\n')
