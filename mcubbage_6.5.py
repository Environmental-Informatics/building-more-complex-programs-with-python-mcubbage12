#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:12:40 2020
Assignment 02 Building Complex Programs from smaller Parts exercise 6.5
@author: mcubbage
"""
#define a function that finds the greatest common denomiator of 2 numbers
 def gcd(a,b):
     if b==0:
         return a
     r=a%b
     return gcd(b,r)
 
#test function gcd using 2 numbers
gcd(420,160)


