install.packages("syuzhet")
library(syuzhet)

#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/fulleg.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/egverbs.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/egadjs.txt'

eg <- readChar(fileName, file.info(fileName)$size)
eg <- unlist(strsplit(eg, " "))
sentiment_vectorg <- get_sentiment(eg, method="bing")

ft_values <- get_transformed_values(sentiment_vectorg, 
                                    low_pass_size = 3, x_reverse_len = 100,
                                    scale_vals = TRUE, scale_range = FALSE)

plot(ft_values, type ="h", main ="Ender's Game using Transformed Values", 
     xlab = "Narrative Time", ylab = "Emotional Valence", col = "red")


#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/fulles.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/esverbs.txt'
#fileName <- 'C:/Users/Jackie/Desktop/CompLingFinal/esadjs.txt'

es <- readChar(fileName, file.info(fileName)$size)
es <- unlist(strsplit(es, " "))
sentiment_vector <- get_sentiment(es, method="bing")

fts_values <- get_transformed_values(sentiment_vector, 
                                    low_pass_size = 3, x_reverse_len = 100,
                                    scale_vals = TRUE, scale_range = FALSE)

plot(fts_values, type ="h", main ="Ender's Shadow using Transformed Values", 
     xlab = "Narrative Time", ylab = "Emotional Valence", col = "red")