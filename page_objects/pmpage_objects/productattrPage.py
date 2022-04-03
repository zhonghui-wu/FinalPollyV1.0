# Author:  wuxianfeng
# Company: songqin
# File:    productattrPage.py
# Date:    2021/9/27
# Time:    13:37
from common.basePage import BasePage
from page_objects.pmpage_objects.addproductattrPage import AddProductAttributePage


class ProductAttributePage(BasePage):
    """
    商品规格页面
    功能1:
    """
    def goto_addproductattr(self):
        self.click_element(self.add_btn)
        return AddProductAttributePage()
    def get_allattr(self):
        """
        获取当前页的所有属性
        :return:
        """
        return self.get_element_text(self.all_attr_name_txt)

