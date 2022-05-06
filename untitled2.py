# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:02:38 2022

@author: acer
"""
#Ninzalar qurli
import turtle as t
import colorsys
t.width(3)
t.tracer(10)
t.bgcolor("black")
h=0
n=50
for i in range(150):
    c=colorsys.hsv_to_rgb(h, 1, 0.8)
    h+=1/n
    t.pencolor(c)
    t.circle(i,99)
    t.forward(i)
    t.right(370)
    t.forward(i)
    t.right(180)
t.done()    