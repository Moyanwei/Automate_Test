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
        register_web[1].register(REG.ContactNone_data['companyName'], REG.ContactNone_data['LicenseNo'],
                                 REG.ContactNone_data['linkMan'], REG.ContactNone_data['contactNumber'],
                                 REG.ContactNone_data['detail'], REG.ContactNone_data['invoiceTitle'],
                                 REG.ContactNone_data['dutyParagraph'], REG.ContactNone_data['bankOfDeposit'],
                                 REG.ContactNone_data['bankAccount'], REG.ContactNone_data['file_path1'],
                                 REG.ContactNone_data['file_path2'], REG.ContactNone_data['file_path3'])
        assert REG.ContactNone_data['errorMsg'] == register_web[1].Contact_err()

    def test_register02(self, register_web):
        register_web[1].register(REG.ContactPhoneNone_data['companyName'], REG.ContactPhoneNone_data['LicenseNo'],
                                 REG.ContactPhoneNone_data['linkMan'], REG.ContactPhoneNone_data['contactNumber'],
                                 REG.ContactPhoneNone_data['detail'], REG.ContactPhoneNone_data['invoiceTitle'],
                                 REG.ContactPhoneNone_data['dutyParagraph'], REG.ContactPhoneNone_data['bankOfDeposit'],
                                 REG.ContactPhoneNone_data['bankAccount'], REG.ContactPhoneNone_data['file_path1'],
                                 REG.ContactPhoneNone_data['file_path2'], REG.ContactPhoneNone_data['file_path3'])
        assert REG.ContactPhoneNone_data['errorMsg'] == register_web[1].ContactPhone_err()

    def test_register03(self, register_web):
        register_web[1].registerxYyzx_None(REG.YyzxNone_data['companyName'], REG.YyzxNone_data['LicenseNo'],
                                           REG.YyzxNone_data['linkMan'], REG.YyzxNone_data['contactNumber'],
                                           REG.YyzxNone_data['detail'], REG.YyzxNone_data['invoiceTitle'],
                                           REG.YyzxNone_data['dutyParagraph'], REG.YyzxNone_data['bankOfDeposit'],
                                           REG.YyzxNone_data['bankAccount'], REG.YyzxNone_data['file_path1'],
                                           REG.YyzxNone_data['file_path2'], REG.YyzxNone_data['file_path3'])
        assert REG.YyzxNone_data['errorMsg'] == register_web[1].Yyzx_err()

    def test_register04(self, register_web):
        register_web[1].register(REG.CompanyName_data['companyName'], REG.CompanyName_data['LicenseNo'],
                                 REG.CompanyName_data['linkMan'], REG.CompanyName_data['contactNumber'],
                                 REG.CompanyName_data['detail'], REG.CompanyName_data['invoiceTitle'],
                                 REG.CompanyName_data['dutyParagraph'], REG.CompanyName_data['bankOfDeposit'],
                                 REG.CompanyName_data['bankAccount'], REG.CompanyName_data['file_path1'],
                                 REG.CompanyName_data['file_path2'], REG.CompanyName_data['file_path3'])
        assert REG.CompanyName_data['errorMsg'] == register_web[1].CompanyName_err()

    def test_register05(self, register_web):
        register_web[1].register(REG.Normal_data['companyName'], REG.Normal_data['LicenseNo'],
                                 REG.Normal_data['linkMan'], REG.Normal_data['contactNumber'],
                                 REG.Normal_data['detail'], REG.Normal_data['invoiceTitle'],
                                 REG.Normal_data['dutyParagraph'], REG.Normal_data['bankOfDeposit'],
                                 REG.Normal_data['bankAccount'], REG.Normal_data['file_path1'],
                                 REG.Normal_data['file_path2'], REG.Normal_data['file_path3'])
        assert register_web[1].submit_is_exist()
