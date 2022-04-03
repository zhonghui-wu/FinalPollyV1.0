# Author:  wuxianfeng
# Company: songqin
# File:    test_login.py
# Date:    2021/9/26
# Time:    17:21
from page_objects.loginPage import LoginPage
import pytest
import allure
from utils.handle_yaml import get_yaml_data
from utils.handle_path import testdata_path

@pytest.mark.dependency(name='login_success')
@allure.severity('blocker')
@pytest.mark.parametrize('username,password',
                         get_yaml_data(testdata_path+'test_login_data_success.yaml'))
def test_login_success(username,password):
    """
    仅测试成功的案例
    :param username: 用户名
    :param password: 密码
    :return:
    """
    loginpage = LoginPage()
    loginpage.open_loginpage().login_system(username,password)
    assert loginpage.get_element_text(['xpath','//*[text()="首页"]'])=='首页'
    loginpage.click_element(['xpath','//img'])
    loginpage.wait_click_element(['xpath', "//span[text()='退出']"])


@allure.severity('normal')
@pytest.mark.parametrize('username,password,locator,expected',
                         get_yaml_data(testdata_path+'test_login_data_failed.yaml'))
def test_login_failed(username,password,locator,expected):
    """
    仅测试失败的案例
    :param username: 用户名
    :param password: 密码
    :param locator: 失败message的定位器
    :param expected: 预期结果
    :return:
    """
    loginpage = LoginPage()
    loginpage.open_loginpage().login_system(username,password)
    #预期结果和定位的元素是不一样的，所以这是一个变化的内容
    assert loginpage.wait_get_element_text(locator)== expected

@allure.severity('minor')
@pytest.mark.parametrize('username,password,locator,expected',
                         get_yaml_data(testdata_path+'test_login_data_all.yaml'))
@pytest.mark.skip(reason='不想跑')  #这个方法会被collect，但不会执行
def test_login_all(username,password,locator,expected):
    """
    失败和错误都存在的用例
    :param username:
    :param password:
    :param locator:
    :param expected:
    :return:
    """
    loginpage = LoginPage()
    loginpage.open_loginpage().login_system(username,password)
    #预期结果和定位的元素是不一样的，所以这是一个变化的内容
    assert loginpage.wait_get_element_text(locator)== expected
    #issue1:登录失败后找不到相应的元素，导致用例失败了。
    # loginpage.click_element(['xpath','//img'])
    # loginpage.wait_click_element(['xpath', "//span[text()='退出']"])
    #issue2:尝试判断元素存在就点击，没有元素就不点击
    #下面的代码也跑通了
    if loginpage.isexist_element(['xpath',"//span[text()='首页']"],Action=expected):
        loginpage.click_element(['xpath','//img'])
        loginpage.wait_click_element(['xpath', "//span[text()='退出']"])
    #issue3:比较好的做法
    # if loginpage.driver.current_url == 'http://120.55.190.222:38090/#/home':
    #     loginpage.click_element(['xpath','//img'])
    #     loginpage.wait_click_element(['xpath', "//span[text()='退出']"])



if __name__ == '__main__':
    pytest.main(['-srs','test_login.py'])