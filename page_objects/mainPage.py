# Author:  wuxianfeng
# Company: songqin
# File:    mainPage.py
# Date:    2021/9/27
# Time:    8:31
from common.basePage import BasePage
from page_objects.pmpage_objects.addproductPage import AddProductPage
from page_objects.pmpage_objects.brandmanagePage import BrandManagePage
from page_objects.pmpage_objects.productattrPage import ProductAttributePage
from page_objects.pmpage_objects.productkindPage import ProductKindPage
from page_objects.pmpage_objects.productlistPage import ProductListPage
from page_objects.pmpage_objects.producttypePage import ProductTypePage


class MainPage(BasePage):
    """
    首页类
    """
    def goto_productlist(self):
        """
        去商品管理->商品列表页面
        :return:商品列表页
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_productlist)
        return ProductListPage()
    def goto_brandmanage(self):
        """
        去商品管理->品牌管理页面
        :return:品牌管理页
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_brandmanage)
        return BrandManagePage()
    def goto_productkind(self):
        """
        去商品管理->商品分类页面
        :return:
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_productkind)
        return ProductKindPage()
    def goto_producttype(self):
        """
        去商品管理->商品类型页面
        :return:
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_producttype)
        return ProductTypePage()
    def goto_addproduct(self):
        """
        去商品管理->添加商品页面
        :return:添加商品页
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_addproduct)
        return AddProductPage()
    def goto_productattr(self):
        """
        去商品管理->商品规格页面
        :return:
        """
        self.click_element(self.menu_productmanage)
        self.click_element(self.submenu_pm_productattr)
        return ProductAttributePage()
    def logout_mainpage(self):
        """
        回到登录页面  #触发条件，测试添加商品，然后再测试，从头开始。
        :return:
        """
        self.click_element(self.personal_button)
        self.wait_click_element(self.logout_button)
if __name__ == '__main__':
    from page_objects.loginPage import LoginPage
    #优化前的调用
    # test_loginpage = LoginPage().open_loginpage().login_system('松勤老师','123456')
    # test_mainpage = MainPage()
    # test_mainpage.goto_productlist()
    #优化后的调用
    test_mainpage = LoginPage().open_loginpage().login_system('松勤老师','123456')
    test_mainpage.goto_addproduct()