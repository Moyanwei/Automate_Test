# coding: utf-8
import pytest
from TestDatas.RegisterDatas import register_datas as REG


@pytest.mark.usefixtures('register_web')
class TestRegister:
    """
     注册功能
     :param data: 测试数据
     :param register_web: 注册函数
     :return: 断言
     步骤：
     登录页面-输入用户名- membMobile: ---
     登录页面-输入密码- membPassword: ---
     登录页面-点击登录按钮
     页面跳转至注册信息填写界面-填写注册认证信息
     断言-首页-获取注册界面（提交）按钮元素，确认元素是否存在
    """
    def test_register01(self, register_web):
        register_web[1].register(REG.abnormal_data['companyName'], REG.abnormal_data['LicenseNo'],
                                 REG.abnormal_data['linkMan'], REG.abnormal_data['contactNumber'],
                                 REG.abnormal_data['detail'], REG.abnormal_data['invoiceTitle'],
                                 REG.abnormal_data['dutyParagraph'], REG.abnormal_data['bankOfDeposit'],
                                 REG.abnormal_data['bankAccount'], REG.abnormal_data['file_path1'],
                                 REG.abnormal_data['file_path2'], REG.abnormal_data['file_path3'])
        assert REG.abnormal_data['errorMsg'] == register_web[1].get_err()

    def test_register02(self, register_web):
        register_web[1].register(REG.normal_data['companyName'], REG.normal_data['LicenseNo'],
                                 REG.normal_data['linkMan'], REG.normal_data['contactNumber'],
                                 REG.normal_data['detail'], REG.normal_data['invoiceTitle'],
                                 REG.normal_data['dutyParagraph'], REG.normal_data['bankOfDeposit'],
                                 REG.normal_data['bankAccount'], REG.normal_data['file_path1'],
                                 REG.normal_data['file_path2'], REG.normal_data['file_path3'])
        assert register_web[1].submit_is_exist()

    def test_register04(self, register_web):
        register_web[1].registerxYyzx_None(REG.yyzxNone_data['companyName'], REG.yyzxNone_data['LicenseNo'],
                                           REG.yyzxNone_data['linkMan'], REG.yyzxNone_data['contactNumber'],
                                           REG.yyzxNone_data['detail'], REG.yyzxNone_data['invoiceTitle'],
                                           REG.yyzxNone_data['dutyParagraph'], REG.yyzxNone_data['bankOfDeposit'],
                                           REG.yyzxNone_data['bankAccount'], REG.yyzxNone_data['file_path1'],
                                           REG.yyzxNone_data['file_path2'], REG.yyzxNone_data['file_path3'])
        assert REG.yyzxNone_data['errorMsg'] == register_web[1].get_err()
