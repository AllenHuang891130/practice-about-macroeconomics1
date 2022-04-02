#!/usr/bin/env python
# coding: utf-8

# In[55]:


import csv
import locale
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件
plt.style.use("ggplot")
a = []
b = []
currency = []
m1 = []
m2 = []
year = [] 
year1 = []
year2 = []
with open('FM0501A1Ac.csv', encoding='big5' , errors = 'ignore') as a1:
    rows = csv.reader(a1, delimiter=',')
    a += rows
with open('gdp.csv', encoding='big5' , errors = 'ignore') as b1:
    rows = csv.reader(b1, delimiter=',')
    b += rows
for i in range(5,30):
    currency.append(int(a[i][31])/int(b[i-1][1]))
    m1.append(int(a[i][31])+int(a[i][55])+int(a[i][57])/int(b[i-1][1]))
    m2.append(int(a[i][59])/int(b[i-1][1]))
for j in range(1997,2022):
    year.append(j)
    year1.append(j)
    year2.append(j)
#plt.plot(year, currency , c = "r") 
#plt.plot(year1, m1 ,  "g") 
plt.plot(year2, m2 ,  "b")
#plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




