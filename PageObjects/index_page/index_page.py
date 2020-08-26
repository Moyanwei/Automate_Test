# coding: utf-8
from PageLocactors.Lndex.lndex_locators import IndexLocator as index_loc
from Common.basepage import BasePage


class IndexPage(BasePage):
    def if_user_is_exist(self):
        """
        用户元素是否存在。存在返回True，不存在返回False
        :return:
        """
        try:
            self.wait_element_visible(index_loc.logout_loc, "首页 - 查看用户名是否存在")
        except TimeoutError:
            return False
        else:
            return True


    def get_error_msg(self):
        """
        # 获取错误提示信息
        return self.wait.until(EC.visibility_of_element_located(loc.error_msg)).text
        """
        return self.get_element_txt(index_loc.error_msg_loc, "获取错误提示信息")