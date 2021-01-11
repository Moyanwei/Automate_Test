from PageLocactors.LoginLocators.login_locators import LoginLocator as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    # 登录
    def login(self, membMobile, membPassword):
        self.get_element_input_txt(loc.username_loc, "登录页面 - 输入用户名", membMobile)
        self.get_element_input_txt(loc.password_loc, "登录页面 - 输入密码", membPassword)
        self.get_element_click(locator=loc.login_btn_loc, img_doc="登陆页面 - 点击登陆按钮")

    # 获取错误提示
    def get_err(self):
        doc1 = '登录页面_登录功能错误信息_获取错误信息'
        doc2 = '登录页面_登录功能错误信息_密码为空'
        try:
            return self.get_element_txt(loc.error_msg_loc, doc1)
        except:
            return self.get_element_txt(loc.password1_msg_loc, doc2)

    # 验证正向用例运行成功
    def if_user_is_exist(self):
        """
        用户元素是否存在。存在返回True，不存在返回False
        :return:
        """
        try:
            self.wait_element_visible(loc.logout_loc, "首页 - 查看用户名是否存在")
        except TimeoutError:
            return False
        else:
            return True


