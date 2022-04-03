# Author:  wuxianfeng
# Company: songqin
# File:    test_searchbrand.py
# Date:    2021/9/27
# Time:    16:39
import random
from time import sleep

import pytest,allure

@allure.epic('史诗:宝利商城测试')
@allure.feature('feature:商品管理模块')
@allure.story('用户故事:测试添加商品类型')
@allure.title('case:测试成功添加商品类型')
def test_searchbrand(init_mainpage):
    with allure.step('1. 登录系统进入首页'):
        test_mainpage = init_mainpage
    with allure.step('2. 进入品牌管理页面'):
        brandpage = test_mainpage.goto_brandmanage()
    with allure.step('3. 在当前页随机取一个品牌名'):
        test_brandname = random.choice(brandpage.get_pagebrandnames())
    with allure.step('4. 搜索你的品牌名'):
        brandpage.search_brand(test_brandname)
        sleep(1)  #不等待也不太行
        results = brandpage.get_pagebrandnames()
    #results.append('捣蛋的') 可以用来测试你的测试方法
    #判断一个字符串是否在列表中的每个元素中（注意这只是示例，不够严谨，原则上应该验证所有的结果都含有）
    #方法一:
    # for result in results:
    #     if test_brandname not in result:
    #         assert False
    # else:
    #     assert True
    #方法二：
    assert len(list(filter(lambda x: test_brandname in x, results))) == len(results)

if __name__ == '__main__':
    pytest.main(['-sv',__file__])
