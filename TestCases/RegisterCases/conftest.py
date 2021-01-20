# -*- coding: UTF-8 -*-
import win32api
import win32con
import pytest
from selenium import webdriver
from Common.handle_log import HandleLog
from PageObjects.LoginPage.login_page import LoginPage
from PageObjects.RegisterPage.register_page import RegisterPage
from TestDatas.CommonDatas import common_datas as ce
from TestDatas.LoginDatas.login_datas import login_user as cd


@pytest.fixture(scope='module')  # 测试继承的关系说明
def access_web():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def register_web(access_web):
    driver = access_web
    driver.get(ce.login_url)
    LoginPage(driver).login(cd['membMobile'], cd['membPassword'])
    Register = RegisterPage(driver)
    yield driver, Register
