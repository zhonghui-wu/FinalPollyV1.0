# Author:  wuxianfeng
# Company: songqin
# File:    addproductkindPage.py
# Date:    2021/9/27
# Time:    14:50
from common.basePage import BasePage


class AddProductKindPage(BasePage):
    """
    添加商品分类页
    """
    def add_product_kind(self, kind_name,
                         kind_idx=None,
                         number=None,
                         sorting_num=None,
                         show=None,
                         show_navigation=None,
                         show_home_page=None):
        """
        添加商品分类方法
        :param kind_name:分类名字
        :param kind_idx:上级分类
        :param number:数量单位
        :param sorting_num:排序
        :param show:是否显示
        :param show_navigation:是否显示在导航栏
        :param show_home_page:是否显示在首页
        :return:
        """
        # 输入分类名称
        self.input_text(self.cate_name_input, kind_name)
        # 选择上级分类
        if not kind_idx:
            self.click_element(self.kind_select)
            # 点击某个分类
                # 这个分类是1的话就是无上级分类
            self.kind_select_idx[-1] = self.kind_select_idx[-1].replace('%s', kind_idx)
            self.click_element(self.kind_select_idx)
        if not number:
            # 输入数量单位
            self.input_text(self.number_input, number)
        # 输入排序
        if not sorting_num:
            self.input_text(self.sorting_input, sorting_num)
        # 是否显示
        if not show:
            self.is_show[-1] = self.is_show[-1].replace("%s", show)
            self.click_element(self.is_show)
        if not show_navigation:
        # 是否显示在导航栏
            self.is_show_navigation[-1] = self.is_show_navigation[-1].replace("%s", show_navigation)
            self.click_element(self.is_show_navigation)
        # 是否显示在首页
        if not show_home_page:
            self.is_show_home_page[-1] = self.is_show_home_page[-1].replace('%s', show_home_page)
            self.click_element(self.is_show_home_page)
        # 点击提交按钮
        self.click_element(self.submit_btn)
        # 确认提交
        self.click_element(self.primary_submit_btn)