from PageLocactors.RegisterLocators.register_Locators import RegisterLocator as loc
from Common.basepage import BasePage


class RegisterPage(BasePage):
    def register(self, companyName, LicenseNo, linkMan, contactNumber, detail, file_path):
        self.get_element_input_txt(loc.companyName_loc, "输入公司名称", companyName)
        self.get_element_input_txt(loc.LicenseNo_loc, "输入营业执照号", LicenseNo)
        self.get_element_click(loc.uploadOne_loc, "点击上传营业执照图片")
        self.upload_file(filename=file_path, img_doc="营业执照")  # file_path 图片路径
        self.get_element_click(loc.uploadTwo_loc, "点击上传身份证图片")
        self.upload_file(filename=file_path, img_doc="身份证正")  # file_path 图片路径
        self.get_element_click(loc.uploadThree_loc, "点击上传身份证图片")
        self.upload_file(filename=file_path, img_doc="身份证反")  # file_path 图片路径
        self.get_element_input_txt(loc.linkMan_loc, "输入联系人", linkMan)
        self.get_element_input_txt(loc.contactNumber_loc, "输入联系人号码", contactNumber)
        self.get_element_click(loc.site_loc, "地址选择")
        self.get_element_click(loc.province_loc, "省")
        self.get_element_click(loc.city_loc, "市")
        self.get_element_click(loc.district_loc, "省")
        self.get_element_click(loc.detailButton_loc, "详细地址定位")
        self.get_element_click(loc.detail_loc, "输入详细地址", detail)
        self.get_element_click(loc.add_address, "详细地址确定按钮")
        self.get_element_click(loc.yyzx_loc, "选择运营中心")
        self.get_element_click(loc.xzyy_loc, "西藏运营中心")


