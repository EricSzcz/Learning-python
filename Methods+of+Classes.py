
# coding: utf-8

# In[43]:


class Circle(object):
    
    #Class object attributes
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        
    def area(self):
        #radius**2 * pi
        return (self.radius**2) * Circle.pi
    
    def set_radius(self,new_radius):
        """
        This methods take in a radius and resets the current radius of the Circle
        """
        self.radius = new_radius
        
    def get_radius(self):
        return self.radius
    
    def perimeter(self):
        return (2**Circle.pi)*self.radius
        


# In[35]:


c = Circle(radius = 10)


# In[36]:


c.radius


# In[37]:


c.radius


# In[26]:


c.set_radius(20)


# In[27]:


c.radius


# In[32]:


c.get_radius()


# In[44]:


c = Circle(radius = 5)


# In[47]:


c.area()


# In[48]:


c.perimeter()


# In[42]:


c = Circle(circumference=5)

