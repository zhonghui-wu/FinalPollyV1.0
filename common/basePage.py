# Author:  wuxianfeng
# Company: songqin
# File:    basePage.py
# Date:    2021/9/26
# Time:    16:49
from common.comm_driver import CommDriver
from config.project_config import wait_timeout, wait_poll_frequency
from utils.handle_yaml import get_yaml_data
from utils.handle_path import common_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.handle_path import logs_path,screenshots_path
class  BasePage():

    """
    页面基类
    功能：
        1. 初始化得到一个浏览器
        2. 打开一个URL
        3. 获取页面上的一个元素
        4. 点击元素
        5. 在元素上输入内容
        补充:
        6. 获取元素的文本   #触发条件: 测试登录，判断登录后首页的元素文本是否是'首页'
        7. 增加一个等待元素出现后点击的方法 #触发条件点击个人中心后来不及点退出
        8. 输入了错误的用户名和密码后提示信息太快，导致无法获取到，获取元素信息也要等待
    """
    def __init__(self):
        """
        初始化得到一个浏览器
        """
        self.locators = get_yaml_data(common_path+'elements.yaml')[self.__class__.__name__]
        for element,locator in self.locators.items():
            setattr(self,element,locator)
        self.driver = CommDriver().get_driver()
    def  open_url(self,url):
        """
        打开一个URL
        :param url: 指定的url地址
        :return: None
        """
        self.driver.get(url)
    def  get_element(self,locator):
        """
        获取页面上的一个元素
        :param locator: 元素定位器
        :return: 返回一个webelement对象
        """
        return self.driver.find_element(*locator)
    def  get_elements(self,locator):
        """
        获取页面上的一个元素
        :param locator: 元素定位器
        :return: 返回一个webelement对象
        """
        return self.driver.find_elements(*locator)
    def  click_element(self,locator):
        """
        点击元素
        :param locator: 元素定位器
        :return: None
        """
        self.get_element(locator).click()
    def  input_text(self,locator,text,append=False):
        """
        在元素上输入内容
        :param locator: 元素定位器
        :param text: 在元素上输入的文本
        :param append: 是否追加输入，如果是True就追加，默认清空后再输入
        :return: None
        """
        if not append:
            self.get_element(locator).clear()  #注意要先清空，处理一些元素上的默认值或者提示信息
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).send_keys(text)

    def  get_element_text(self,locator):
        """
        获取一个元素的text
        :param locator:定位器
        :return: 元素text
        """
        return self.get_element(locator).text
    def  get_element_texts(self, locator):
        """
        获取一组元素的text
        :param locator:定位器
        :return: 元素text组成的列表
        """
        eles = self.get_elements(locator)
        return [ele.text for ele in eles]
    def  wait_click_element(self, locator):
        WebDriverWait(self.driver,
                      timeout=wait_timeout,
                      poll_frequency=wait_poll_frequency)\
            .until(EC.visibility_of_element_located(locator)).click()
    def  wait_get_element_text(self,locator):
        """
        等待一定时间后获取元素的文本
        :param locator: 元素的定位器
        :return:
        """
        return WebDriverWait(self.driver,
                      timeout=wait_timeout,
                      poll_frequency=wait_poll_frequency)\
            .until(EC.visibility_of_element_located(locator)).text
    def  isexist_element(self,locator,Action=None):
        '''
        判断元素是否存在，注意要加异常捕获，不然还是超时
        :param locator:
        :param Action:
        :return:
        '''
        try:
            element = WebDriverWait(self.driver,
                      timeout=wait_timeout,
                      poll_frequency=wait_poll_frequency) \
            .until(EC.element_to_be_clickable(locator))
            return element
        except:
            self.driver.save_screenshot(screenshots_path+f'{Action}.png')
            from utils.handle_loguru import log
            log.error(f'{Action}元素无法定位')
            return False