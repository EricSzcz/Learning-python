
# coding: utf-8

# In[1]:


l = []

for letter in 'word':
    l.append(letter)
print(l)


# In[2]:


l = [letter for letter in 'word']


# In[3]:


l


# In[4]:


lst = [letter for letter in 'word']


# In[5]:


lst


# x^2 for x in range(0,10)

# In[6]:


lst = [x**2 for x in range(0,11)]


# In[7]:


lst


# In[8]:


lst = [number for number in range(11) if number % 2 == 0]


# In[9]:


lst


# In[11]:


lst = []

for number in range(11):
    if number %2 == 0:
        lst.append(number)


# In[12]:


lst


# In[14]:


celsius = [0,10,20.1,34.5]

fahrenheit = [temp for temp in celsius]


# In[15]:


fahrenheit


# In[16]:


celsius = [0,10,20.1,34.5]

fahrenheit = [temp * (9/5.0) + 32 for temp in celsius]


# In[17]:


fahrenheit


# In[18]:


lst = [x**2 for x in range(11)]


# In[19]:


lst


# In[22]:


# Final result is x**4 for num in range(11)
lst = [x**2 for x in [x**2 for x in range(11)]]


# In[21]:


lst

