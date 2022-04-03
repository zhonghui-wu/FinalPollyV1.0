# Author:  wuxianfeng
# Company: songqin
# File:    handle_yaml.py
# Date:    2021/9/26
# Time:    17:04
import yaml
from pprint import pprint
from utils.handle_path import common_path,testdata_path
def get_yaml_data(file):
    with open(file,encoding='UTF-8') as f:
        return yaml.safe_load(f.read())
if __name__ == '__main__':
    pprint(get_yaml_data(testdata_path+'test_login_data_success.yaml'))