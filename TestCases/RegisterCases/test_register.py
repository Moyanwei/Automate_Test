# coding: utf-8
import pytest
import allure
from TestDatas.RegisterDatas import register_datas


@allure.feature('注册功能')
@allure.issue('https://oms.sdhwlw.com/')
@pytest.mark.login
@pytest.mark.usefixtures('register_driver')
class TestRegister:
    @allure.story('注册信息填写完整-注册成功')
    @allure.severity('normal')
    @pytest.mark.parametrize('data', register_datas.normal_data)
    def test_register01(self, data, register_driver):
        """
        注册功能
        :param data: 测试数据
        :param register_driver: 注册函数
        :return:
        步骤：
        登录页面-输入用户名- membMobile: 15649909501
        登录页面-输入密码- membPassword: 123456
        登录页面-点击登录按钮
        页面跳转至注册信息填写界面-填写注册认证信息
        断言-首页-获取注册界面（提交）按钮元素，确认元素是否存在
        """
        with allure.step('1.公司名称:{}'
                         '2.社会信用代:{}'
                         '3.联系人:{}'
                         '4.联系电话:{}'
                         '5.详细地址:{}'
                         '6.发票抬头:{}'
                         '7.税号:{}'
                         '8.开户行:{}'
                         '9.银行账号:{}'
                         '10.点击-提交'.format(data['companyName'], data['LicenseNo'], data['linkMan'],
                                           data['contactNumber'], data['detail'], data['invoiceTitle'],
                                           data['dutyParagraph'], data['bankOfDeposit'], data['bankAccount'])):
            register_driver.register(data['companyName'], data['LicenseNo'], data['linkMan'],
                                     data['contactNumber'], data['detail'], data['invoiceTitle'],
                                     data['dutyParagraph'], data['bankOfDeposit'], data['bankAccount'])
            assert register_driver.submit_is_exist()
