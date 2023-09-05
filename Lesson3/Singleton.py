#Цель шаблона Singleton заключаются в следующем:
# - Обеспечение создания одного и только одного объекта класса
# - Предоставление точки доступа для объекта, который является глобальным для программы
# - Контроль одновременного доступа к ресурсам, которые являются общими
#Простой способ реализации Singleton – сделать закрытым метод конструктора и создать статический метод, 
#который выполняет инициализацию объекта. Таким образом, один объект создается при первом вызове, 
#а класс будет всегда возвращать тот же объект при попытки новой инициализации объекта.

#Шаблон Singleton:
#Реализуйте паттерн Singleton на языке Python для класса Logger, 
#который будет использоваться для логирования информации в приложении. 
#Гарантируйте, что только один экземпляр класса Logger будет создан.

# -*- coding: utf-8 -*-
import logging
import os
import datetime
import time


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# python 3 style
class MyLogger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        dirname = "./log"

        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

        streamHandler = logging.StreamHandler()

        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

        print("Generate new instance")

    def get_logger(self):
        return self._logger

# a simple usecase 
if __name__ == "__main__":
    logger = MyLogger.__call__().get_logger()
    logger.info("Hello, Logger")
    logger.debug("bug occured")