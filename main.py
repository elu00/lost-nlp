from textblob import TextBlob
import pickle
import sys

n = sys.argv[1]
chars = {"jin", "sun", "jack", "kate", "sawyer", "juliet"}
charData = {}
pos = set(["JJ", "RB", "RBR", "RBS"])
i = 0
f = open('data/out' + n + '.txt', 'r')
text = f.read() # open a document
a = TextBlob(text)
f.close()
for char in chars:
    charData[char] = [[], {}]
for sentence in a.sentences:
    sentiment = sentence.sentiment.polarity
    descr = [tag[0] for tag in sentence.tags if tag[1] in pos]
    for char in chars:
        if sentence.word_counts[char] > 0:
            charData[char][0].append(sentiment)
            for word in descr:
                charData[char][1][word] = charData[char][1].get(word, 0) + 1
    i += 1
    print("Processed sentence", i)

pickle.dump( charData, open( "charData"+ n + ".p", "wb" ) )
