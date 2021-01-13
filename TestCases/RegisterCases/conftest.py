# -*- coding: UTF-8 -*-
import win32api
import win32con
import pytest
from selenium import webdriver
from Common.handle_log import HandleLog
from PageObjects.LoginPage.login_page import LoginPage
from PageObjects.RegisterPage.register_page import RegisterPage
from TestDatas.CommonDatas import common_datas as cd
from py._xmlgen import html


@pytest.fixture(scope='class')
def access_web():
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    LoginPage(driver).login(*cd.login_user)
    login_page = LoginPage(driver)
    register_page = RegisterPage(driver)

    yield driver, login_page, register_page


# @pytest.fixture(scope='class')
# def register_web(access_web):  # 继承了access_web的前置后置。作为参数，函数名称就是返回值
#     login_page = LoginPage(access_web)
#     register_page = RegisterPage(access_web)
#
#     yield register_page, login_page

@pytest.fixture
def register_driver(access_web):
    register_page = RegisterPage(access_web)

    case_log = HandleLog(logger_name='Case').get_logger()
    case_log.info('{:=^40s}'.format('开始执行测试'))
    # 获取屏幕尺寸
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

    yield register_page

    case_log.info('{:=^40s}'.format('用例执行结束'))


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 质量管理部门QA")])
    prefix.extend([html.p("测试人员: 阿木木")])