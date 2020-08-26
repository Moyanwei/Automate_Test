from selenium.webdriver.common.by import By


class IndexLocator:
    logout_loc = (By.XPATH, '//div[@class="header_user_account_mobile"]')
    compile_loc = (By.XPATH, '//div[@class="Content_right"]//a[text()="编辑"]')
    error_msg_loc = (By.XPATH, '//div[@class="_alert_dialog"]')  # 异常提示语