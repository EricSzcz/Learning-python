
# coding: utf-8

# In[3]:


def vol(rad):
    rad = rad / 3.14
    rad = rad / 2
    print(rad)
    pass


# In[4]:


vol(31.40)


# In[21]:


def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.isupper():
            up += 1
        else:
            low += 1
    print('No. of Upper case characters : %s'%(up))
    print('No. of Lower case characters : %s'%(low))
    pass


# In[22]:


s = 'hi '


# In[23]:


up_low(s)


# In[11]:


s[0].isupper()


# In[16]:


def unique_list(l):
    x = set(l)
    print(x)    
    pass


# In[19]:


t = [1,1,1,1,2,2,3,3,3,3,4,5]


# In[20]:


unique_list(t)


# In[36]:


def multiply(numbers):
    result = 1
    for num in numbers:
        result = num*result
    print(result)
    pass


# In[25]:


numbers = [1,2,3,-4]


# In[37]:


multiply(numbers)


# In[41]:


def palindrome(s):
    x = s
    s = s[::-1]
    if x == s:
        return True
    else:
        return False
    pass


# In[42]:


palindrome('ana')


# In[43]:


palindrome('carro')


# In[94]:


'test e'.rstrip(' ')


# In[65]:


l = []

for letter in t:
    l.append(letter)


# In[118]:


t = ' te st'
t = t.replace(" ","")
t


# In[159]:


import string


# In[170]:


def ispangram(str, alphabet=string.ascii_lowercase):
    str = str.lower()
    str = str.replace(" ","")
    str = set(str)
    str = sorted(str)
    alphabet = sorted(alphabet)
    if str == alphabet:
        return True
    else:
        return False
    pass


# In[171]:


ispangram('The quick brown fox jumps over the lazy dog','abcdefghijklmnopqrstuvwxyz')


# In[123]:


x = []
for letter in t:
    x.append(letter)
    


# In[133]:


x = 'cbda'


# In[134]:


x = sorted(x)


# In[135]:


x


# In[136]:


y = 'abcd'


# In[137]:


x == y


# In[138]:


y


# In[139]:


y = sorted(y)


# In[140]:


y


# In[141]:


x == y

