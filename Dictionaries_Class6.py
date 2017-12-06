
# coding: utf-8

# In[1]:


l = [1,2,3]


# In[2]:


l[0]


# In[3]:


my_dict = {'key1':'value','key2':'value2'}


# In[4]:


my_dict['key1']


# In[9]:


my_dict = {'k1':123,'k2':3.4,'k3':'string'}


# In[6]:


my_dict['k3']


# In[7]:


my_dict['k3'].upper()


# In[10]:


my_dict['k1']


# In[11]:


my_dict['k1'] - 120


# In[12]:


my_dict['k1']


# In[13]:


my_dict['k1'] = my_dict['k1'] - 120


# In[14]:


my_dict['k1']


# In[15]:


my_dict


# In[16]:


my_dict['k1']


# In[17]:


my_dict['k1'] = my_dict['k1'] + 100


# In[18]:


my_dict['k1']


# In[19]:


my_dict['k1'] += 100


# In[20]:


my_dict['k1']


# In[21]:


d = {}


# In[22]:


d


# In[23]:


d['animal'] = 'Dog'


# In[24]:


d['answer'] = 42


# In[27]:


d


# In[26]:


d


# In[28]:


d = {'k1':{'nestkey':{'subnestkey':'value'}}}


# In[29]:


d['k1']


# In[30]:


d['k1']['nestkey']


# In[31]:


d['k1']['nestkey']['subnestkey']


# In[32]:


d['k1']['nestkey']['subnestkey'].upper()


# In[33]:


d = {}


# In[34]:


d['k1'] = 1


# In[35]:


d['k2'] = 2


# In[36]:


d['k3'] = 3


# In[37]:


d


# In[38]:


d.keys()


# In[39]:


d.values()


# In[41]:


d.items()

