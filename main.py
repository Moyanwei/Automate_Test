import pytest

if __name__ == '__main__':
    pytest.main(['--html=OutPuts/reports/Test_Oms_UI.html',
                 '--alluredir=OutPuts/allure-server-report'])
