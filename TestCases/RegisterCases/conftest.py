# -*- coding: UTF-8 -*-
import win32con
import pytest
from selenium import webdriver
from Common.handle_log import HandleLog
from PageObjects.RegisterPage.register_page import RegisterPage
from TestDatas.RegisterDatas import register_datas