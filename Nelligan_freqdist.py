#frequency distributions of words for cleaned text, verbs, adjs, advbs
import codecs
import nltk
from nltk import Text
from nltk.tokenize import *
from nltk.probability import *
import matplotlib
matplotlib

#get length, lexical diversity
g = codecs.open('fulleg.txt', 'r', 'utf-8')
s = codecs.open('fulles.txt', 'r', 'utf-8')
raw_fileg = g.read()
raw_files = s.read()
tokensg = word_tokenize(raw_fileg)
tokenss = word_tokenize(raw_files)
len_eg = len(tokensg)
len_es = len(tokenss)
ld_eg = len_eg/len(set(tokensg))
ld_es = len_es/len(set(tokenss))
print("Lex Diversity of Ender's Game:", ld_eg, "  Lex Diversity of Ender's Shadow:", ld_es)

#get freq dist
g = codecs.open('egcleaned.txt', 'r', 'utf-8')
s = codecs.open('escleaned.txt', 'r', 'utf-8')

#g = codecs.open('egverbs.txt', 'r', 'utf-8')
#s = codecs.open('esverbs.txt', 'r', 'utf-8')

#g = codecs.open('egadjs.txt', 'r', 'utf-8')
#s = codecs.open('esadjs.txt', 'r', 'utf-8')

raw_fileg = g.read()
raw_files = s.read()
tokensg = word_tokenize(raw_fileg)
tokenss = word_tokenize(raw_files)
fdistg = FreqDist(tokensg)
for key in fdistg:
    fdistg[key] = fdistg[key]/len_eg
fdists = FreqDist(tokenss)
for key in fdists:
    fdists[key] = fdists[key]/len_eg
fdistg.plot(50, cumulative = False)
fdists.plot(50, cumulative = False)

