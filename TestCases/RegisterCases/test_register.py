# coding: utf-8
import pytest
import allure
from TestDatas.RegisterDatas import register_datas as REG


@allure.feature('注册模块')
@allure.issue('https://oms.sdhwlw.com/')
@pytest.mark.usefixtures('register_web')
class TestRegister:
    """
     注册功能测试步骤：
     登录页面-输入用户名- membMobile: ---
     登录页面-输入密码- membPassword: ---
     登录页面-点击登录按钮
     页面跳转至注册信息填写界面-填写注册认证信息
     断言-首页-获取注册界面提示语、页面元素，确认元素是否存在或提示语是否存在
    """
    @allure.story('测试注册功能，联系人字段为空')
    @pytest.mark.parametrize('data', REG.ContactNone_data)
    def test_register01(self, data, register_web):
        with allure.step('1.输入公司名称:{}'
                         '2.输入营业执照号:{}'
                         '3.')
            register_web[1].register(data['companyName'], data['LicenseNo'],
                                 data['linkMan'], data['contactNumber'],
                                 data['detail'], data['invoiceTitle'],
                                 data['dutyParagraph'], data['bankOfDeposit'],
                                 data['bankAccount'], data['file_path1'],
                                 data['file_path2'], data['file_path3'])
        assert data['errorMsg'] == register_web[1].Contact_err()   # 断言:联系人不能为空

    @allure.story('测试注册功能，联系电话字段为空')
    @pytest.mark.parametrize('data', REG.ContactPhoneNone_data)
    def test_register02(self, data, register_web):
        register_web[1].register(data['companyName'], data['LicenseNo'],
                                 data['linkMan'], data['contactNumber'],
                                 data['detail'], data['invoiceTitle'],
                                 data['dutyParagraph'], data['bankOfDeposit'],
                                 data['bankAccount'], data['file_path1'],
                                 data['file_path2'], data['file_path3'])
        assert data['errorMsg'] == register_web[1].ContactPhone_err()    # 断言:联系方式不能为空

    @allure.story('测试注册功能，运营中心字段为空')
    @pytest.mark.parametrize('data', REG.YyzxNone_data)
    def test_register03(self, data, register_web):
        register_web[1].registerxYyzx_None(data['companyName'], data['LicenseNo'],
                                           data['linkMan'], data['contactNumber'],
                                           data['detail'], data['invoiceTitle'],
                                           data['dutyParagraph'], data['bankOfDeposit'],
                                           data['bankAccount'], data['file_path1'],
                                           data['file_path2'], data['file_path3'])
        assert data['errorMsg'] == register_web[1].Yyzx_err()   # 断言:运营中心不能为空

    @allure.story('测试注册功能，公司名称字段已存在且重复时')
    @pytest.mark.parametrize('data', REG.YyzxNone_data)
    def test_register04(self, data, register_web):
        register_web[1].register(data['companyName'], data['LicenseNo'],
                                 data['linkMan'], data['contactNumber'],
                                 data['detail'], data['invoiceTitle'],
                                 data['dutyParagraph'], data['bankOfDeposit'],
                                 data['bankAccount'], data['file_path1'],
                                 data['file_path2'], data['file_path3'])
        assert data['errorMsg'] == register_web[1].CompanyName_err()   # 断言:公司名称已存在

    @allure.story('测试注册功能，注册成功')
    @pytest.mark.parametrize('data', REG.Normal_data)
    def test_register05(self, data, register_web):
        register_web[1].register(data['companyName'], data['LicenseNo'],
                                 data['linkMan'], data['contactNumber'],
                                 data['detail'], data['invoiceTitle'],
                                 data['dutyParagraph'], data['bankOfDeposit'],
                                 data['bankAccount'], data['file_path1'],
                                 data['file_path2'], data['file_path3'])
        assert register_web[1].submit_is_exist()   # 断言:注册成功后某一元素存在
