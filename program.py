#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
#модуль для математики
import numpy
#очередной модуль для математики(:
import matplotlib.pyplot as mpp
#модуль для построения графиков
if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]#создание списка аргументов функции
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )#задает параметр рафика
    mpp.show()#выводит график на экран
