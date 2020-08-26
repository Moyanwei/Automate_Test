# -*- coding: UTF-8 -*-
import logging
import logging.handlers

from Common.handle_config import HandleConfig
from Common import contants

do_config = HandleConfig()
logger_level = do_config.get_value('Log', 'logger_level')
log_filename = contants.log_filename

console_level = do_config.get_value('Log', 'console_level')
file_level = do_config.get_value('Log', 'file_level')

simple_formatter = do_config.get_value('Log', 'simple_formatter')
verbose_formatter = do_config.get_value('Log', 'verbose_formatter')


class HandleLog(object):
    """
     定义日志显示的格式
     formatter = logging.Formatter('[%(asctime)s] - '  # 当前系统时间
                                   '[%(levelname)s] - '  # 日志信息级别
                                   '[%(filename)s] - '  # 当前日志所在的文件名、模块名级别
                                   '[line: %(lineno)d] - '  # 出错的行数
                                   '[%(name)s] - '  # 日志收集器名字
                                   '[日志信息]: %(message)s')  # 日志输出的信息
     """
    def __init__(self, logger_name):
        # 1、定义日志收集器
        self.case_log = logging.getLogger(logger_name)
        self.case_log.handlers.clear()

        # 2、指定日志收集器的日志等级
        # NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
        self.case_log.setLevel(logger_level)

        # 3、定义日志输出渠道，输出到控制台
        console_handle = logging.StreamHandler()

        # 输出到文件
        file_handle = logging.FileHandler(log_filename, encoding='utf-8')

        # 4、指定日志输出渠道的日志等级
        console_handle.setLevel(console_level)
        file_handle.setLevel(file_level)


        ch = logging.Formatter(simple_formatter)
        fh = logging.Formatter(verbose_formatter)
        console_handle.setFormatter(ch)  # 控制台显示简洁的日志
        file_handle.setFormatter(fh)  # 日志文件中显示详细日志

        # 对接，将日志收集器与输出渠道对接
        self.case_log.addHandler(console_handle)
        self.case_log.addHandler(file_handle)

    def get_logger(self):
        """
        获取日志对象
        :return:
        """
        return self.case_log


case_log = HandleLog(logger_name='OMS').get_logger()


if __name__ == '__main__':
    case_log = HandleLog(logger_name='casetest').get_logger()
    case_log.debug("debug日志")
    case_log.info("info日志")
    case_log.warning('warning日志')
    case_log.error('error日志')
    case_log.critical('critical日志')