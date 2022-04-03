# Author:  wuxianfeng
# Company: songqin
# File:    producttypePage.py
# Date:    2021/9/27
# Time:    15:18
from common.basePage import BasePage
from time import sleep

class ProductTypePage(BasePage):
    """
    商品类型页面
    """
    def addproducttype(self,
                       typename,style,isshow):
        """
        添加商品类型
        :param typename: 类型名称
        :param style:列表央视
        :param isshow:是否展示,1展示,2不展示
        :return:
        """
        #1. 点击添加按钮
        self.click_element(self.add_product_type_btn)
        #2. 输入商品类型
        self.input_text(self.type_name_input,typename)
        #3. 点击样式
        self.list_style_radio_btn[-1]=self.list_style_radio_btn[-1].replace('%s',style)
        self.click_element(self.list_style_radio_btn)
        #4. 点击是否展示在首页
        self.is_show_on_home_btn[-1]=self.is_show_on_home_btn[-1].replace('%s',isshow)
        self.click_element(self.is_show_on_home_btn)
        #5. 点击确定
        self.click_element(self.confirm_btn)

    def get_lasttypename(self):
        """
        获取最后一个商品类型的名字
        :return:
        """
        #1. 点击最后一页的按钮
        self.click_element(self.last_page_btn)
        sleep(1) #此处不等待非常容易出错
        return self.get_element_text(self.last_type_name)