#!/usr/bin/env python
# coding: utf-8

# In[24]:


from pandas import *
xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/project analysis and design SIT764/Domains-and-subdomains.xlsx')# synonyms for domains
df = xls.parse(xls.sheet_names[0])
dm=df.iloc[:,[0,7,12,18,24]]
sd1=df.iloc[:,1:7]
sd2=df.iloc[:,8:12]
sd3=df.iloc[:,13:18]
sd4=df.iloc[:,19:24]
sd5=df.iloc[:,25:31]
sd=[sd1,sd2,sd3,sd4,sd5]


# In[25]:


xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/project analysis and design SIT764/Spero-a-master/Spero-a Front-End/De-identified student comments.xlsx') # sampe strings
df1 = xls.parse(xls.sheet_names[2])
print(df1)


# In[26]:


from numpy import nan as Nan
import pandas as pd
import re
St = df1['IMPROVE'].tolist()
li = dm.columns.tolist()
for x in St:
    St1=x
    a=[]
    cc=[]
    aa, bb = np.where(df1.values == St1)
    cou=0
    tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', St1.lower())]
    for y in tokens:
        cou=cou+1
        if(y=="," or y== "." or y== "!" or y== "?" or y== ";"):
            cou=cou-1
        else:    
            s = (dm == y).any()
            p=s.index[s]
            if(p.any()!=0):
                if(len(p)>1):
                    for i in p:
                        a.append(str(i))
                else:
                    a.append(str(p[0]))    
    a=np.unique(a)    
    if(len(a) != 0):
        df1.at[aa[0],bb[0]+1]= a[0]
        for i in range(len(a)-1):
            r1, c1 = df1.shape
            df1.at[r1,"IMPROVE"] = St1
            df1.at[r1,1]= a[i+1]
    else:
        df1.at[aa[0],bb[0]+1]= "unkonwn"
        df1.at[aa[0],bb[0]+2]= "unkonwn"
df1 = df1.sort_values('IMPROVE')
df1 = df1.reset_index(drop=True)
print(df1)
r, c = df1.shape
for i in range(r):
    countf=-1
    for xy in li:
        countf=countf+1
        if(df1.iat[i,1]==xy):
                tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', df1.iat[i,0].lower())]
                b=[]
                for y in tokens:
                    cou=cou+1
                    if(y=="," or y== "." or y== "!" or y== "?" or y== ";"):
                        cou=cou-1
                    else:  
                        s = (sd[countf] == y).any()
                        p=s.index[s]
                        if(p.any()!=0):
                            if(len(p)>1):
                                for k in p:
                                    b.append(str(k))
                            else:
                                b.append(str(p[0]))
                b=np.unique(b)    
                if(len(b) != 0):
                    df1.at[i,2]= b[0]
                    for j in range(len(b)-1):
                        r1, c1 = df1.shape
                        df1.at[r1,"IMPROVE"] = df1.iat[i,0]
                        df1.at[r1,1]= df1.iat[i,1]
                        df1.at[r1,2]= b[j+1]
                else:
                    df1.at[i,2]="unkonwn"
        
            
df1 = df1.sort_values('IMPROVE')
df1 = df1.reset_index(drop=True)
print(df1)  


# In[20]:


df1.to_csv(r'C:/Users/Krishna Asrith/Desktop/sample3.csv')


# In[ ]:




