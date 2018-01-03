
# coding: utf-8

# In[16]:


class Animal(object):
    def __init__(self):
        print('Animal Created')
        
    def whoAmI(self):
        print('Animal')
        
    def eat(self):
        print('Eating')


# In[17]:


a = Animal()


# In[22]:


class Dog(Animal):    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
        
    def whoAmI(self):
        print('Dog')
    
    def bark(self):
        print('woof!')    
    


# In[23]:


d = Dog()


# In[14]:


d = Dog


# In[24]:


d.whoAmI()


# In[25]:


d.eat()


# In[26]:


d.bark()

