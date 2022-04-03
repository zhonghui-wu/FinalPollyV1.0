# Author:  wuxianfeng
# Company: songqin
# File:    addbrandPage.py
# Date:    2021/9/27
# Time:    11:23
from common.basePage import BasePage


class AddBrandPage(BasePage):
    """
    添加品牌页面
    """
    def addbrand(self,bname):
        """
        添加品牌
        :param bname:品牌名字
        :return:
        """
        from time import sleep
        sleep(2)
        self.input_text(self.brand_name_input,bname)
        self.click_element(self.commit_btn)
        self.click_element(self.confirm_btn)
