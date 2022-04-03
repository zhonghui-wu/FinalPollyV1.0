# Author:  wuxianfeng
# Company: songqin
# File:    test_addproducttype.py
# Date:    2021/9/27
# Time:    15:52


import pytest,allure
from utils.handle_randstr import get_rand_str
@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:测试添加商品类型')
@allure.title('case:测试成功添加商品类型')
def test_addproducttype(init_mainpage):
    with allure.step('1. 登录系统进入首页'):
        mainpage  = init_mainpage
    with allure.step('2. 添加商品类型'):
        test_typename = '商品类型'+get_rand_str(5)
        print(test_typename)
        mainpage.goto_producttype().addproducttype(test_typename,'1','1')
    with allure.step('3. 断言'):
        #最后一个类型的名字 = 测试时用的
        assert  test_typename == mainpage.goto_producttype().get_lasttypename()
if __name__ == '__main__':
    pytest.main(['-sv',__file__])