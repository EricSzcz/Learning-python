
# coding: utf-8

# In[1]:


x = 0

while x < 10:
    print('x is currently:',x)
    x += 1


# In[5]:


x= 0

while x < 10:
    print('x is currently:',x)
    x += 1
else:
    print('All done!')


# In[6]:


# break continue and pass


# In[7]:


x = 0

while x < 10:
    print('x is currently:',x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    
    if x== 3:
        print('Hey x equals 3')
    else:
        print('continuing...')
        continue


# In[8]:


x = 0

while x < 10:
    print('x is currently:',x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    
    if x== 3:
        print('Hey x equals 3!')
        break
    else:
        print('continuing...')
        continue

