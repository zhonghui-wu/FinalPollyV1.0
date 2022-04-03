# Author:  wuxianfeng
# Company: songqin
# File:    handle_path.py
# Date:    2021/9/26
# Time:    17:05

import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(project_path,'config\\')
utils_path = os.path.join(project_path,'utils\\')
common_path = os.path.join(project_path,'common\\')
testdata_path = os.path.join(project_path,'case_datas\\')
logs_path = os.path.join(project_path,'outputs\\logs\\')
screenshots_path = os.path.join(project_path, 'outputs\\screenshots\\')
reports_path = os.path.join(project_path, 'outputs\\reports\\')
if __name__ == '__main__':
    print(config_path+'project_config.py')