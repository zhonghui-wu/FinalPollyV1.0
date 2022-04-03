# Author:  wuxianfeng
# Company: songqin
# File:    addproductPage.py
# Date:    2021/9/27
# Time:    8:44
from common.basePage import BasePage


class AddProductPage(BasePage):
    """
    添加商品页面
    1. 跳转到商品列表页面
    2. 回首页
    3. 添加商品页
    """
    def goto_productlist(self):
        self.wait_click_element(self.submenu_pm_productlist)
    def back_mainpage(self):
        self.wait_click_element(self.home_button)
    def add_product(self,kl1,kl2,pname,subtitle,bl1):
        """
        添加商品
        :param kl1: 商品分类一级菜单
        :param kl2: 商品分类二级菜单
        :param pname: 商品名称
        :param subtitle: 副标题
        :param bl1: 商品品牌
        :return: None
        """
        # 1. 点击商品分类
        self.click_element(self.product_kind_select)
        # 2. 点击商品分类一级菜单
        self.product_kind_select_index1[-1]= self.product_kind_select_index1[-1].format(kl1)
        self.click_element(self.product_kind_select_index1)
        # 3. 点击商品分类二级菜单
        self.product_kind_select_index2[-1]=self.product_kind_select_index2[-1].format(kl2)
        self.click_element(self.product_kind_select_index2)
        # 4. 输入商品名称
        self.input_text(self.product_name,pname)
        # 5. 输入副标题
        self.input_text(self.product_subtitle,subtitle)
        # 6. 点击商品品牌
        self.wait_click_element(self.product_brand_select)
        # 7. 点击商品品牌一级菜单
        self.product_brand_select_idx[-1]=self.product_brand_select_idx[-1].format(bl1)
        self.wait_click_element(self.product_brand_select_idx)
        # 8. 点击下一步商品促销
        self.click_element(self.next_commodity_promotion_btn)
        # 9. 点击下一步，填写商品属性
        self.click_element(self.next_product_attribute_btn)
        # 10.点击下一步，选择商品关联
        self.click_element(self.netxt_product_related_btn)
        # 11.点击完成，提交商品
        self.click_element(self.complete_btn)
        # 12.点击确定
        self.click_element(self.submit_btn)
if __name__ == '__main__':
    from page_objects.loginPage import LoginPage
    test_mainpage = LoginPage().open_loginpage().login_system('松勤老师','123456')
    test_addproductpage = test_mainpage.goto_addproduct()
    test_addproductpage.add_product(1,1,'测试092701','副标题0927',1)