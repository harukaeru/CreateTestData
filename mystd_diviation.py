# -*- coding: utf-8 -*-
""" The module to calculate the standard diviation of the list. (標準偏差) """

from __future__ import division

divideSumByAll = lambda sumNum, lt: sumNum / len(lt)

def calc_avarage(lt):
    """ Calculate the avarage of the list. (相加平均) """

    sumNum = 0
    for num in lt:
        sumNum += num

    return divideSumByAll(sumNum, lt)

def calc_variance(lt):
    """ Calculate the variance of the list. (分散) """

    av = calc_avarage(lt)
    sumNum = 0
    for num in lt:
        sumNum += ((av - num) ** 2)

    return divideSumByAll(sumNum, lt)

def calc_diviation(lt):
    """ root of variance """

    from math import sqrt
    return sqrt(calc_variance(lt))

