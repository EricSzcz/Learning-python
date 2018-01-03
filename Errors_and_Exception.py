
# coding: utf-8

# In[1]:


2 + 's'


# In[6]:


try:
    2 + 's'
except:
    print('There was a type error!')
finally:
    print('Finally this was printed')


# In[9]:


try:
    f = open('testfile123','w')
    f.write('Test write this')
except:
    print('Error in writing to the file!')
else:
    print('File was a sucess')


# In[10]:


try:
    f = open('testfile123','r')
    f.write('Test write this')
except:
    print('Error in writing to the file!')
else:
    print('File was a sucess')


# In[12]:


try:
    f = open('testfile123','r')
    f.write('Test write this')
except:
    print('There was an error!')
finally:
    print('Always execute finally code blocks!')


# In[16]:


def askint():
    try:
        val = int(input('Please enter an integer: '))
    except:
        print('Looks like you did not enter an integer!')
        val = int(input('Try again - please enter an integer! '))
    finally:
        print('Finally block executed!')
    print(val)


# In[14]:


askint()


# In[18]:


askint()


# In[20]:


def askint():
    while True:
        try:
            val = int(input('Please enter an integer: '))
        except:
            print("Looks like you didn't enter an integer: ")
            continue
        else:
            print('Correct, that is an integer!')
            break
        finally:
            print('Finally block executed')
        print(val)


# In[21]:


askint()

