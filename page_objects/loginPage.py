# Author:  wuxianfeng
# Company: songqin
# File:    loginPage.py
# Date:    2021/9/26
# Time:    16:58
from common.basePage import BasePage
from config.project_config import pollyurl
from page_objects.mainPage import MainPage


class LoginPage(BasePage):
    def open_loginpage(self):
        self.open_url(pollyurl)
        return self
    def login_system(self,uname,pword):
        self.input_text(self.username_input,uname)
        self.input_text(self.password_input,pword)
        self.click_element(self.login_button)
        return MainPage()
if __name__ == '__main__':
    test = LoginPage()
    test.open_loginpage().login_system('松勤老师','123456')
