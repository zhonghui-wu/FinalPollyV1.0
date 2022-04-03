print()
"""
日志相关内容：
    1- 日志的输出渠道：文件xxx.log    控制台输出
    2- 日志级别： DEBUG-INFO-WARNING-ERROR-CRITICAL
    3- 日志的内容：2021-10-20 13:50:52,766 - INFO - handle_log.py[49]:我是日志信息
                  年- 月 - 日 时:分:秒,毫秒       -级别   -哪个文件[哪行]:具体报错信息
"""
from time import strftime
import logging
from utils.handle_path import logs_path
def logger(fileLog=True,name=__name__):
    """
    :param fileLog: bool值，如果为True则记录到文件中否则记录到控制台
    :param name: 默认是模块名
    :return: 返回一个日志对象
    """
    #0 定义一个日志文件的路径，在工程的logs目录下，AutoPolly开头-年月日时分.log
    logDir = f'{logs_path}/AutoPolly-{strftime("%Y%m%d%H%M")}.log'
    #1 创建一个日志收集器对象
    logObject = logging.getLogger(name)
    #2- 设置日志的级别
    logObject.setLevel(logging.INFO)
    #3- 日志内容格式
    fmt = "%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]:%(message)s"
    formater = logging.Formatter(fmt)

    if fileLog:#log文件模式
        #设置日志渠道--文件输出
        handle = logging.FileHandler(logDir,encoding='utf-8')
        #日志内容与渠道绑定
        handle.setFormatter(formater)
        #把日志对象与渠道绑定
        logObject.addHandler(handle)
    else:
        #设置日志渠道--控制台输出
        handle2 = logging.StreamHandler()
        #日志内容与渠道绑定
        handle2.setFormatter(formater)
        #把日志对象与渠道绑定
        logObject.addHandler(handle2)

    return logObject

log = logger()#控制台输出日志

if __name__ == '__main__':
    log = logger()#控制台输出日志
    log.info('我是日志信息')