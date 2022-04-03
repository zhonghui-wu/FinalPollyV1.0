# Author:  wuxianfeng
# Company: songqin
# File:    test_addproductattr.py
# Date:    2021/9/27
# Time:    13:51
import os

import pytest,allure

from utils.handle_path import reports_path
from utils.handle_randstr import get_rand_str
@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:测试添加商品规格')
@allure.title('case:测试成功添加商品规格')
def test_addprodctattr(init_mainpage):
    with allure.step('1. 登录系统进入首页'):
        test_mainpage = init_mainpage
    with allure.step('2. 跳转到商品规格页面再跳转到添加规格'):
        test_addproductattrpage = test_mainpage.goto_productattr().goto_addproductattr()
    with allure.step('3. 添加商品规格'):
        test_attrname = '商品规格'+get_rand_str(5)
        test_addproductattrpage.addproductattr(test_attrname,'1','1')
    # from time import sleep
    # sleep(2)
    with allure.step('4. 断言'):
        assert test_attrname in test_mainpage.goto_productattr().get_allattr()

if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir',reports_path,'--clean-alluredir'])
    os.system(f'allure serve {reports_path}')