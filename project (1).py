import pandas as pd
from pandas import *
from numpy import nan as Nan
import pandas as pd
import re
from textblob import TextBlob
import xlrd


def getdictionary(url):
    xls = ExcelFile(url)  # synonyms for domains
    #xls = ExcelFile('C:/Users/Krishna Asrith/Desktop/project analysis and design SIT764/Domains-and-subdomains.xlsx')
    df = xls.parse(xls.sheet_names[0])
    dm = df.iloc[:, [0, 7, 12, 18, 24]]
    sd1 = df.iloc[:, 1:7]
    sd2 = df.iloc[:, 8:12]
    sd3 = df.iloc[:, 13:18]
    sd4 = df.iloc[:, 19:24]
    sd5 = df.iloc[:, 25:31]
    sd = [sd1, sd2, sd3, sd4, sd5]
    # print(dm)
    return sd, dm


def getreviews(url1):
    #df1 = pd.read_csv(url1)  # sampe strings
    df1 = xls.parse(xls.sheet_names[0])
    print(df1)
    return df1


def dandsd(df1, dm, sd):
    St = df1['IMPROVE'].tolist()
    li = dm.columns.tolist()
    for x in St:
        St1 = x
        a = []
        cc = []
        aa, bb = np.where(df1.values == St1)
        cou = 0
        tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', St1.lower())]
        for y in tokens:
            cou = cou + 1
            if (y == "," or y == "." or y == "!" or y == "?" or y == ";"):
                cou = cou - 1
            else:
                s = (dm == y).any()
                p = s.index[s]
                if (p.any() != 0):
                    if (len(p) > 1):
                        for i in p:
                            a.append(str(i))
                    else:
                        a.append(str(p[0]))
        a = np.unique(a)
        r, c = df1.shape
        if (len(a) != 0):
            df1.at[aa[0], bb[0] + 1] = a[0]
            for i in range(len(a) - 1):
                r1, c1 = df1.shape
                df1.at[r1, "IMPROVE"] = St1
                df1.at[r1, 1] = a[i + 1]
        else:
            df1.at[aa[0], bb[0] + 1] = "unkonwn"
            df1.at[aa[0], bb[0] + 2] = "unkonwn"
    df1 = df1.sort_values('IMPROVE')
    df1 = df1.reset_index(drop=True)
    # print(df1)
    r, c = df1.shape
    for i in range(r):
        countf = -1
        for xy in li:
            countf = countf + 1
            # print(countf)
            if (df1.iat[i, 1] == xy):
                tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', df1.iat[i, 0].lower())]
                b = []
                for y in tokens:
                    cou = cou + 1
                    if (y == "," or y == "." or y == "!" or y == "?" or y == ";"):
                        cou = cou - 1
                    else:
                        s = (sd[countf] == y).any()
                        p = s.index[s]
                        if (p.any() != 0):
                            if (len(p) > 1):
                                for k in p:
                                    b.append(str(k))
                            else:
                                b.append(str(p[0]))
                b = np.unique(b)
                if (len(b) != 0):
                    df1.at[i, 2] = b[0]
                    for j in range(len(b) - 1):
                        r1, c1 = df1.shape
                        df1.at[r1, "IMPROVE"] = df1.iat[i, 0]
                        df1.at[r1, 1] = df1.iat[i, 1]
                        df1.at[r1, 2] = b[j + 1]
                else:
                    df1.at[i, 2] = "unkonwn"

    df1 = df1.sort_values('IMPROVE')
    df1 = df1.reset_index(drop=True)
    # print(df1)
    return (df1)


def getsentiment(df1):
    stemmed_sentences = df1['IMPROVE'].tolist()
    count = -1
    for row in stemmed_sentences:
        count = count + 1
        sentence_analysis = []
        analysis = TextBlob(row)
        a = analysis.sentiment
        if a.polarity >= 0.1:
            df1.at[count, 3] = "positive"
        else:
            df1.at[count, 3] = "negative"

    return df1


def store(df, url):
    df.to_csv(url)


sd, dm = getdictionary('./domains_dictionary/Domains-and-subdomains.xlsx')
df1 = getreviews('./uploaded_files/comments_csv.csv')
df1 = dandsd(df1, dm, sd)
df1 = getsentiment(df1)
store(df1, './output_files/out1.csv')

# In[13]:


df1.columns = ['IMPROVE', 'DOMAIN', 'SUBDOMAIN', 'SENTIMENT']
#print(df1)

# In[ ]:


# In[ ]:


# In[ ]:


# In[14]:
domains = {
    'chartTitle': 'Overall Results across all Domains',
    'labels': [],
    'positive': [],
    'negative': []
}

assessment = {
    'chartTitle': 'Results for Comments on Assessment',
    'labels': [],
    'positive': [],
    'negative': []
}

course = {
    'chartTitle': 'Results for Comments on Course',
    'labels': [],
    'positive': [],
    'negative': []
}

outcomes = {
    'chartTitle': 'Results for Comments on Outcomes',
    'labels': [],
    'positive': [],
    'negative': []
}

staff = {
    'chartTitle': 'Results for Comments on Staff',
    'labels': [],
    'positive': [],
    'negative': []
}

support = {
    'chartTitle': 'Results for Comments on Support',
    'labels': [],
    'positive': [],
    'negative': []
}


g1 = df1.groupby(["DOMAIN", "SUBDOMAIN", "SENTIMENT"]).count().reset_index()
domnames = g1.DOMAIN.unique()

for dom in domnames:
    dpcount = 0
    dncount = 0
    domains['labels'].append(dom)
    sdomnames = g1.query('DOMAIN == @dom').SUBDOMAIN.unique()
    for sdom in sdomnames:
        tp = 0
        tn = 0
        tp = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "positive"').IMPROVE.sum()
        tn = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "negative"').IMPROVE.sum()
        dpcount += tp
        dncount += tn
        if dom == "ASSESSMENT":
            assessment['labels'].append(sdom)
            assessment['positive'].append(tp)
            assessment['negative'].append(tn)
        elif dom == "COURSE/UNIT DESIGN":
            course['labels'].append(sdom)
            course['positive'].append(tp)
            course['negative'].append(tn)
        elif dom == "OUTCOMES":
            outcomes['labels'].append(sdom)
            outcomes['positive'].append(tp)
            outcomes['negative'].append(tn)
        elif dom == "STAFF":
            staff['labels'].append(sdom)
            staff['positive'].append(tp)
            staff['negative'].append(tn)
        elif dom == "SUPPORT":
            support['labels'].append(sdom)
            support['positive'].append(tp)
            support['negative'].append(tn)
    domains['positive'].append(dpcount)
    domains['negative'].append(dncount)

print(domains)
print(assessment)
print(course)
print(support)
print(staff)
print(outcomes)








    #domains['positive'].append(g1.query('DOMAIN == dom',)

#g1 = df1.groupby(["DOMAIN", "SENTIMENT"]).count()
#print(g1)
#g2 = g1.count().reset_index()
#print(g2)

# g1.count().to_dict('dict')
# df1.groupby('DOMAIN').reset_index().first()
# print(df1)#.size().to_frame('size').reset_index().sort_values(['iso_country', 'size'], ascending=[True, False])


# In[15]:


# g1.apply(reset_index(drop=True))
# for key, item in g1:
#   print(g1.get_group(key), "\n\n")
# g1.describe()
# print(df1.loc[:,1:10])
# g1 = g1.reset_index(drop=True)
# store(g1,'C:/Users/Krishna Asrith/Desktop/sample4.csv')


# In[ ]:
