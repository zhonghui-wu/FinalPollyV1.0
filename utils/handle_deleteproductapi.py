# Author:  wuxianfeng
# Company: songqin
# File:    handle_delapi.py
# Date:    2021/9/19
# Time:    15:00

import requests
import jsonpath
from config.project_config import polly_api_url,pollyurl,username,password

def del_product_id(id):
    '''
    通过传递的id的值来删除商品数据
    :param id: 商品的id
    :return: None
    '''
    login_url = f'{polly_api_url}sys/sysUser/login' #地址不要多/
    login_data = dict(username=username,password=password)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    req = requests.post(login_url,json=login_data)
    token = jsonpath.jsonpath(req.json(),'$..token')[0]
    delete_url = f'{polly_api_url}pms/PmsProduct/delete/{id}'  #地址不要多/
    headers['Authorization']='Bearer {}'.format(token)
    requests.get(delete_url,headers=headers)
if __name__ == '__main__':
    from selenium import webdriver
    driver  = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(pollyurl)
    driver.find_element_by_css_selector('#username').send_keys('松勤老师')
    driver.find_element_by_css_selector('#password').send_keys('123456')
    driver.find_element_by_css_selector('#btnLogin').click()
    driver.find_element_by_xpath("//span[text()='商品管理']").click()
    driver.find_element_by_xpath("//span[text()='商品列表']").click()
    first_product_id = driver.find_element_by_css_selector(".el-table__row:nth-child(1)>td:nth-child(2)>.cell").text
    del_product_id(first_product_id)
    driver.refresh()
