import pandas as pd
from pandas import *
import re
from textblob import TextBlob


def getdictionary(url):
    xls = ExcelFile(url)  # synonyms for domains
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
    xls = ExcelFile(url1)  # sampe strings
    df1 = xls.parse(xls.sheet_names[2])
    # print(df1)
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
            if y == "," or y == "." or y == "!" or y == "?" or y == ";":
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
                    if y == "," or y == "." or y == "!" or y == "?" or y == ";":
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


sd, dm = getdictionary('C:/Users/Krishna Asrith/Desktop/project analysis and design SIT764/Domains-and-subdomains.xlsx')
df1 = getreviews(
    'C:/Users/Krishna Asrith/Desktop/project analysis and design SIT764/Spero-a-master/Spero-a Front-End/De-identified student comments.xlsx')
df1 = dandsd(df1, dm, sd)
df1 = getsentiment(df1)
store(df1, 'C:/Users/Krishna Asrith/Desktop/sample3.csv')
