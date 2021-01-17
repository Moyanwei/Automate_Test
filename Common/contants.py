# coding: utf-8

import os
# 项目地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Common 地址
common_dir = os.path.join(base_dir, "Common")
basepage_file = os.path.join(common_dir, "basepage.py")  # 操作方法

handle_log_file = os.path.join(common_dir, "handle_log.py")  # 封装的日志

handle_config_file = os.path.join(common_dir, "handle_config.py")   # 配置文件方法

# Configs 目录地址
configs_dir = os.path.join(base_dir, "Configs")
global_file = os.path.join(configs_dir, "global.ini")
write_config_file = os.path.join(configs_dir, "write_config.ini")

# Outputs 目录地址
outputs_dir = os.path.join(base_dir, "OutPuts")
logs_dir = os.path.join(outputs_dir, "logs")
log_filename = os.path.join(logs_dir, "cases.log")   # 日志文件
screenshots_dir = os.path.join(outputs_dir, "screenshots")   # 截图保存路径
reports_dir = os.path.join(outputs_dir, "reports")
allure_reports_dir = os.path.join(outputs_dir, "allure-server-report")   # allure报告文件

report_file = os.path.join(reports_dir, "Test_Oms_UI.html")   # HTML报告路径

# TestCases 目录地址
test_cases_dir = os.path.join(base_dir, "TestCases")   # 测试用例文件目录

# TestDatas 目录地址
test_datas_dir = os.path.join(base_dir, "TestDatas")   # 测试数据文件目录
common_datas_file = os.path.join(test_datas_dir, "common_datas.py")  # 基础数据
# test_file = os.path.join(test_datas_dir, "test.xlsx")   # 上传文件的目录