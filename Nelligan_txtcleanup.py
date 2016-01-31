import nltk
#nltk.download()
#nltk.download('stopwords')
from nltk import text
from nltk.corpus import stopwords
from nltk.tokenize import *
import re
import codecs
import json

#the text files were stripped of forewords and afterwords as well as chapter titles
#(using Geany: regex ^.*Chapter.*$ for Ender's Game and ^[0-9]*$ for Ender's Shadow
#and then deleting titles by hand) before being processed in Python


#create stopwords list including proper nouns
adjstopwords = stopwords.words('english')
names = ['bugger','ender','third','wiggin', 'peter', 'valentine', 'bean', 'andrew', 'alai', 'petra', 'graff',
         'anderson', 'major','bernard', 'carn','carby','chamrajnagar','admiral','crazy','tom','hegemon',
         'imbu', 'bonzo', 'madrid', 'fly,' 'molo','dink','meeker','rose','de','polemarch',
         'mazer','rackham','shen','stilson','locke','demontheses',
         'poke', 'achilles', 'nikolai', 'carlotta', 'volescu', 'anton', 'julian', 'seargent',
         'ullysses','rotterdam','dap', 'dimak', 'said']
for i in names:
    adjstopwords.append(i)

#clean texts
texts = ["endersgame", "endersshadow"]
cleaned_texts = []
nostopwords = []
for token_list in texts:
    f = codecs.open(token_list+'.txt', 'r', 'utf-8')
    raw_file = f.read()
    raw_file = re.sub("\W", " ", raw_file) #deletes punctuation
    raw_file = re.sub("\d", " ", raw_file) #deletes numbers
    tokens = word_tokenize(raw_file) #tokenize
    tokens = [w.lower() for w in tokens] #lowercase everything
    cleaned_texts.append([word for word in tokens])
    nostopwords.append([word for word in tokens if word not in adjstopwords]) #remove stopwords
egcleaned = nostopwords[0]
escleaned = nostopwords[1]

fulleg = cleaned_texts[0]
fulles = cleaned_texts[1]

#tag and make groups of adj, verb
tagged_eg = nltk.pos_tag(egcleaned)
egverbs = []
egadjs = []
for token, tag in tagged_eg:
    if tag.startswith('JJ'):
        egadjs.append(token)
    if tag.startswith('VB'):
        egverbs.append(token)

tagged_es = nltk.pos_tag(escleaned)
esverbs = []
esadjs = []
for token, tag in tagged_es:
    if tag.startswith('JJ'):
        esadjs.append(token)
    if tag.startswith('VB'):
        esverbs.append(token)

#write to text files
with open("fulleg.txt", "wt") as f:
    for s in fulleg:
        f.write(s + " ")

with open("fulles.txt", "wt") as f:
    for s in fulles:
        f.write(s + " ")

with open("egcleaned.txt", "wt") as f:
    for s in egcleaned:
        f.write(s + " ")

with open("egverbs.txt", "wt") as f:
    for s in egverbs:
        f.write(s + " ")

with open("egadjs.txt", "wt") as f:
    for s in egadjs:
        f.write(s + " ")

with open("escleaned.txt", "wt") as f:
    for s in escleaned:
        f.write(s + " ")

with open("esverbs.txt", "wt") as f:
    for s in esverbs:
        f.write(s + " ")

with open("esadjs.txt", "wt") as f:
    for s in esadjs:
        f.write(s + " ")



