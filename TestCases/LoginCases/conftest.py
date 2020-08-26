# -*- coding: UTF-8 -*-
import win32api
import win32con
import pytest
from selenium import webdriver
from Common.handle_log import HandleLog
from PageObjects.index_page.index_page import IndexPage
from PageObjects.LoginPage.login_page import LoginPage
from TestDatas.CommonDatas import common_datas as cd
from py._xmlgen import html


@pytest.fixture(scope='class') # 测试继承的关系说明
def access_web():
    # case_log.info('{:=^80s}'.format('Test Start'))
    driver = webdriver.Chrome()
    driver.get(cd.login_url)

    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def login_web(access_web):   # 继承了access_web的前置后置。作为参数，函数名称就是返回值
    login_page = LoginPage(access_web)
    index_page = IndexPage(access_web)

    yield access_web, login_page, index_page


@pytest.fixture
def init_driver():
    """
     前置
     打开谷歌浏览器，访问web网址
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
    index_page = IndexPage(init_driver)

    case_log = HandleLog(logger_name='Case').get_logger()
    case_log.info('{:=^40s}'.format('开始执行测试'))
    # 获取屏幕尺寸
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CXSCREEN))
    case_log.info(win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

    yield (login_page, index_page)

    case_log.info('{:=^40s}'.format('用例执行结束'))
    init_driver.quit()

def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "OMS-UI自动化测试项目v1.0"
    config._metadata['接口地址'] = 'https://api.sdhwlw.com/'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 质量管理部门QA")])
    prefix.extend([html.p("测试人员: 阿木木")])
