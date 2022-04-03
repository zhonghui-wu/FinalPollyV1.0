# Author:  wuxianfeng
# Company: songqin
# File:    addproductattrPage.py
# Date:    2021/9/27
# Time:    13:42
from common.basePage import BasePage


class AddProductAttributePage(BasePage):
    """
    添加商品属性页面
    """
    def addproductattr(self,attrname,pl1,attrtype):
        """
        添加商品属性
        :param attrname: 商品属性名称
        :param pl1: 商品一级菜单第几个，1是第一个
        :param attrtype: 类型:1表示属性，2表示规格,字符串格式
        :return:
        """
        #1. 输入商品属性名称
        self.input_text(self.attr_name_input,attrname)
        #2. 点击商品类型
        self.click_element(self.type_select)
        #3. 点击商品类型一级菜单
        self.type_select_idx[-1]=self.type_select_idx[-1].replace('%s',pl1)
        self.wait_click_element(self.type_select_idx)
        #4. 选择类型
        self.product_type_radio[-1]=self.product_type_radio[-1].replace('%s',attrtype)
        self.click_element(self.product_type_radio)
        #5. 点击提交
        self.click_element(self.submit_btn)
        #6. 点击确定
        self.wait_click_element(self.sure_btn)

