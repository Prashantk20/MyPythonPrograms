#!/usr/bin/env python
# coding: utf-8

# In[7]:


import turtle
my_wn=turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Drawing Square")
my_pen=turtle.pen
my_pen.color("black")
def my_sqrfunc(size):
    for i in range(4):
        my_pen.fd(size)
        my_pen.left(90)
        size=size-5
my_sqrfunc(146)
my_sqrfunc(126)
my_sqrfunc(106)
my_sqrfunc(146)
my_sqrfunc(86)
my_sqrfunc(66)
my_sqrfunc(46)
my_sqrfunc(26)
del my_pen
turtle.Screen().bye()


# In[ ]:




