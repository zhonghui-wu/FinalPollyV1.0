# Author:  wuxianfeng
# Company: songqin
# File:    productlistPage.py
# Date:    2021/9/27
# Time:    9:39
from common.basePage import BasePage


class ProductListPage(BasePage):
    """
    商品列表页面
    功能:
    1. 获取第一个商品名称 #用于验证添加商品是否成功
    """
    def get_first_productname(self):
        return self.get_element_text(self.first_product)