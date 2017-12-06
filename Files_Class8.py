
# coding: utf-8

# In[1]:


pwd


# In[2]:


f = open('test.txt')


# In[3]:


f.read()


# In[4]:


f.read()


# In[5]:


f.seek(0)


# In[6]:


f.read()


# In[8]:


f.seek(0)


# In[9]:


f.readlines()


# In[10]:


get_ipython().run_cell_magic('writefile', 'new.txt', 'First line\nSecond line')


# In[12]:


for line in open('new.txt'):
    print(line)


# In[13]:


for words in open('new.txt'):
    print(line)

