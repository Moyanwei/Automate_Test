# -*- coding: UTF-8 -*-
import win32con
import pytest
from selenium import webdriver
from Common.handle_log import HandleLog
from PageObjects.RegisterPage.register_page import RegisterPage
from TestDatas.RegisterDatas import register_datas
from py._xmlgen import html


@pytest.fixture(scope='class')
def access_web():
    driver = webdriver.Chrome()
    driver.get(cd.login_url)

    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def login_web(access_web):  # 继承了access_web的前置后置。作为参数，函数名称就是返回值
    login_page = LoginPage(access_web)

    yield access_web, login_page


@pytest.fixture()
def init_driver():
    """
     前置,打开谷歌浏览器，访问web网址
   """
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()

    driver.implicitly_wait(30)
    # 分割线 + 返回值
    yield driver


@pytest.fixture
def login_driver(init_driver):
    login_page = LoginPage(init_driver)

    case_log = HandleLog(logger_name='Case').get_logger()
    case_log.info('{:=^40s}'.format('开始执行测试'))
    # 获取屏幕尺寸
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

    yield login_page

    case_log.info('{:=^40s}'.format('用例执行结束'))
    init_driver.quit()