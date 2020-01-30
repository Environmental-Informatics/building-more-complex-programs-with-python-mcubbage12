#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:58:24 2020
Assignment 02 Building Complex Programs from smaller Parts exercise 4.2

@author: mcubbage
"""

#import turtle
import turtle

#name the pointer in the turtle window bob
bob= turtle.Turtle()

#define function that draws one petal of a flower
def petal():
    bob.fd(50)    
    bob.rt(45)
    bob.fd(50)
    bob.rt(135)
    bob.fd(50)
    bob.rt(45)
    bob.fd(50)
    
#define function that draws a flower with 8 petals 
#this does not look exactly like figure 1 in the book, but I do not know how to get the arches
def flower ():
    for i in range(8):
        petal()
    
#draw a 8 petal flower
flower()


##################

#this is the code from the answer key in the book. However, there is an error when I run it saying that modeule polygon does not exist
import turtle

from polygon import arc


def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()