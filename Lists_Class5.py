
# coding: utf-8

# In[1]:


my_list = [1,2,3]


# In[2]:


my_list


# In[3]:


my_list =['string',23,1.3,'o']


# In[4]:


my_list


# In[5]:


len(my_list)


# In[6]:


my_list = ['one','two','three',4,5]


# In[7]:


my_list[0]


# In[8]:


my_list[1:]


# In[9]:


my_list[:3]


# In[10]:


'hello' + 'world'


# In[11]:


my_list


# In[12]:


my_list + ['new item']


# In[13]:


my_list


# In[16]:


my_list = my_list + ['permanent add']


# In[17]:


my_list


# In[18]:


my_list * 2


# In[19]:


l = [1,2,3]


# In[20]:


l


# In[21]:


l.append('append me!')


# In[22]:


l


# In[24]:


l.pop()


# In[25]:


x = l.pop(0)


# In[26]:


x


# In[27]:


l


# In[29]:


l[1]


# In[30]:


new_list = ['a','e','x','b','c']


# In[31]:


new_list


# In[33]:


new_list.reverse()


# In[34]:


new_list


# In[35]:


new_list.sort()


# In[36]:


new_list


# In[37]:


l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]


# In[38]:


matrix = [l_1,l_2,l_3]


# In[39]:


matrix


# In[40]:


matrix[0]


# In[41]:


matrix[0][2]


# In[42]:


matrix[1][1]


# In[43]:


matrix[2][0]


# In[44]:


first_col = [row[0] for row in matrix]


# In[45]:


first_col

