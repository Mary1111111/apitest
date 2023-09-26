# 导包
import tool
import logging.handlers
# 新建类
class  GetLog:
    # 新建日志器变量
    __logger = None
    # 新建获取日志器方法
    @classmethod
    def  get_logger(cls,log_path = 'D:\python\pythonProject5\log\kjtt.log'):
        # 判断日志器是不是为空
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器

            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 获取格式器
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(formatter)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        return cls.__logger

