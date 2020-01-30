#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:41:11 2020

@author: mcubbage
Assignment 02 Building Complex Programs from smaller Parts 5.2

"""
#excercise 5.2 part 2
#create a function that check's fermat's theory

def check_fermat (a,b,c,n):
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    if n>2 and (a^n) +(b^n) ==(c^n):
        print('Holy, smokes, fermat was wrong!')
    else:
        print('No, that doesnt work')
        
#choose parameters for fermat's theory function
a= input("Choose number for a:")
b= input("Choose number for b:")
c= input("Choose number for c:")
n= input("Choose number for n:")

#use user input in the function that says if fermat's theory works
check_fermat(a,b,c,n)

