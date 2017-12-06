
# coding: utf-8

# In[ ]:


#def = define


# In[1]:


def name_of_function():
    pass


# In[2]:


name_of_function()


# In[3]:


def name_of_function(arg1,arg2):
    
    pass


# In[4]:


name_of_function(1,2)


# In[5]:


def my_addition_func(arg1,arg2):
    print(arg1+arg2)
    pass


# In[6]:


my_addition_func(1,2)


# In[7]:


def my_addition_func(arg1,arg2):
    """
    here is my docstring
    """
    print(arg1+arg2)
    pass


# In[8]:


def say_hello():
    print('Hello')


# In[9]:


say_hello()


# In[10]:


def greeting(name):
    print('Hello '+name)


# In[11]:


greeting('Eric')


# In[12]:


def add_num(num1,num2):
    return num1+num2


# In[13]:


x = add_num(2,3)


# In[14]:


x


# In[15]:


print(add_num('one','two'))


# In[18]:


x = add_num('one','two')


# In[19]:


x


# In[20]:


def is_prime():
    pass


# In[21]:


is_prime()


# In[22]:


def is_prime(num):
    pass


# In[24]:


is_prime(2)


# In[26]:


def is_prime(num):
    """
    This function checks for prime numbers
    INPUT: A number
    OUTPUT: A print statement whether or not the number is prime
    """
    for n in range(2, num):
        if num % n == 0:
            print('Not Prime')
            break
    else:
        print('The number is prime')
    pass


# In[28]:


is_prime(12)

