from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TmsLocator:
    cargo_add_cargobtn = (By.XPATH, '//button[@class="_active_button addGoods"]')  # 添加货物按钮

    cargo_add_cargosName = (By.XPATH, '//*[@id="AddEditGoods"]//input[@placeholder="输入货物名称"]')  # 货物名称

    cargo_add_cargosTypeId = (By.XPATH, '//*[@id="AddEditGoods"]//input[@class="el-input__inner"]')  # 货物类型

    cargo_add_cargosType = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')  # 货物下拉框选中并点击

    cargo_add_cargosVersion = (By.XPATH, '//input[@placeholder="输入货物型号"]')  # 货物型号

    cargo_add_cargosPack = (By.XPATH, '//input[@placeholder="输入货物包装"]')  # 货物包装

    cargo_add_cargosWeight = (By.XPATH, '//input[@placeholder="输入单位重量"]')  # 货物单位重量

    cargo_add_cargosVolume = (By.XPATH, '//input[@placeholder="输入单位体积"]')  # 货物单位体积

    cargo_add_cargosValue = (By.XPATH, '// input[ @ placeholder="输入货值"]')  # 货值

    cargo_add_cargobutton = (By.XPATH, '// button[@class="save_car _active_button"]')  # 新增按钮

    cargo_add_cancelButton = (By.XPATH, '//button[@class="cancel_car"]')  # 取消按钮

    cargo_add_cargo_msg = (By.XPATH, '//div[@class="_alert_dialog"]')  # 异常提示




