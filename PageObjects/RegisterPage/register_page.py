from PageLocactors.RegisterLocators.register_Locators import RegisterLocator as loc
from Common.basepage import BasePage
import time


class RegisterPage(BasePage):
    def register(self, companyName, LicenseNo, linkMan, contactNumber, detail, invoiceTitle, dutyParagraph,
                 bankOfDeposit, bankAccount, file_path1, file_path2, file_path3):
        self.get_element_input_txt(loc.companyName_loc, "输入公司名称", companyName)
        self.get_element_input_txt(loc.LicenseNo_loc, "输入营业执照号", LicenseNo)
        self.get_element_click(loc.uploadOne_loc, "点击上传营业执照图片")
        self.upload_file(filename=file_path1, img_doc="营业执照")  # file_path 图片路径
        self.get_element_click(loc.uploadTwo_loc, "点击上传身份证图片")
        self.upload_file(filename=file_path2, img_doc="身份证正")  # file_path 图片路径
        self.get_element_click(loc.uploadThree_loc, "点击上传身份证图片")
        self.upload_file(filename=file_path3, img_doc="身份证反")  # file_path 图片路径
        self.get_element_input_txt(loc.linkMan_loc, "输入联系人", linkMan)
        self.get_element_input_txt(loc.contactNumber_loc, "输入联系人号码", contactNumber)
        self.get_element_click(loc.site_loc, "地址选择")
        self.scroll(loc.scroll_loc, "滚动地址选择")
        self.get_element_click(loc.province_loc, "省")
        self.get_element_click(loc.city_loc, "市")
        self.get_element_click(loc.district_loc, "省")
        self.get_element_click(loc.detailButton_loc, "详细地址定位")
        self.get_element_input_txt(loc.detail_loc, "输入详细地址", detail)
        time.sleep(3)
        self.get_element_click(loc.add_address, "详细地址确定按钮")
        self.get_element_click(loc.yyzx_loc, "选择运营中心")
        self.get_element_click(loc.xzyy_loc, "测试运营中心")
        time.sleep(2)
        self.get_element_click(loc.operating_loc, "运营范围")
        self.get_element_click(loc.specialLine_loc, "专线运输")
        self.get_element_input_txt(loc.invoiceTitle_loc, "输入发票抬头", invoiceTitle)
        self.get_element_input_txt(loc.dutyParagraph_loc, "输入税号", dutyParagraph)
        self.get_element_input_txt(loc.bankOfDeposit_loc, "输入开户行", bankOfDeposit)
        self.get_element_input_txt(loc.bankAccount_loc, "输入银行账号", bankAccount)
        self.get_element_click(loc.submit_loc, "提交")

    def get_err(self):
        linkman = '注册页面_注册功能错误信息_获取异常提示语:联系人不能为空'
        contact = '注册页面_注册功能错误信息_获取异常提示语:联系方式不能为空'
        yyzx = '注册页面_注册功能错误信息_获取异常提示语:运营中心不能为空'
        companyName = '注册页面_注册功能错误信息_获取异常提示语:公司名称已存在'
        try:
            return self.get_element_txt(loc.linkmanErr_loc, linkman)
        except Exception:
            return self.get_element_txt(loc.contactEerr_loc, contact)
        except Exception:
            return self.get_element_txt(loc.yyzx_loc, yyzx)
        except Exception:
            return self.get_element_txt(loc.companyNameErr_loc, companyName)

    def submit_is_exist(self):
        """
        提交按钮元素是否存在。存在返回True，不存在返回False
        :return:
        """
        try:
            self.wait_element_visible(loc.toExamine_loc, "注册成功提示信息是否存在")
        except TimeoutError:
            return False
        else:
            return True
