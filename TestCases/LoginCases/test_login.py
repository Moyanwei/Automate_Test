# coding: utf-8
import pytest
import allure
from TestDatas.LoginDatas import login_datas


@allure.feature('登录模块')
@allure.issue('https://oms.sdhwlw.com/')
@pytest.mark.login
@pytest.mark.usefixtures('login_driver')  # 调用（执行）了login_driver这个函数

class TestLogin:
    @allure.story('用户名和密码正确-登录成功')
    @allure.severity('normal')
    @pytest.mark.parametrize('data', login_datas.oms_success_data)
    def test_login01(self, data, login_driver):
        """
        :param data:测试数据
        :param login_driver:登录函数
        :return: login_driver如果没有返回值，就不需要传参
        步骤：
        登录页面-输入用户名- membMobile: 15649909501
        登录页面-输入密码- membPassword: 123456
        登录页面-点击登录按钮
        断言-首页-获取用户元素，确认是否存在
        """
        with allure.step('1.输入用户名：{}。 '
                         '2.输入密码：{}。 '
                         '3.点击登录'.format(data['membMobile'], data['membPassword'])):
            login_driver[0].login(data['membMobile'], data['membPassword'])
        assert login_driver[1].if_user_is_exist()

    @allure.story('用户名和密码异常-登录失败')
    # @pytest.mark.flaky(reruns=2, reruns_delay=5)
    @pytest.mark.parametrize('data', login_datas.error_passwordFormat_data)
    def test_login02(self, data, login_driver):
        """
        :param data:测试数据
        :param login_driver:登录函数
        :return: login_driver如果没有返回值，就不需要传参
        步骤：
        登录页面-获取错误提示信息-用户名和密码异常-登录失败
        断言-登录界面-获取错误提示信息，获取提示语的text
        """
        with allure.step('1.输入用户名：{}。 '
                         '2.输入密码：{}。 '
                         '3.点击登录'.format(data['membMobile'], data['membPassword'])):
            try:
                img_doc = data['dataName']
                login_driver[0].login(data['membMobile'], data['membPassword'])
                assert data['errorMsg'] == login_driver[0].get_err()
            except Exception as e:
                login_driver[0].save_screen_shoot(img_doc)
                raise e

