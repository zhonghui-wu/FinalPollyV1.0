# Author:  wuxianfeng
# Company: songqin
# File:    comm_driver.py
# Date:    2021/9/26
# Time:    16:00
from selenium import webdriver
from config.project_config import def_browname, headless_flag, def_impwait_time

class Singe(object):
    """
    单例的一种实现
    """
    _instance = None  #这个类变量用来存放实例
    def __new__(cls, *args, **kwargs): #
        if cls._instance is None:  #如果这个类没有实例
            cls._instance = super().__new__(cls)  #那就new一个
        return cls._instance  #返回实例

class Single1(object):
    """
    单例的另一种实现，其实是跟上面类似的，但单例还有很多其他方法的实现。可以去学习
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            #__instance私有变量，类没有__instance这个变量（不能直接看到）
            cls._instance = super().__new__(cls)
        return cls._instance

class CommDriver(Singe):
    """
    1. 通用的浏览器类
    """
    driver = None  #设置一个类属性
    def get_driver(self,
                   browname=def_browname,
                   headless=headless_flag,
                   implicitly_wait_time=def_impwait_time):
        """
        1. 获取浏览器对象
        :param browname: 浏览器名字，目前支持
        :param headless: 是否有头，True是无头，False是有头
        :param implicitly_wait_time: 隐式等待时间
        :return: 返回一个浏览器
        """

        if self.driver is None:  #如果获取过浏览器了，这个就有值了不会再做下面的事情
            if not headless:
                if browname == 'chrome':
                    self.driver = webdriver.Chrome()

                elif browname == 'firefox':
                    self.driver = webdriver.Firefox()
                else:
                    raise Exception(f'{browname} is not supported')
            else:
                if browname == 'chrome':
                    self.__option = webdriver.ChromeOptions()
                    self.__option.add_argument('-headless')
                    self.driver = webdriver.Chrome(options=self.__option)
                elif browname == 'firefox':
                    self.__option = webdriver.FirefoxOptions()
                    self.__option.add_argument('-headless')
                    self.driver = webdriver.Firefox(options=self.__option)
                else:
                    raise Exception(f'{browname} is not supported')
            self.driver.maximize_window()
            self.driver.implicitly_wait(implicitly_wait_time)
        return self.driver

if __name__ == '__main__':
    test_driver1 = CommDriver()
    test_driver1.get_driver()
    test_driver2 = CommDriver()
    test_driver2.get_driver()
    print(id(test_driver2)==id(test_driver1))