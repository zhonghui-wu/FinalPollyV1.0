# Author:  wuxianfeng
# Company: songqin
# File:    brandmanagePage.py
# Date:    2021/9/27
# Time:    10:46
from common.basePage import BasePage
from page_objects.pmpage_objects.addbrandPage import AddBrandPage


class BrandManagePage(BasePage):
    """
    品牌管理页面
    功能:
    1. 去添加品牌页面
    2. 获取最后一个品牌名称
    """
    def goto_addbrand(self):
        self.click_element(self.add_brand_btn)
        return AddBrandPage()
    def get_lastbrandname(self):
        self.click_element(self.last_page_btn)
        from time import sleep
        sleep(2)
        return self.get_element_text(self.last_brand_name)
    def search_brand(self,brandname):
        self.input_text(self.brand_search_input,brandname)
        self.click_element(self.search_btn)
    def  get_pagebrandnames(self):
        """
        获取当前页所有的品牌名称
        :return:
        """
        return self.get_element_texts(self.all_brand_name_txt)