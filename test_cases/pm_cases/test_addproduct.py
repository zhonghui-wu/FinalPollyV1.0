# Author:  wuxianfeng
# Company: songqin
# File:    test_addproduct.py
# Date:    2021/9/27
# Time:    9:13
import os

from utils.handle_path import reports_path
from utils.handle_randstr import get_rand_str
import pytest
import allure
@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:测试添加商品')
class TestAddProduct():
    @allure.severity('normal')
    @allure.testcase(url='https://cn.bing.com/',name='测试成功添加产品1')
    @allure.title('测试成功添加产品1')
    def test_addproduct_b(self,init_mainpage):
        """
        测试添加商品是否成功V1
        :return:
        """
        with allure.step('step1: 登录系统进入首页'):
            # test_mainpage = LoginPage().open_loginpage().login_system('松勤老师','123456')
            test_mainpage = init_mainpage
        with allure.step('step2: 添加商品页面'):
            test_addproductpage = test_mainpage.goto_addproduct()
        with allure.step('step3: 添加商品'):
            test_pname = '商品名称' + get_rand_str(5)
            test_subtile = '副标题' + get_rand_str(5)
            test_addproductpage.add_product(1,1,test_pname,test_subtile,1)
        # sleep(2)
        with allure.step('step4: 回主页'):
            test_addproductpage.back_mainpage()
            expect_pname = test_mainpage.goto_productlist().get_first_productname()
        with allure.step('step5: 断言'):
            assert test_pname==expect_pname
            # test_mainpage.driver.quit()  #这是失败的，对象没了
            #test_mainpage.logout_mainpage()
    @allure.testcase(url='https://www.baidu.com/',name='测试成功添加产品2')
    @allure.title('测试成功添加产品2')
    def test_addproduct_a(self,init_mainpage):
        # test_mainpage = LoginPage().open_loginpage().login_system('松勤老师','123456')
        with allure.step('step1: 登录系统进入首页'):
            test_mainpage = init_mainpage
        with allure.step('step2: 添加商品页面'):
            test_addproductpage = test_mainpage.goto_addproduct()
        with allure.step('step3: 添加商品'):
            test_pname  = '商品名称'+get_rand_str(5)
            test_subtile = '副标题'+get_rand_str(5)
            test_addproductpage.add_product(1,1,test_pname,test_subtile,1)
            # sleep(2)
        with allure.step('step4: 回主页'):
            test_addproductpage.back_mainpage()
            expect_pname = test_mainpage.goto_productlist().get_first_productname()
        with allure.step('step5: 断言'):
            assert test_pname==expect_pname
        #如果要一个用例跑多次，那你能实现一下吗？
        #思路是可以回到登录页面
if __name__ == '__main__':
    pytest.main(['-sv','test_addproduct.py','--alluredir',reports_path,'--clean-alluredir'])
    os.system(f'allure serve {reports_path}')