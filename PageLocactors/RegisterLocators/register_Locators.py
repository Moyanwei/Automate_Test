from selenium.webdriver.common.by import By


class RegisterLocator:
    companyName_loc = (By.XPATH, '//input[@placeholder="输入公司名称"]')  # 输入公司名称
    LicenseNo_loc = (By.XPATH, '//input[@placeholder="输入统一社会信用代码或营业执照号"]')  # 输入营业执照号
    linkMan_loc = (By.XPATH, '//input[@placeholder="输入联系人姓名"]')  # 输入联系人
    contactNumber_loc = (By.XPATH, '//input[@placeholder="输入联系人号码"]')  # 输入联系人号码
    site_loc = (By.XPATH, "//input[@placeholder='选择省/市/区']")  # 地址选择
    scroll_loc = (By.XPATH, "//div[@id='cascader-menu-939-0']/div[@class='el-scrollbar__bar is-vertical']/div[@class='el-scrollbar__thumb']")
    province_loc = (By.XPATH, "//li[starts-with(@role,'menuitem')]/span[text()='浙江']")  # 省
    city_loc = (By.XPATH, "//li[starts-with(@role,'menu')]/span[text()='杭州']")  # 市
    district_loc = (By.XPATH, "//li[starts-with(@role,'menu')]/span[text()='萧山区']")  # 区
    detailButton_loc = (By.XPATH, "//input[contains(@placeholder,'详细地址定位')]")  # 详细地址定位
    detail_loc = (By.XPATH, "//input[@id='tipinput']")  # 输入详细地址
    add_address = (By.XPATH, "//button[@class='confirm']")  # 详细地址确定按钮
    uploadOne_loc = (By.XPATH, "//label[@class='merc_license']")  # 上传营业执照图片
    uploadTwo_loc = (By.XPATH, "//div[@class='avatar']")  # 上传身份证正面
    uploadThree_loc = (By.XPATH, "//div[@class='avatar upimg']")  # 上传身份证反面
    yyzx_loc = (By.XPATH, "//input[@placeholder='请选择运营中心']")  # 选择运营中心
    xzyy_loc = (By.XPATH, "//div[@class='el-scrollbar']//span[contains(text(),'测试运营中心')]")   # 所属运营中心
    operating_loc = (By.XPATH, "//div[@class='el-select']//input[@placeholder='请选择']")   # 运营范围
    specialLine_loc = (By.XPATH, "//span[contains(text(),'专线运输')]")  # 专线运输
    invoiceTitle_loc = (By.XPATH, '//input[@placeholder="输入发票抬头"]')  # 输入发票抬头
    dutyParagraph_loc = (By.XPATH, '//input[@placeholder="输入税号"]')  # 输入税号
    bankOfDeposit_loc = (By.XPATH, '//input[@placeholder="输入开户行"]')  # 输入开户行
    bankAccount_loc = (By.XPATH, '//input[@placeholder="输入银行账号"]')  # 输入银行账号
    submit_loc = (By.XPATH, '//button[@ class="upBtn"]')  # 提交按钮
    companyNameErr_loc = (By.XPATH, '//div[@class="_alert_dialog"]/child::p[text()="公司名称已存在!"]')  # 公司名称已存在
    linkmanErr_loc = (By.XPATH, '//div[@class="_alert_dialog"]/child::p[text()="联系人不能为空"]')  # 联系人不能为空
    contactEerr_loc = (By.XPATH, '//div[@class="_alert_dialog"]/child::p[text()="联系方式不能为空"]')  # 联系方式不能为空
    yyzxErr_loc = (By.XPATH, '//div[@class="_alert_dialog"]/child::p[text()="运营中心不能为空"]')   # 运营中心不能为空
