from selenium.webdriver.common.by import By


class TmsDeleteDepartment:
    dele_depaName = (By.XPATH, "//ul[@class='search clear']//input[contains(@placeholder,'输入部门名称')]")  # 输入部门名称

    query_button = (By.XPATH, "//*[@id='departManage']//ul[@class='search clear']//button[@class='_active_button']")  # 查询按钮

    delete_button = (By.XPATH, "//div[@class='el-table__fixed-right']//a[@class='_operate']/following::a[text()='删除']")  # 删除按钮

    confirm_button = (By.XPATH, "//button[contains(@class,'primary_btn confirm_btn')]")  # 确定按钮

    dele_Depart_msg = (By.XPATH, "//span[@class='el-table__empty-text']")  # 异常提示