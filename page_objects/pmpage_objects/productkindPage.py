# Author:  wuxianfeng
# Company: songqin
# File:    productkindPage.py
# Date:    2021/9/27
# Time:    14:40
from common.basePage import BasePage
from page_objects.pmpage_objects.addproductkindPage import AddProductKindPage
from time import sleep

class ProductKindPage(BasePage):
    """
    商品分类页
    """
    def goto_addproductkind(self):
        """
        去添加商品分类页
        :return:
        """
        self.click_element(self.add_btn)
        return AddProductKindPage()
    def get_last_productkind(self):
        self.click_element(self.last_page_btn)
        sleep(1)
        return self.wait_get_element_text(self.last_kind_name)