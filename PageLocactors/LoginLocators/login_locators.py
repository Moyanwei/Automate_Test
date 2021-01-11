from selenium.webdriver.common.by import By


class LoginLocator:
    username_loc = (By.XPATH, '//input[@placeholder="请输入账号"]')  # 账号输入框
    password_loc = (By.XPATH, '//input[@placeholder="请输入密码"]')  # 密码输入框
    login_btn_loc = (By.XPATH, '//div[@class="gologin"]')  # 点击 登录 按钮
    error_msg_loc = (By.XPATH, '//div[@class="_alert_dialog"]')  # 账号或密码错误
    password1_msg_loc = (By.XPATH, '//p[text()="请输入密码!"]')  # 异常提示语
    password2_msg_loc = (By.XPATH, '//a[@class="forget"]')  # 异常提示语 忘记密码?
    logout_loc = (By.XPATH, '//div[@class="header_user_account_mobile"]')  # 用户头像元素
