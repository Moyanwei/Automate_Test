# 正常场景测试数据
oms_success_data = [{'membMobile': '15691750516', 'membPassword': 'sdh168168'}]

login_user = {'membMobile': '18858541566', 'membPassword': 'sdh123456'}

# 异常场景测试数据
error_passwordFormat_data = [{'membMobile': '15691750516',
                              'membPassword': '12345',
                              'errorMsg': '账号或密码错误!',
                              'dataName': '密码少于6位登录失败'},
                             {'membMobile': '15691750516',
                              'membPassword': '1234567890',
                              'errorMsg': '账号或密码错误!',
                              'dataName': '密码超过6位登录失败'},
                             {'membMobile': '15691750516',
                              'membPassword': '',
                              'errorMsg': '请输入密码!',
                              'dataName': '密码为空位登录失败'}]
