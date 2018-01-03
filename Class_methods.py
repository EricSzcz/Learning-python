
# coding: utf-8

# In[30]:


class Line(object):
    def __init__(self,coor1,coor2):
        import math
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 +(y2-y1)**2 )**0.5
         
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1))/(x2-x1)


# In[31]:


coordinate1 = (3,2)
coordinate2 = (8,10)


# In[32]:


li = Line(coordinate1,coordinate2)


# In[33]:


li.distance()


# In[35]:


li.slope()


# In[36]:


class Cylinder(object):
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * (3.14) * (self.radius)**2
    def surface_area(self):
        top = (3.14)*(self.radius)**2
        return 2*top + 2*3.14*self.radius*self.height


# In[37]:


c = Cylinder(2,3)


# In[38]:


c.volume()


# In[39]:


c.surface_area()

