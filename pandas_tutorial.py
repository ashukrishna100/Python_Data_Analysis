
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np


# In[24]:


from pandas import Series, DataFrame


# In[4]:


##pandas series representation
obj = pd.Series([4, 7, -5, 3])
print(obj)


# In[7]:


##fetch value and index of pandas series
print(obj.values)
print(obj.index)
print(obj[2])


# In[11]:


##assign custom index to a series
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2['a'])


# In[18]:


##filtering and maths operations
print(obj2[obj2<0])
print(obj2**2)


# In[23]:


## make a series from dictionary
data1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(data1)
print(obj3)
'Ohio' in obj3


# In[25]:


##is null and not null
pd.notnull(obj3)


# In[29]:


##override the index
state=['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(data1, index=state)
print(obj4)
##replace the index
obj3.index=state
obj3


# In[28]:


##combination of series
print(obj3+obj4)


# In[32]:


##naming the series and index
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)


# In[36]:


##dataframe from dictionary
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
df1 = pd.DataFrame(data)
print(df1)


# In[42]:


##head method
print(df1.head(2))
print(df1.tail(2))


# In[70]:


##select some particular columns
df2=pd.DataFrame(data, columns=['year','pop'])
print(df2)


# In[71]:


##Dataframe functions
print(df2.columns)
print(df2['year'])
#print(df2.year)
print("#######") ##to selct rows
print(df2.loc[2])


# In[72]:


##del the columns and get the values
del df2['pop']
print(df2.columns)
print(df1.values)


# In[4]:


##some pandas functionalities

##reindexing
ser1 = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
ser_new = ser1.reindex(['a', 'b', 'c', 'd', 'e'])
print(ser_new)


# In[4]:


##arithematic operations on dataframes
dframe1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),index=['Ohio', 'Texas', 'Colorado'])
print(dframe1)
dframe2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(dframe2)
print(dframe1+dframe2)  ##union
print(dframe1-dframe2)  ## simple substraction


# In[18]:


print(dframe1)
## apply user defined functions on dataframe
f = lambda x: x.max() - x.min()
print(dframe1.apply(f))
print('######################')
print(dframe1.apply(f,axis='columns'))


# In[32]:


## sorting
print(dframe1)
print(dframe1.sort_index())
print(dframe1.sort_index(axis=1))
print('#############')
print(dframe1.sort_values(by=['d','b','c']))


# In[10]:


##remove row and columns
print(dframe1)
print(dframe1.drop('b',axis=1))   ##removes 'b' columns
print(dframe1.drop('Ohio',axis=0))  ##removes 'Ohio' row


# In[22]:


##condition,reset and set index
dframe3 = pd.DataFrame(np.random.randn(4, 3), index=list('abcd'),columns=list('wxy'))
print(dframe3[dframe3['w']>0])
print(dframe3.reset_index())
##set new column as index
dframe3['ID']=['AS1','AS2','AS3','AS4']   ##create a new column ID
print(dframe3)
print(dframe3.set_index('ID'))  ##set index as id


# In[33]:


##Missing Data (dropna() and fillna()),groupby,count,describe
dt = {'a':[1,np.nan,3],'b':[10,np.nan,2],'c':[0,5,2]}
dt = pd.DataFrame(dt)
dt


# In[30]:


dt.dropna()


# In[31]:


dt.dropna(axis=1)


# In[36]:


print(dt.fillna('100'))
#fill with mean value
dt['a'].fillna(dt['a'].mean())


# In[46]:


##count,describe,groupby
print(dt.count())
print(dt.describe())


# In[48]:


##correlation
dt.corr()


# In[49]:


##covariance
dt.cov()

