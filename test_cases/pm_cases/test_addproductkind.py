# Author:  wuxianfeng
# Company: songqin
# File:    test_addproductkind.py
# Date:    2021/9/27
# Time:    15:01
import pytest
import allure
from utils.handle_randstr import get_rand_str
@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:测试添加商品分类')
@allure.title('case:测试成功添加商品分类')
@allure.severity('normal')
def test_addproductkind(init_mainpage):
    """
    测试成功添加商品分类
    :param init_mainpage: 登录系统
    :return:
    """
    with allure.step('1. 登录系统进入首页'):
        mainpage = init_mainpage
    with allure.step('2. 添加商品分类'):
        test_kindname = '商品分类'+get_rand_str(5)
        mainpage.goto_productkind().goto_addproductkind()\
            .add_product_kind(test_kindname,'1','1','1','2','2','2')
    with allure.step('3. 断言'):
        assert test_kindname == mainpage.goto_productkind().get_last_productkind()
if __name__ == '__main__':
    pytest.main(['-sv',__file__])
