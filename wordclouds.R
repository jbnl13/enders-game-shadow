install.packages("wordcloud")
install.packages("tm")
install.packages("RColorBrewer")
library("wordcloud")
library("tm")
library("RColorBrewer")

#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/egcleaned.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/egverbs.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/egadjs.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/escleaned.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/esverbs.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/esadjs.txt'
words <- readChar(fileName, file.info(fileName)$size)
words <- unlist(strsplit(words, ' '))
wordcloud(words, random.order=FALSE, max.words=70, colors=brewer.pal(8,"Set1"))