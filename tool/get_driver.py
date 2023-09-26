
from  selenium import webdriver
# 导包appium

from appium import webdriver

import page

class GetDriver:
    # 首先是声明变量
    _web_driver = None
    _app_driver =None
    # 然后再获取driver变量 为了不用进行类名实例化，将方法修饰为类名方法
    @classmethod
    def get_web_driver(cls,url):
        if cls._web_driver is None:
            # 获取浏览器
            cls._web_driver = webdriver.Edge()
            # 最大化浏览器
            cls._web_driver.maximize_window()
            # 获取页面操作
            cls._web_driver.get(url)
        return  cls._web_driver

        # 判断_web_driver 是不是为空，为空就创建driver 不为空就
        pass

    # 退出driver 方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver 不为空
        if cls._web_driver:
            #退出操作
            cls._web_driver.quit()
            # 置空操作
            cls._web_driver = None


    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断app_driver 是不是为空
        if cls._app_driver is None:
            #设置启动页面
            desired_caps = {}
            # 必填
            desired_caps['platformName']='Android'
            desired_caps['platformName']='5.1'
            # 必填
            desired_caps['deviceName']='192.168.56.101:5555'
            # app包名
            desired_caps['appPackage']= page.appPackage
            # 启动名
            desired_caps['appActivity']=page.appActivity
            # 设置driver
            cls._app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        return cls._web_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls._app_driver:
            # 退出操作
            cls._app_driver.quit()
            # 置空操作
            cls._app_driver = None
            


