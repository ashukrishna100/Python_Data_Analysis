
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


## determine size and shape of an array
array1=np.array([(2,3,4,5),(1,0,3,6)])
print(array1.size)
print(array1.shape)


# In[3]:


## Reshape an array
array1=np.array([(2,3,4,5),(1,0,3,6)])
print(array1.reshape(4,2))


# In[4]:


## Datatype
print(array1.dtype)
##change datatype
float_array1=array1.astype(np.float64)
print(float_array1)
print(float_array1.dtype)


# In[5]:


##indexing and slicing
array2=np.arange(10)
print(array2)
print(array2[5])
print(array2[3:5])


# In[6]:


##change elements of 1-D array
array2[5]=100
print(array2)


# In[7]:


## slicing
array2_slice=array2[:6]
print(array2_slice)


# In[8]:


## 2-D array,  array1=[[2, 3, 4, 5],[1, 0, 3, 6]]
print(array1[1])
print(array1[1,3])


# In[9]:


##slicing in 2-d array
print(array1[:2,3:])
print(array1[:2,3])


# In[10]:


##transposing and dot product
array3=np.arange(10).reshape(5,2)   ##5*2=10,5*2 matrix/array
print(array3)


# In[11]:


print(array3.T)
## becomes 2*5 matrix/array


# In[12]:


##dot product
print(np.dot(array3.T,array3))


# In[13]:


## Universal functions ; array2=[  0   1   2   3   4 100   6   7   8   9]
print(array2.sum())
print(array2.max())
print(array2.std())
print(array2.var())
print(np.median(array2))
print(np.sqrt(array2))


# In[21]:


##conditional logic on Array operations
array4=np.random.randn(2,3)
print(array4)
print(array4>0)
print(np.where(array4 > 0, 2, -2))


# In[39]:


## operations of rows and columns ,axis
print(array3)
print(array3.sum(axis=0))
print(array3.sum(axis=1))
print(array3.sum(axis=None))


# In[48]:


##concatenate arrays
array5=np.random.randn(2,4)
print(np.concatenate((array1, array5)))


# In[73]:


##sorting
#print(array5)
array5.sort(1)
print(array5)


# In[71]:


##unique and sets
names = np.array(['Chandu','Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))
print(sorted(set(names)))


# In[83]:


## identity matrix
print(np.identity(2))
print(np.eye(2,4,k=2))

