#!/usr/bin/env python
# coding: utf-8

# In[1]:


def drawPolygon(myTurtle,sideLength,n):
     angle = 360.0/n
     for i in range(n):
        myTurtle.forward(sideLength)
        myTurtle.right(angle)


# In[2]:


def drawSquare(myTurtle, sideLength) : 
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)


# In[3]:


def drawSpiral(myTurtle,maxSide) :
    for sideLength in range(0,maxSide+1,5) :
        myTurtle.forward(sideLength)
        myTurtle.right(90)


# In[4]:


def drawSquare(myTurtle, sideLength) : 
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)


# In[ ]:




