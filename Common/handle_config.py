# -*- coding: UTF-8 -*-
"""
将程序中不常变化的数据放在配置文件中，有什么好处呢?
方便调用，当变更配置时，减少重复工作
将代码中的配置项抽取到配置文件中，修改配置时不需要涉及到代码修改，极大的方便后期软件的维护
"""

from configparser import ConfigParser
from Common import contants


class OperationalError(Exception):
    'operation error'


class HandleConfig(object):

    def __init__(self, filenames=None):

        self.config = ConfigParser()
        self.config.read(contants.global_file, encoding='utf-8')  # 先加载开关
        open = self.config.getboolean('Switch', 'open')
        if open:
            self.config.read(filenames=contants.write_config_file, encoding='utf-8')
        else:
            self.config.read(filenames=contants.write_config2_file, encoding='utf-8')

    def get_value(self, section, option):
        # 代码优化，如果没有就抛出异常，不要报错，配置文件、加载是否正确
        try:
            return self.config.get(section, option)
        except SyntaxError as e:
            raise OperationalError("Option %s is not found in "
                                   "configuration, error: %s" %
                                   (section, e))

    def get_int(self, section, option):
        return self.config.getint(section, option)

    def get_float(self, section, option):
        return self.config.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.config.getboolean(section, option)

    def get_eval_data(self, section, option):
        return eval(self.config.get(section, option))

    def has_section(self, section):
        if self.config.has_section(section):
            return True
        else:
            return False

    def has_option(self, section, option):
        if self.config.has_option(section, option):
            return True
        else:
            return False


class WriteConfig(object):
    def write_config(self, datas):
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return '数据不合法，应为嵌套字典的字典'

            config_write = ConfigParser()
            config_write.read(filenames=contants.global_file, encoding='utf-8')
            # write_switch = config_write.getboolean('Switch', 'write')
            open_file = config_write.getboolean('Switch', 'open')

            for key in datas:
                config_write[key] = datas[key]

            if open_file:
                with open(contants.write_config_file, 'a+') as file:
                    config_write.write(file)
            else:
                with open(contants.write_config2_file, 'a+') as file:
                    config_write.write(file)


if __name__ == '__main__':
    # cf = HandleConfig()
    # print(cf.get_value('file path', 'case_path'))
    user_dict = {
        'test': {
            'Id': 1,
            'regname': 'lu',
            'mobilephone': '12345678901',
            'pwd': '123456',
        }
    }
    wr = WriteConfig()
    pa = wr.write_config(datas=user_dict)
    print(pa)
    pass
