from selenium.webdriver.common.by import By


class TmsDeleteCargo:
    import_cargosName = (By.XPATH, "//div[@id='MyInput']//input[@placeholder='输入货物名称']")  # 货物名称

    dele_cargosTypeId = (By.XPATH, "//ul[@class='search clear']//input[@placeholder='选择货物类型']")  # 货物类型

    dele_cargosType = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span")  # 货物类型下拉框选中并点击

    Query_button = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span")  # 查询按钮

    delete_button = (By.XPATH, "//div[@class='List_middle']//a[@class='_operate']/following::a[text()='删除']")  # 删除按钮

    confirm_button = (By.XPATH, "//button[@class='primary_btn confirm_btn']")  # 确定按钮

    dele_cargo_msg = (By.XPATH, "//div[@class='_alert_dialog']")  # 异常提示