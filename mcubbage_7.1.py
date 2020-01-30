#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:29:35 2020
Assignment 02 Building Complex Programs from smaller Parts exercise 7.1
@author: mcubbage
"""

#import math to be able to take sqaure root of numbers
import math
#create function mysqrt that finds square root of a number using newton's method
def mysqrt(a,x):
    while true:
        print(x)
        y=(x+a/x)/2
        if y ==x:
            break
        x=y
    return x

#test mysqrt 
mysqrt(4,3)

#define function that uses python's internal square root function
def real_sr(a):
    return math.sqrt(a)
    

#test real_sr
real_sr(9)



#write a function called test_square_root that prints a,mysqrt(a),real_sr(a), and the difference between the two function outputs
def test_square_root():
    from decimal import Decimal
    a = 1
    x = 4
    while a < 10:
        y = Decimal(format(mysqrt(a,x),".10f"))
        square_method = Decimal(format(math.sqrt(a), ".10f"))
        diff = format(y - square_method, ".10f")
        print("\t", a, "\t", y,"\t", square_method,"\t" "diff:",diff,)
        a = a + 1









