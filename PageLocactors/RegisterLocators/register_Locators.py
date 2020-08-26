from selenium.webdriver.common.by import By


class RegisterLocator:
    companyName_loc = (By.XPATH, '//input[@placeholder="输入公司名称"]')  # 输入公司名称
    LicenseNo_loc = (By.XPATH, '//input[@placeholder="输入统一社会信用代码或营业执照号"]')  # 输入营业执照号
    linkMan_loc = (By.XPATH, '//input[@placeholder="输入联系人姓名"]') # 输入联系人
    contactNumber_loc = (By.XPATH, '//input[@placeholder="输入联系人号码"]')  # 输入联系人号码
    site_loc = (By.XPATH, "//span[@class='el-cascader__label']")  # 地址选择
    province_loc = (By.XPATH, "//li[starts-with(@role,'menuitem')]/span[text()='广西']")  # 省
    city_loc = (By.XPATH, "//li[starts-with(@role,'menu')]/span[text()='南宁']")  # 市
    district_loc = (By.XPATH, "//li[starts-with(@role,'menu')]/span[text()='武鸣区']")  # 区
    detailButton_loc = (By.XPATH, "//input[contains(@placeholder,'详细地址定位')]")  # 详细地址定位
    detail_loc = (By.XPATH, "//input[@id='tipinput3']")  # 输入详细地址
    add_address = (By.XPATH, "//button[@class='confirm']")  # 详细地址确定按钮
    uploadOne_loc = (By.XPATH, "//label[@class='merc_license']")  # 上传营业执照图片
    uploadTwo_loc = (By.XPATH, "//div[@class='avatar']//input[@name='avatar']")  # 上传身份证正面
    uploadThree_loc = (By.XPATH, "//div[@class='avatar upimg']//input[@name='avatar']")  # 上传身份证反面
    yyzx_loc = (By.XPATH, "//input[@placeholder='请选择运营中心']")  # 选择运营中心
    xzyy_loc = (By.XPATH, "//li[@class='el-select-dropdown__item']/span[text()='西藏运营中心']")