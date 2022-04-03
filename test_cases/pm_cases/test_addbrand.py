# Author:  wuxianfeng
# Company: songqin
# File:    test_addbrand.py
# Date:    2021/9/27
# Time:    11:27
from utils.handle_randstr import get_rand_str
from utils.handle_path import reports_path
import os
import  pytest,allure
@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:添加品牌')
@allure.title('case1:测试成功添加品牌')
def test_addbrand(init_mainpage):
    with allure.step('1. 登录系统进入首页'):
        mainpage = init_mainpage
    with allure.step('2. 切换到品牌管理'):
        test_brandpage = mainpage.goto_brandmanage()
    with allure.step('3. 切换到添加品牌'):
        test_addbrandpage = test_brandpage.goto_addbrand()
    with allure.step('4. 添加品牌'):
        test_bname = '品牌名字'+get_rand_str(5)
        test_addbrandpage.addbrand(test_bname)
    with allure.step('5. 获取最后一个品牌名'):
        expect_bname = mainpage.goto_brandmanage().get_lastbrandname()
    with allure.step('6. 断言'):
        assert test_bname == expect_bname
if __name__ == '__main__':
    pytest.main(['-sv','test_addbrand.py','--alluredir',reports_path,'--clean-alluredir'])
    os.system(f'allure serve {reports_path}')