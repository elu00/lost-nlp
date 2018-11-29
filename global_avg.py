from textblob import TextBlob
text = open('data/review1.txt', 'r').read() # open a document
a = TextBlob(text)
