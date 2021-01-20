# coding: utf-8
# 1、封装基本关键字，任何一个页面操作都可以实时捕获异常/输入日志/失败截图

import time
import win32gui
import win32con
import allure
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver  # 调用所有的WebDriver对象
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import contants
from Common.handle_log import case_log
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver):
        """指明WebDriver对象，driver.可以直接找出find_element内容"""
        self.driver = driver

    def save_screen_shoot(self, img_doc):
        """
        img_doc: 执行的操作描述
        存储到指定目录下 - 加上路径配置
        :param img_doc:截图图片
        :return:
        """
        t = datetime.strftime(datetime.now(), "%Y%m%d%H%M")  # t的格式是 年月日
        filename = contants.screenshots_dir + '/' + "{}_{}.png".format(t, img_doc)
        self.driver.save_screenshot(filename)
        with open(filename, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)
        case_log.info("页面截图成功文件保存在：{}".format(filename))

    def wait_element_visible(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可见
        :param locator:
        :param img_doc:截图图片
        :param timeout:
        :param frequeny:
        :return:
        """
        case_log.info("在 {} ，等待元素 {} 可见。".format(img_doc, locator))
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            # 异常截图 - 通过截图名称，知道是哪个页面或者那个模块出错了
            # 异常日志捕获
            case_log.exception("页面{}等待元素可见失败".format(locator))
            self.save_screen_shoot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_log.info("页面元素{}等待存在,等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return ele

    def get_element(self, locator, img_doc):
        """获取页面中的所有元素"""
        case_log.info("在 {}, 查找元素{}可见。".format(img_doc, locator))
        start_time = time.time()
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            # 异常截图 - 通过截图名称，知道是哪个页面或者那个模块出错了
            # 异常日志捕获
            case_log.exception("在{}中查找元素{}查找失败！".format(img_doc, locator))
            self.save_screen_shoot(img_doc)
            raise e
        else:
            end_time = time.time()
            case_log.info("页面元素{}查找存在，等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return ele

    def get_element_click(self, locator, img_doc, timeout=20, frequency=0.5):
        """等待元素可点击"""
        self.wait_element_visible(locator, img_doc, timeout, frequency)
        ele = self.get_element(locator, img_doc)
        case_log.info("在 {}，点击元素{}。".format(img_doc, locator))
        try:
            return ele.click()
        except Exception as e:
            case_log.exception("在{}中点击元素，点击元素失败".format(img_doc, locator))
            self.save_screen_shoot(img_doc)
            raise e

    def get_element_input_txt(self, locator, img_doc, content, timeout=20, frequency=0.5):
        """对输入框输入文本内容"""
        self.wait_element_visible(locator, img_doc, timeout, frequency)
        ele = self.get_element(locator, img_doc)
        case_log.info("在 {}，对元素{}输入内容：{}。".format(img_doc, locator, content))
        try:
            return ele.send_keys(content)
        except Exception as e:
            case_log.exception("在元素{}中输入内容{}元素输入文本失败".format(locator, content))
            self.save_screen_shoot(img_doc)
            raise e

    def clear_text(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        清除文本框的内容
        :param locator:
        :param img_doc: 截图说明，截图图片
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        """
        try:
            case_log.info("在 {}中清除元素{}的文本内容".format(img_doc, locator))
            self.get_element_click(locator, img_doc, timeout, frequency)
            self.get_element(locator, img_doc).clear()
        except Exception as e:
            case_log.error("在 {}中清除元素{}的文本内容失败！".format(img_doc, locator))
            self.save_screen_shoot(img_doc)
            raise e

    def get_element_attribute(self, locator, img_doc, attribute_name, timeout=20, frequency=0.5):
        """获取WebElement对象的属性值"""
        self.wait_element_visible(locator, img_doc, timeout, frequency)
        ele = self.get_element(locator, img_doc)
        case_log.info("在 {}，获取元素{}属性{}。".format(img_doc, attribute_name, locator))
        try:
            value = ele.get_attribute(attribute_name)
        except Exception as e:
            case_log.exception("在 {}中获取元素{}的属性{}获取元素属性失败".format(img_doc, locator, attribute_name))
            self.save_screen_shoot(img_doc)
            raise e
        else:
            case_log.info("获取元素属性内容为： {} ".format(value))
            return value

    def wait_page_contain_element(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素存在
        :param locator:
        :param img_doc:截图图片
        :param timeout:
        :param frequeny:
        :return:
        """
        case_log.info("在 {}，等待元素{}存在。".format(img_doc, locator))
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(locator))
        except TimeoutError:
            # 异常截图 - 通过截图名称，知道是哪个页面或者那个模块出错了
            # 异常日志捕获
            case_log.exception("页面元素{}等待元素存在失败".format(locator))
            self.save_screen_shoot(img_doc)
        else:
            end_time = time.time()
            case_log.info("页面元素{}等待存在,等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return ele

    def get_element_txt(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        获取元素文本只要存在就行，不需要可见
        :param locator:
        :param img_doc:截图图片
        :param timeout:
        :param frequeny:
        :return:
        """
        self.wait_page_contain_element(locator, img_doc, timeout, frequency)
        ele = self.get_element(locator, img_doc)
        case_log.info("在 {} ，获取元素文本内容： {} 。".format(img_doc, locator))
        try:
            text = ele.text
        except Exception as e:
            case_log.exception("在{}中获取元素{}元素文本内容失败".format(locator, img_doc))
            self.save_screen_shoot(img_doc)
            raise e
        else:
            case_log.info("获取元素文本内容为：{} ".format(text))
            return text

    def get_element_select(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可以被选择
        :param locator:
        :param fqc:
        :return:
        """
        case_log.info("在 {}，等待元素{}可以选择。".format(img_doc, locator))
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, frequency).until(EC.element_located_to_be_selected(locator))
        except Exception as e:
            case_log.exception("等待元素{}选择失败".format(locator))
            self.save_screen_shoot(img_doc)
        else:
            end_time = time.time()
            case_log.info("页面等待元素{}可以选择，等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return ele

    def get_frame_element(self, locator, img_doc, timeout=20, frequency=0.5):  # need update
        """
        跳转到iframe
        :param locator:
        :param eqc:
        :return:
        """
        case_log.info("在 {}，跳转到iframe{}。".format(img_doc, locator))
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, frequency).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        except TimeoutError:
            # 异常截图 - 通过截图名称，知道是哪个页面或者那个模块出错了
            # 异常日志捕获
            case_log.exception("跳转iframe失败")
            self.save_screen_shoot(img_doc)
        else:
            end_time = time.time()
            case_log.info("跳转到iframe{},等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return ele

    def get_mouse_element_click(self, img_doc, timeout=20, frequency=0.5):
        """鼠标悬浮"""
        self.wait_element_visible(img_doc, timeout, frequency)
        ele = self.get_element(img_doc)
        case_log.info("在 {}，对元素{}进行鼠标操作 。".format(img_doc))
        try:
            ac = ActionChains(self.driver)
            return ac.move_to_element(ele).click(ele).perform()
        except Exception as e:
            case_log.exception("鼠标操作元素失败")
            self.save_screen_shoot(img_doc)
            raise e

    def get_upload_file(self, filePath, browser_type="chrome"):
        """
        前提：windows上传窗已经出现，sleep1-2秒等待弹出的出现
        :param locator:
        :param img_doc:截图图片
        :param files:
        :return:
        """
        if browser_type.lower() == "chrome":
            title = "打开"
        elif browser_type.lower() == "firefox":
            title = "文件上传"
        elif browser_type.lower() == "ie":
            title = "选择要加载的文件"
        else:
            title = ""  # 这里根据其它不同浏览器类型来修改

        # 一级窗口“#32770”，“打开”
        dialog = win32gui.FindWindow('#32770', title)  # 一级窗口
        print(dialog)
        # 找到窗口
        ComboxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)  # 二级
        print(ComboxEx32)
        # 向下传递
        comboBox = win32gui.FindWindowEx(ComboxEx32, 0, 'ComboBox', None)  # 三级
        print(comboBox)
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        print(edit)
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&O)')  # 四级
        print(button)
        print('ok')
        time.sleep(2)
        # 发送文件路径，输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)
        time.sleep(2)
        # 点击打开按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(2)

    def upload_file(self, filename, img_doc, browser_type="chrome"):
        """
        非input标签的文件上传
        :param filename: 文件名（绝对路径）
        :param img_doc: 截图说明，截图图片
        :param browser_type: 浏览器类型
        :return:
        """
        try:
            case_log.info("上传文件（{}）".format(filename))
            time.sleep(2)
            self.get_upload_file(filePath=filename, browser_type=browser_type)
        except Exception as e:
            case_log.error("上传文件（{}）失败！".format(filename))
            self.save_screen_shoot(img_doc)
            raise e
        else:
            time.sleep(2)

    def get_elements(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待多个元素可见
        :param locator:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        case_log.info("在 {}，等待多个元素{} 可见。".format(img_doc, locator))
        start_time = time.time()
        try:
            eles = WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            # 异常截图 - 通过截图名称，知道是哪个页面或者那个模块出错了
            # 异常日志捕获
            case_log.exception("等待多个元素{}可见失败".format(locator))
            self.save_screen_shoot(img_doc)
        else:
            end_time = time.time()
            case_log.info("页面等待多个元素{}可见，等待时间长为：{}s 。".format(locator, round(end_time - start_time, 3)))
            return eles

    def switch_windows(self, img_doc, name=None, frequency=20):  # 查看窗口跳转源代码
        # 等待
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, frequency).until(EC.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        self.driver.switch_to.window()
        self.save_screen_shoot(img_doc)

    def switch_to_default_content(self, img_doc):
        """
        切换iframe到main页面
        :param img_doc: 截图说明，截图图片
        :return:
        """
        try:
            case_log.info("切换iframe到main页面")
            self.driver.switch_to.default_content()
        except Exception as e:
            case_log.error("切换iframe到main页面失败！")
            self.save_screen_shoot(img_doc)
            raise e


if __name__ == '__main__':  # 测试basepage方法是否正确
    driver = webdriver.Chrome()
    base = BasePage(driver)
    base.driver.get("http://www.baidu.com/")
    base.get_element_input_txt((By.XPATH, "//input[@id='kw']"), "输入内容", content='test')
