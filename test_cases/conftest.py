# Author:  wuxianfeng
# Company: songqin
# File:    conftest.py.py
# Date:    2021/9/26
# Time:    17:32
import pytest
from page_objects.loginPage import LoginPage
from utils.handle_loguru import log
from config.project_config import username,password

def pytest_collection_modifyitems(items):
    #items是用例对象列表
    for item in items:
        #用例名字 item.name
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        #用例的节点
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='session',autouse=True)
def run_all():
    """
    所有测试的setup和teardown
    :return:
    """
    print('\n宝利商城开始测试了')
    # log.error('\n宝利商城开始测试了')
    yield
    # log.error('\n宝利商城测试结束了')
    print('\n宝利商城测试结束了')

@pytest.fixture(scope='session')
def init_mainpage():
    """
    商品管理页面的setup和teardown
    :return:
    """
    mainpage = LoginPage().open_loginpage().login_system(username,password)
    yield mainpage
    mainpage.driver.quit()

