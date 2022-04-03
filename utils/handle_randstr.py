# Author:  wuxianfeng
# Company: songqin
# File:    handle_randstr.py
# Date:    2021/9/27
# Time:    9:17
from random import sample
from string import digits,ascii_letters

def get_rand_str(length):
    return ''.join(sample(ascii_letters+digits,length))

if __name__ == '__main__':
    print(get_rand_str(5))
