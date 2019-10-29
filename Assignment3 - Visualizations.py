#!/usr/bin/env python
# coding: utf-8

# In[2]:


#All imports needed for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import mpld3

#mpld3.enable_notebook()


# In[3]:


fileName = '/Users/Devon/Desktop/SchoolStuff/uAlbany/Senior/Spring 2019/INF428/Assignments/Assignment3/Drinking_Water_Quality_Distribution_Monitoring_Data.csv'
waterData = pd.read_csv(fileName, encoding="ISO-8859-1")
#Fix Messy Columns
waterData.columns = waterData.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
waterData.head()
waterData.columns


# In[4]:


#Change year function
def changeYear(value):
    if "15" in value:
        value = "2015"
    elif "16" in value:
        value = "2016"
    elif "17" in value:
        value = "2017"
    elif "18" in value:
        value = "2018"
    elif "19" in value:
        value = "2019"
    return value

#Creates newYear column
waterData['newYear']=waterData['sample_date'].map(changeYear)


# In[5]:


#Fixes NaN column values
waterData['newTurbidity']=pd.to_numeric(waterData['turbidity'], errors='coerce').fillna(0)
waterData['newFluoride']=pd.to_numeric(waterData['fluoride'], errors='coerce').fillna(0)
waterData['newColiform']=pd.to_numeric(waterData['coliform'], errors='coerce').fillna(0)
waterData['newE_coli']=pd.to_numeric(waterData['e_coli'], errors='coerce').fillna(0)

#waterData['newTurbidity'].head()
#waterData['newFluoride'].head()
#waterData['newColiform'].head()
#waterData['newE_coli'].head()


# In[6]:


#Create empty figures to save all plots for the website
#fig1=plt.figure()
#fig2=plt.figure()
#fig3=plt.figure()
#fig4=plt.figure()
#fig5=plt.figure()
#fig6=plt.figure()
#fig7=plt.figure()
#fig8=plt.figure()
#fig9=plt.figure()
#fig10=plt.figure()


# In[11]:


#FIRST VISUALIZATION

#fig1=plt.figure()

#Groups data by the 'Sample class' column
classes = waterData.groupby('sample_class')
#Controls the explode attributes for the pie chart
explode = [0.1,0.3,0.05,0.5,2.3,3.7]

get_ipython().run_line_magic('matplotlib', 'inline')
#Creates pie chart representing the # of samples contained in each sample class
classes['sample_number'].count().plot.pie(shadow=True, explode = explode , autopct = '%1.3f%%')

plt.title('Percentage of Samples in Each Sample Class')
plt.xlabel('')
plt.ylabel('')
plt.show()

#mpld3.save_html(fig1,'simple.html')


# In[8]:


import os
os.getcwd()


# In[10]:


#SECOND VISUALIZATION

#fig2 = plt.figure()

#Create Bar Graph for average amounts of Residual Chlorine in each year

years=waterData.groupby('newYear')
means=years.mean()
means['residual_free_chlorine'].plot.bar()

plt.title('Average Amount of Residual Free Chlorine from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Residual Free Chlorine (mg/L)')

#mpld3.save_html(fig1,'simple2.html')

plt.show()


# In[23]:


#THIRD VISUALIZATION

x = waterData.residual_free_chlorine
y = waterData.newTurbidity
z = np.array(waterData.newFluoride)

plt.scatter(x,y,s=z*10)

plt.title('Bubble Chart using Chlorine, Turbidity and Flouride')
plt.xlabel('Residual Free Chlorine (mg/L)')
plt.ylabel('Turbidity (NTU)')
plt.show()


# In[13]:


#FOURTH VISUALIZATION

a = np.array(waterData.newYear)
a = np.sort(a)

chlorine = np.array(waterData.residual_free_chlorine)
#testing
#chlorine = np.array(waterData.newTurbidity)
#chlorine = np.array(waterData.newFluoride)
#chlorine = np.array(waterData.newColiform)
#chlorine = np.array(waterData.newE_coli)

plt.plot(a,chlorine)

plt.title('Chlorine Values from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Residual Free Chlorine (mg/L)')
plt.show()

#there's supposed to be a drop in 2017 (-9.99)


# In[14]:


#FIFTH VISUALIZATION
#Controls the explode attributes for the pie chart
explode = [0.1,0.05,0.05,0.05,0.3]

get_ipython().run_line_magic('matplotlib', 'inline')
#Creates pie chart representing the # of samples contained in each sample class
years['newYear'].count().plot.pie(shadow=True, explode = explode , autopct = '%1.3f%%')

plt.title('Percentage of Data from Each Year')
plt.xlabel('')
plt.ylabel('')
plt.show()


# In[15]:


#SIXTH VISUALIZATION
means['newTurbidity'].plot.bar()

plt.title('Average Amount of Turbidity from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Turbidity (NTU)')
plt.show()


# In[16]:


#SEVENTH VISUALIZATION
means['newFluoride'].plot.bar()

plt.title('Average Amount of Fluoride from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Fluoride (mg/L)')
plt.show()


# In[17]:


#EIGHT VISUALIZATION
means['newColiform'].plot.bar()

plt.title('Average Amount of Coliform from 2015-2019')
plt.xlabel('Year')
plt.ylabel('Coliform (Quanti-Tray) (MPN/100mL)')
plt.show()


# In[18]:


#NINTH VISUALIZATION
means['newE_coli'].plot.bar()

plt.title('Average Amount of E-Coli from 2015-2019')
plt.xlabel('Year')
plt.ylabel('E-coli (Quanti-Tray) (MPN/100mL)')
plt.show()


# In[19]:


#TENTH VISUALIZATION
a = waterData.newColiform
b = waterData.newE_coli

plt.scatter(a,b)

plt.title('Scatter Chart using Coliform and E-coli')
plt.xlabel('Coliform (Quanti-Tray) (MPN/100mL)')
plt.ylabel('E-coli (Quanti-Tray) (MPN/100mL)')
plt.show()


# In[ ]:




