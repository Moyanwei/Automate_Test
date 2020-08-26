from selenium.webdriver.common.by import By


class TmsAddDepartment:
    button_addUser = (By.XPATH, "//button[@class='_active_button addUser']")  # 添加部门按钮

    add_depaName = (By.XPATH, "//div[@id='MyInput']/following::input[contains(@placeholder,'输入部门名称')]")  # 输入部门名称

    add_depaLinkman = (By.XPATH, "//div[@id='MyInput']/following::input[contains(@placeholder,'输入联系人')]")  # 输入联系人

    add_depaLinkphone = (By.XPATH, "//div[@id='MyInput']/following::input[contains(@placeholder,'输入联系电话')]")  # 输入联系电话

    add_depaFax = (By.XPATH, "//div[@id='MyInput']/following::input[contains(@placeholder,'输入传真')]")   # 输入传真

    add_depaRemark = (By.XPATH, "//div[@id='MyInput']/following::textarea[@placeholder='输入备注内容']")  # 备注

    addDepart_button = (By.XPATH, "//div[@class='_dialog_wrapper']//button[text()='添加']")  # 添加按钮

    cancel_button = (By.XPATH, "//button[@class='_normal_button addDepartDialogFooterBtn']")  # 添加按钮

    addDepart_msg = (By.XPATH, '//div[@class="_alert_dialog"]')  # 异常提示