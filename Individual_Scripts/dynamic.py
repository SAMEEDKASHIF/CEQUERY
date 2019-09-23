import nltk
import pandas as pd
from nltk.corpus import stopwords
import re
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from pycorenlp import StanfordCoreNLP
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_excel('De-identified student comments.xlsx', columns=["HELPFUL", "IMPROVE"])
df = pd.concat(df[frame] for frame in df.keys())
df = df.dropna(axis=0)

def remove_special_characters(text, remove_digits=False):
   pattern = r'[^a-zA-z0-9\.\s]' if not remove_digits else r'[^a-zA-z\.\s]'
   text = re.sub(pattern, '', text)
   return text

q = []
for index in df:
    special = remove_special_characters(index,remove_digits=True)
    q.append(special)

def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

w = []
for idx in q:
    stem_words = simple_stemmer(idx)
    w.append(stem_words)

filtered_words = [word.lower() for word in w if word not in stopwords.words('english')]
#print(filtered_words)

sentences = ""
for items in filtered_words:
    sentences += items
#print(sentences)

strg = re.sub(r'\s([?.!"](?:\s|$))', r'\1', sentences)
strg = strg.replace(" .",".")
strg = strg.replace(". ",".")
strg = strg.replace(".",". ")

savefile = open("sentences.txt","w")
savefile.write(strg)
savefile.close()

#java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate(strg,
                   properties={
                       'annotators': 'parse',
                       'outputFormat': 'json',
                       'timeout': 550000,
                   })

#pos = 0
#neg = 0
#veryPos = 0
#veryNeg = 0
#neutral = 0
#for s in res["sentences"]:
#    if(s["sentiment"] == "Positive"):
#        pos += 1
#    if (s["sentiment"] == "Negative"):
#        neg += 1
#    if (s["sentiment"] == "Verynegative"):
#        veryNeg += 1
#    if (s["sentiment"] == "Verypositive"):
#        veryPos += 1
#    if (s["sentiment"] == "Neutral"):
#        neutral += 1

#    print("%d: '%s': %s %s" % (
#        s["index"],
#        " ".join([t["word"] for t in s["tokens"]]),
#        s["sentimentValue"], s["sentiment"]))
#print("Positive:",pos,"Negative:",neg,"Neutral:",neutral,"Very Positive:",veryPos,"Very Negative:",veryNeg)

#print("-----------------------------------------------------------------------------------------------------------------")
#"(ROOT (S (SBAR (IN Though) (S (NP (PRP he)) (VP (VBD was) (ADJP (RB very) (JJ rich))))) (, ,) (NP (PRP he)) (VP (VBD was) (ADVP (RB still)) (ADJP (RB very) (JJ unhappy))) (. .)))"

from nltk import Tree
for i in range(len(res["sentences"])):
    parse_str = res["sentences"][i]["parse"]
    #print(parse_str)
    t = Tree.fromstring(parse_str)
    #print(t)
    subtexts = []
    for subtree in t.subtrees():
        #print(subtree[])
        if subtree.label() == "S":
            #print(' '.join(subtree.leaves()))
            subtexts.append(' '.join(subtree.leaves()))
        #print(subtexts)
    presubtexts = subtexts[:]
    #print(presubtexts)
    #df = pd.DataFrame(data=presubtexts)
    #df = df.dropna()
    if (len(presubtexts)>=1):
        count = 1
        for k in presubtexts:
            if(count == 1):
                count = 0
            else:
                print(presubtexts[0])
                print(k)
      #print(presubtexts[0])

    #for i in reversed(range(len(subtexts)-1)):
    #    sub = subtexts[i]
    #subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]

    #leftover = presubtexts[0][presubtexts[0].index(presubtexts[1])+len(presubtexts[1]):]
    #print(leftover)

    #print(l)

    # from textblob import TextBlob
    # !pip install stanfordnlp
    # !pip install textblob vadersentiment
    # from vadersentiment.vadersentiment import SentimentIntensityAnalyzer
    # print(fullStr)
    # sentence_analysis=[]
    # for row in stemmed_sentences:
    #  analysis = TextBlob(row)
    #  sentence_with_sentiment=[row,analysis.sentiment]
    #  sentence_analysis.append(sentence_with_sentiment)

    # print(sentence_analysis)

    # pos_count = 0
    # pos_positive = 0
    # pos_negative = 0
    # for row in sentence_analysis:
    #   pos_count +=1
    #   if row[1].polarity > 0.5:
    #      pos_positive += 1
    #
    #   if row[1].polarity < 0.5:
    #      pos_negative+=1
    # print(pos_count)
    # print(pos_positive)
    # print(pos_negative)
