
# coding: utf-8

# In[1]:


l = [1,2,3]


# In[3]:


l.count(2)


# In[4]:


#Objects


# In[5]:


type(1)


# In[6]:


type([1,2,3])


# In[7]:


type((1,2,3))


# In[8]:


type({'k1':1})


# In[9]:


def square(num):
    return num**2


# In[10]:


type(square)


# In[11]:


class Sample(object):
    pass


# In[12]:


x = Sample()


# In[13]:


type(x)


# In[28]:


class Dog(object):
    #Class Object attribute
    species = 'mammal'
    
    def __init__(self,breed,name,fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


# In[29]:


sam = Dog(breed='Lab',name = 'Sammy', fur=True)


# In[27]:


sam.name


# In[18]:


sam = Dog(breed='Huskie')


# In[20]:


sam.breed


# In[23]:


sam.species


# In[30]:


sam.fur

