
# coding: utf-8

# In[3]:


def vol(rad):
    rad = rad / 3.14
    rad = rad / 2
    print(rad)
    pass


# In[4]:


vol(31.40)


# In[64]:


def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.isupper():
            up += 1
        else:
            low += 1
    print('No. of Upper case characters : '+str(up))
    print('No. of Lower case characters : '+str(low))
    pass


# In[62]:


s = 'hi '


# In[63]:


up_low(s)


# In[11]:


s[0].isupper()

