#!/usr/bin/env python
# coding: utf-8

# In[514]:


from pandas import *
xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/sample.xlsx')# synonyms for domains
df = xls.parse(xls.sheet_names[0])
print(df)


# In[515]:


from pandas import *
xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/sample1.xlsx') # sampe strings
df1 = xls.parse(xls.sheet_names[0])
print(df1)


# In[516]:


from pandas import *
xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/sample2.xlsx') #s
df2 = xls.parse(xls.sheet_names[0])
print(df2)


# In[517]:


from numpy import nan as Nan
import pandas as pd
#domains = pd.DataFrame()
#s2 = pd.Series([1,1])
#df1.append(s2, index=len(St))
#df1.loc[df.index.max()] = Nan
St = df1['String'].tolist()
print(St[0].split())
print(len(St))
print(df1)
#print(s2)

print(df1.index.max())
r, c = df1.shape
print(r)
li = df2.columns.tolist()
print(li)
a=St[3].split()
print(a)
#print(a[2][0])


# In[518]:



count2=0
for x in St:
    #print(x)
    count2=count2+1
    St1=x
    a=[]
    cc=[]
    aa, bb = np.where(df1.values == St1)
    count=0
    count1=0
    if count2<6:
        for y in St1.split():
            #print(y)
            s = (df == y).any()
            a.append(s.index[s])
            count1=count1+1
            #print(a[count1-1][0])
            if(a[count1-1]!= 0):
                b=str(a[count1-1][0])
                #print(b)
                #print(count1)
                count=count+1
                #print(a)
                #print(count)
                #print(df1)
                if(count<=1):
                    cc.append(a[count1-1][0])
                    df1.at[aa[count-1],bb[count-1]+1]= a[count1-1][0]
                    #print(df1)
                elif(count>1):
                    z=St1
                    #print(z)
                    cc.append(a[count1-1][0])
                    #print(f)
                    #print(df1)
                    r, c = df1.shape
                    #print(r)
                    St.append(St1)
                    df1.at[r,"String"] = St1
                    df1.at[r,1]= a[count1-1][0]
        if(count==0):
            df1.at[aa[count],bb[count]+1]="unknown"
            df1.at[aa[count],bb[count]+2]="unknown"
            #print(cc)
        #St2 = df1['String'].tolist()
    #print(St)    
    count4=0
    xx, yy = np.where(df1.values == St1)
    for xy in cc:
        for i in range(len(li)):
            if(xy == li[i]):
                sd=df2[xy].tolist()
                #print(x)
                for y in St1.split():
                    for j in range(len(sd)):
                        if(y==sd[j]):
                            count4=count4+1
                            if(count==1):
                                df1.at[aa[0],bb[0]+2]=sd[j]
                            elif(count>1):
                                for i in range(count):
                                    df1.at[xx[i],yy[i]+2]=sd[j]
                if(count4==0):
                    df1.at[aa[0],bb[0]+2]="unknown"
                            
                        
    #if(count>1):
     #   for i in range(count):
      #      print(St)
       #     St.pop()
df1.columns = ['String','domain', 'subdomain']        
print(df1)        
        #dd=[]
        #for i in range(len(bb)):
            #e[aa[i]]='Nan'
            #dataframe.iat[aa[i],bb[i]]='Nan'
            #dd.append(dataframe.iat[aa[i],bb[i]+1])  
            #print(j)
            #dd = dataframe.iat[0,1] 
            #print(dataframe)   
        #cc = dataframe.columns[bb[0]]
        #print(cc)
        #print(e.index(x))
        #c.at[aa[0],0]=x

          #if x!='Nan':
          #print(x)
          #s = (df == x).any()
          #a = s.index[s]
          #print(a)
            


# In[519]:


df1.to_csv(r'C:/Users/Krishna Asrith/Desktop/sample3.csv')


# In[438]:


abc=St[0]
class abc:
    a = 10
print(abc.a) 


# In[252]:


a="Assignment"
b="Assignment"
if(a==b):
    


# In[293]:


li=[]
a=[1,2,3]
b=[2,1,3]
li =  sorted(set(a)-set(b))
li1= sorted(set(a)-set(li))
print(li1)


# In[421]:


print(St)
xx,yy= np.where(df1.values == St[0])
print(xx[1])
print(yy[1])


# In[ ]:




