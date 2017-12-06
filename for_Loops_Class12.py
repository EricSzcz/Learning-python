
# coding: utf-8

# In[1]:


l = [1,2,3,4,5]


# In[2]:


l


# In[3]:


for element in l:
    print(element)


# In[4]:


for num in l:
    print(num)


# In[5]:


for num in l:
    print('something!')


# In[6]:


# MODULO


# In[7]:


10 % 3


# In[8]:


18 % 7


# In[9]:


4 % 2


# In[10]:


l


# In[11]:


for num in l:
    if num % 2 == 0:
        print(num)


# In[12]:


for num in l:
    if num % 2 == 1:
        print(num)


# In[13]:


for num in l:
    if num % 2 == 0:
        print('Here is an even')
    else:
        print('Odd number!')


# In[14]:


l


# In[16]:


list_sum = 0

for num in l:
    list_sum = list_sum + num
    
print (list_sum)


# In[17]:


list_sum = 0

for num in l:
    list_sum += num
    
print (list_sum)


# In[18]:


s = 'this is a string!'


# In[19]:


for item in s:
    print(item)


# In[20]:


for letter in s:
    print(letter)


# In[21]:


tup = (1,2,3,4,5)

for t in tup:
    print(t)


# In[22]:


for item in tup:
    print(item)


# In[23]:


l = [(2,4),(6,8),(10,12)]


# In[24]:


l


# In[25]:


l[0]


# In[26]:


l[0][1]


# In[27]:


l[2][0]


# In[29]:


for tup in l:
    print(tup)


# In[30]:


for (t1,t2) in l:
    print(t1)


# In[31]:


for (t1,t2) in l:
    print(t1)
    print(t2)


# In[32]:


for (t1,t2) in l:
    print(t1+t2)


# In[33]:


d = {'k1':1,'k2':2,'k3':3}


# In[34]:


for item in d:
    print(item)


# In[35]:


for k,v in d.items():
    print(k)
    print(v)
    


# In[36]:


for k in d.items():
    print(k)
    


# In[37]:


for v in d.items():
    print(v)

