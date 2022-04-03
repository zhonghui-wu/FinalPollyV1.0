# Author:  wuxianfeng
# Company: songqin
# File:    handle_loguru.py
# Date:    2021/9/26
# Time:    21:26
from configparser  import  ConfigParser
from loguru import logger
from utils.handle_path import logs_path, config_path
from time import strftime
class MyLog():
    __instance = None #单例实现
    __init_flag = True #控制init调用，如果调用过就不再调用
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self):
        if self.__init_flag: #看是否调用过
            __curdate = strftime('%Y%m%d-%H%M')
            cfg = ConfigParser()
            cfg.read(config_path+'loguru.ini',encoding='utf-8')
            logger.remove(handler_id=None)  #关闭console输出
            logger.add(logs_path+'AutoPolly_'+__curdate+'.log', #日志存放位置
                       retention=cfg.get('log','retention'), #清理
                       rotation=cfg.get('log','rotation'), #循环 达到指定大小后建立新的日志
                       format=cfg.get('log','format'), #日志输出格式
                       level=cfg.get('log','level')) #日志级别
            self.__init_flag = False #如果调用过就置为False
    def info(self,msg):
        logger.info(msg)
    def warning(self,msg):
        logger.warning(msg)
    def critical(self,msg):
        logger.critical(msg)
    def error(self,msg):
        logger.error(msg)
    def debug(self,msg):
        logger.debug(self,msg)
log = MyLog()
if __name__ == '__main__':

        log1 = MyLog()
        log1.critical('test critical')
        from time import sleep
        sleep(1)
        log2 = MyLog()
        log2.error('test error')
        print(id(log1))
        print(id(log2))