# Author:  wuxianfeng
# Company: songqin
# File:    project_config.py
# Date:    2021/9/26
# Time:    16:15

#[browser config]
def_browname = 'chrome'  #默认浏览器是chrome
headless_flag = False     #默认为有头模式，
def_impwait_time = 20     #隐式等待默认20s

#[project config]
pollyurl = 'http://120.55.190.222:38090/#/login'  #宝利商城的URL地址

#[wait config]
wait_timeout = 20
wait_poll_frequency = 0.5
#[account]
username,password = '松勤老师','123456'
#[API]
polly_api_url = 'http://120.55.190.222:38085/'