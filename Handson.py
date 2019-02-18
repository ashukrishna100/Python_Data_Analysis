#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


##reading the data
df = pd.read_csv('train_loanPrediction.csv')


# In[5]:


##quick data exploration
df.head(5)


# In[6]:


##summary of numerical variables
df.describe()


# In[7]:


df.count(axis=0)


# In[8]:


## so the total number of rows=614(in Loan_ID,Education,ApplicantIncome,CoapplicantIncome,Property_Area,Loan_Status)
## we have missing values in (Gender,Married,Depedents,Self_Employed,LoanAmount,Loan_Amount_Term,Credit_History)


# In[9]:


print(df['Property_Area'].value_counts())
print(df['Gender'].value_counts())


# In[10]:


##distribution analysis
df['ApplicantIncome'].hist(bins=50)


# In[11]:


df.boxplot(column='ApplicantIncome', by = 'Gender')


# In[78]:


df.plot.box(grid='True')


# In[12]:


## categorical variable analysis(like Gender,Education)
## distribution of loan status vs Education,Marrried,credit history
t1 = pd.crosstab(df['Education'],df['Loan_Status'])
t1.plot(kind='bar', stacked='True', color=['red','blue'], grid=False)


# In[13]:


## Data Preparation
#Handling Missing Data


# In[14]:


##count missing data in each column
df.apply(lambda x: sum(x.isnull()),axis=0)


# In[15]:


##fill in missing data
df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace= True)


# In[16]:


#check whether missing data has been filled
print(df['LoanAmount'].count())


# In[17]:


df['LoanAmount'].median()


# In[80]:


##Data wrangling-merging,grouping,concatenating
df.groupby('ApplicantIncome').mean()[:5]


# In[81]:


df.groupby('Married').get_group('Yes')[:5]


# In[20]:


##Statistical Analysis


# In[21]:


##calculate mean,median,mode for Applicant Income
print("mean is: ",df['ApplicantIncome'].mean())
print("median is: ",df['ApplicantIncome'].median())
print("mode is: ",df['ApplicantIncome'].mode())


# In[22]:


##calculate standard deviation,skewness and variance for Applicant Income
print("standard deviation is: ",df['ApplicantIncome'].std())
print("variance is: ",df['ApplicantIncome'].var())
print("skewness is: ",df['ApplicantIncome'].skew())


# In[43]:


##Normal distribution
df['ApplicantIncome'].hist(bins=50)


# In[44]:


#calculate mean,mu
x=df['ApplicantIncome']
bins=50
mu=df['ApplicantIncome'].mean()
print("mean is ",mu)
#calculate standard deviation
sigma=df['ApplicantIncome'].std()
print("standard deviation is :",sigma)


# In[46]:


#plot
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()


# In[53]:


##p-value(here less than 0.05)
stats.ttest_ind(df['ApplicantIncome'],df['CoapplicantIncome'])


# In[83]:


##correlation
df.corr()


# In[58]:


##chi-square test
print(stats.chisquare(df['Education'].value_counts()))
print(stats.chisquare(df['Loan_Status'].value_counts()))


# In[88]:


cont = pd.crosstab(df['Education'],df['Loan_Status'])
stats.chi2_contingency(cont)


# In[60]:


df['Education'].value_counts()


# In[65]:


from sklearn.linear_model import LinearRegression


# In[71]:


#Linear regression
X = np.array(df['ApplicantIncome']).reshape(-1,1)
Y = np.array(df['CoapplicantIncome']).reshape(-1,1)
linear_regressor=LinearRegression()
linear_regressor.fit(X,Y)
Y_pred = linear_regressor.predict(X)
print(Y_pred[:5])


# In[74]:


plt.scatter(X,Y)
plt.plot(X,Y_pred,color='red')
plt.show()


# In[ ]:





# In[ ]:




