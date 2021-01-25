# coding: utf-8
import pytest
from TestDatas.RegisterDatas import register_datas as REG


@pytest.mark.usefixtures('register_web')
class TestRegister:
    def test_register01(self, register_web):
        register_web[1].register(REG.abnormal_data['companyName'], REG.abnormal_data['LicenseNo'],
                                 REG.abnormal_data['linkMan'], REG.abnormal_data['contactNumber'],
                                 REG.abnormal_data['detail'], REG.abnormal_data['invoiceTitle'],
                                 REG.abnormal_data['dutyParagraph'], REG.abnormal_data['bankOfDeposit'],
                                 REG.abnormal_data['bankAccount'], REG.abnormal_data['file_path1'],
                                 REG.abnormal_data['file_path2'], REG.abnormal_data['file_path3'])
        assert REG.abnormal_data['errorMsg'] == register_web[1].get_err()

    def test_register02(self, register_web):
        """
        注册功能
        :param data: 测试数据
        :param register_web: 注册函数
        :return:
        步骤：
        登录页面-输入用户名- membMobile: 15649909501
        登录页面-输入密码- membPassword: 123456
        登录页面-点击登录按钮
        页面跳转至注册信息填写界面-填写注册认证信息
        断言-首页-获取注册界面（提交）按钮元素，确认元素是否存在
        """
        register_web[1].register(REG.normal_data['companyName'], REG.normal_data['LicenseNo'],
                                 REG.normal_data['linkMan'], REG.normal_data['contactNumber'],
                                 REG.normal_data['detail'], REG.normal_data['invoiceTitle'],
                                 REG.normal_data['dutyParagraph'], REG.normal_data['bankOfDeposit'],
                                 REG.normal_data['bankAccount'], REG.normal_data['file_path1'],
                                 REG.normal_data['file_path2'], REG.normal_data['file_path3'])
        assert register_web[1].submit_is_exist()
